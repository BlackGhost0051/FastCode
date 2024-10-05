import os
import sqlite3
from flask import render_template, current_app, jsonify, request, Response

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
    return render_template('index.html')

@current_app.route('/<language>')
def python(language):
    try:
        return render_template('/language.html', language=language)
    except Exception as e:
        return render_template('/error.html', status_code=400, message="File not found"), 400

# Add route
# clear statistics
# send statistics

@current_app.route('/statistics')
def statistics():
    # check if is database
    # if not make
    # get info from database statistic
    return render_template('statistics.html'), 200

@current_app.route('/add_file', methods=['POST'])
def edd_file():
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
    file = request.args.get('file')
    language = request.args.get('language')

    if file and language:
        return render_template('typing.html', file=file, language=language)

    return render_template('/error.html', status_code=400, message="File NULL"), 400

@current_app.route('/<language>/list')
def send_list(language):
    language_folder = os.path.join(current_app.root_path + '/static/languages/' + language)
    try:
        files = os.listdir(language_folder)
        return jsonify(files) , 200
    except FileNotFoundError:
        return render_template('/error.html', status_code=404, message="Folder not found"), 404

@current_app.route('/languages_list')
def languages_list():
    try:
        return jsonify(EXTENSIONS_PATH), 200
    except Exception as e:
        return render_template('/error.html', status_code=500, message="Something go wrong"), 500