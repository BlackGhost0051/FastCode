import os
import sqlite3
from datetime import datetime
from flask import render_template, current_app, jsonify, request, Response

EXTENSIONS_PATH = {
    '.py': 'python',
    '.java': 'java',
    '.c': 'c'
}

DATABASE = 'database.db'

def db_init():
    path = os.path.join(os.path.dirname(__file__)) + "/" + DATABASE
    print(path)
    if not os.path.exists(path):
        try:
            connect = sqlite3.connect(path)
            cursor = connect.cursor()
            cursor.execute('''
                            CREATE TABLE statistics (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                chars TEXT,
                                typing_speed REAL,
                                file_name TEXT
                            )
            ''') # need change structure | failed_chars true_chars
            connect.commit()
            print("Database and table created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating database: {e}")
        finally:
            connect.close()
    else:
        print("Database already exists.")
    return path

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


@current_app.route('/statistics')
def statistics():
    return render_template('statistics.html'), 200

@current_app.route('/get_statistics')
def statistics_data():
    path = db_init()
    statistics_data = []

    try:
        connect = sqlite3.connect(path)
        cursor = connect.cursor()
        cursor.execute("SELECT time, chars, typing_speed, file_name FROM statistics")
        rows = cursor.fetchall()

        for row in rows:
            statistics_data.append({
                "time": row[0],
                "chars": row[1],
                "typing_speed": row[2],
                "file_name": row[3]
            })

        return jsonify(statistics_data), 200
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connect.close()
@current_app.route('/send_statistic', methods=['POST'])
def send_statistic():
    path = db_init()

    data = request.get_json()
    chars = data.get('chars')
    typing_speed = data.get('typing_speed')
    file_name = data.get('file_name')

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        connect = sqlite3.connect(path)
        cursor = connect.cursor()
        cursor.execute('''
                    INSERT INTO statistics (time, chars, typing_speed, file_name)
                    VALUES (?, ?, ?, ?)
                ''', (current_time, chars, typing_speed, file_name))
        connect.commit()
        return jsonify({"message": "Statistics saved successfully"}), 200

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connect.close()


@current_app.route('/statistics_clear')
def statistics_clear():
    path = db_init()
    try:
        connect = sqlite3.connect(path)
        cursor = connect.cursor()
        cursor.execute('DELETE FROM statistics')
        connect.commit()
        return "Clear", 200
    except sqlite3.Error as e:
        return render_template('/error.html', status_code=500, message=f"{e}"), 500
    finally:
        connect.close()

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