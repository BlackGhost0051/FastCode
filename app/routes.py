import os
from flask import render_template, current_app, jsonify, request, Response, session, make_response, url_for, redirect

from app.Managers.DataBaseManager import DataBaseManager
from app.Managers.JWTManager import JWTManager

EXTENSIONS_PATH = {
    '.py': 'python',
    '.java': 'java',
    '.c': 'c'
}




@current_app.errorhandler(404)
def page_not_found(e):
    return render_template('/error.html', status_code=404, message=str(e)), 404

@current_app.route('/')
def home():
    # languagesManager = LanguagesManager()
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))


    result = JWTManager.get_token_info(token)
    username = result["username"]

    return render_template('index.html', login=username)


@current_app.route('/profile/<login>', methods=['GET'])
def profile(login):
    return render_template('/profile.html', login=login)

@current_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        try:
            return render_template('/login.html'), 200
        except Exception as e:
            return render_template('/error.html', status_code=400, message=""), 400
    if request.method == 'POST':
        try:
            data = request.get_json()
            login = data.get('login')
            password = data.get('password')

            if not login or not password:
                return jsonify({"error": "Missing login or password"}), 400

            db_manager = DataBaseManager()
            user_id = db_manager.loginUser(login, password)

            if user_id:
                token = JWTManager.generate_token(user_id=user_id, username=login)

                response = make_response(
                    jsonify({"message": "Login successful"})
                )

                response.set_cookie(
                    'token',
                    token,
                    max_age=3600,
                    secure=True,
                    httponly=True,
                    samesite='Lax'
                )

                return response, 200
            else:
                return jsonify({"error": "Invalid login or password"}), 401
        except Exception as e:
            print(f"Error in login_post: {e}")
            return jsonify({"error": "An error occurred"}), 500

@current_app.route('/register', methods=['GET'])
def register_get():
    try:
        return render_template('/register.html'), 200
    except Exception as e:
        return render_template('/error.html', status_code=400, message=""), 400

@current_app.route('/register', methods=['POST'])
def register_post():
    data = request.get_json()

    login = data.get('login')
    password = data.get('password')

    if not login or not password:
        return jsonify({"error": "Missing login or password"}), 400

    db_manager = DataBaseManager()

    try:
        is_registered = db_manager.addUser(login, password)
        if is_registered:
            return jsonify({"message": "Register successful", "success": True}), 200
        else:
            return jsonify({"error": "User already exists", "success": False}), 409
    except Exception as e:
        print(f"Error in register_post: {e}")
        return jsonify({"error": "Internal server error", "success": False}), 500

@current_app.route('/change_password', methods=['POST'])
def change_password():
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))
    pass

@current_app.route('/<language>')
def python(language):
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))
    try:
        return render_template('/language.html', language=language)
    except Exception as e:
        return render_template('/error.html', status_code=400, message="File not found"), 400


@current_app.route('/statistics')
def statistics():
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))
    return render_template('statistics.html'), 200

@current_app.route('/get_statistics')
def statistics_data():
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))
    db_manager = DataBaseManager()

    login = "test"

    statistics_data =  db_manager.get_statistics(login)
    return jsonify(statistics_data), 200


@current_app.route('/send_statistic', methods=['POST'])
def send_statistic():
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))

    db_manager = DataBaseManager()

    login = "test"
    data = request.get_json()
    chars = data.get('chars')
    typing_speed = data.get('typing_speed')
    file_name = data.get('file_name')

    message = db_manager.send_statistic(login, chars, typing_speed, file_name)
    return jsonify(message), 200


@current_app.route('/statistics_clear')
def statistics_clear():
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))

    db_manager = DataBaseManager()


    login = "test"

    message = db_manager.statistics_clear(login)
    return message, 200

@current_app.route('/add_file', methods=['POST'])
def edd_file():
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))

    file = request.files['file']
    if file.filename == '':
        return render_template('/error.html', status_code=400, message="No selected file"), 400

    file_extension = os.path.splitext(file.filename)[1]
    file_path = os.path.join(current_app.root_path, 'static', 'languages', EXTENSIONS_PATH[file_extension], file.filename)

    if os.path.exists(file_path):
        return render_template('/error.html', status_code=400, message="File name is exist"), 400
    else:
        try:
            file.save(file_path)
            return f"File saved at {file_path}", 200
        except Exception as e:
            return render_template('/error.html', status_code=500, message=str(e)), 500


@current_app.route('/<language>/remove_file/<file_name>', methods=['POST'])
def remove_file(language ,file_name):
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))

    file_path = os.path.join(current_app.root_path + "/static/languages/" + language + "/" + file_name)
    print(file_path)

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            return "File removed successfully", 200
        except Exception as e:
            return render_template('/error.html', status_code=500, message=str(e)), 500
    else:
        return render_template('/error.html', status_code=400, message="File not found"), 400

@current_app.route('/<language>/get_code/<file_name>')
def get_file(language, file_name):
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))

    file_path = os.path.join(current_app.root_path + "/static/languages/" + language + "/" + file_name)

    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                code = file.read()
            return Response(code, mimetype='text/plain', status=200)

        except Exception as e:
            return render_template('/error.html', status_code=500, message=str(e)), 500
    else:
        return render_template('/error.html', status_code=400, message="File not found"), 400

@current_app.route('/typing', methods=['GET'])
def typing():
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))

    file = request.args.get('file')
    language = request.args.get('language')

    if file and language:
        return render_template('typing.html', file=file, language=language)

    return render_template('/error.html', status_code=400, message="File NULL"), 400

@current_app.route('/<language>/list')
def send_list(language):
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))

    language_folder = os.path.join(current_app.root_path + '/static/languages/' + language)
    try:
        files = os.listdir(language_folder)
        return jsonify(files) , 200
    except FileNotFoundError:
        return render_template('/error.html', status_code=404, message="Folder not found"), 404

@current_app.route('/languages_list')
def languages_list():
    token = request.cookies.get('token')
    if not JWTManager.verify_token(token):
        return redirect(url_for('login'))

    try:
        return jsonify(EXTENSIONS_PATH), 200
    except Exception as e:
        return render_template('/error.html', status_code=500, message="Something go wrong"), 500