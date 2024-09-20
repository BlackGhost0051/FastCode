import os
from flask import render_template, current_app, jsonify, request, Response

EXTENSIONS_PATH = {
    '.py': 'python',
    '.java': 'java'
}


@current_app.route('/')
def home():
    return render_template('index.html')

@current_app.route('/<language>')
def python(language):
    try:
        return render_template('/languages/' + language + '/main.html')
    except Exception as e:
        return "File not found", 400


@current_app.route('/add_file', methods=['POST'])
def edd_file():
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    file_extension = os.path.splitext(file.filename)[1]
    file_path = os.path.join(current_app.root_path, 'static', 'languages', EXTENSIONS_PATH[file_extension], file.filename)

    if os.path.exists(file_path):
        return "File name is exist", 400
    else:
        try:
            file.save(file_path)
            return f"File saved at {file_path}", 200
        except Exception as e:
            return f"Error: {str(e)}", 500


@current_app.route('/<language>/remove_file/<file_name>', methods=['POST'])
def remove_file(language ,file_name):
    file_path = os.path.join(current_app.root_path + "/static/languages/" + language + "/" + file_name)
    print(file_path)

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            return "File removed successfully", 200
        except Exception as e:
            return f"Error removing file: {str(e)}", 500
    else:
        return "File not found", 400

@current_app.route('/<language>/get_code/<file_name>')
def get_file(language, file_name):
    file_path = os.path.join(current_app.root_path + "/static/languages/" + language + "/" + file_name)

    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                code = file.read()
            return Response(code, mimetype='text/plain', status=200)

        except Exception as e:
            return f"Error reading file: {str(e)}", 500
    else:
        return "File not found", 400

@current_app.route('/<language>/list')
def send_list(language):
    language_folder = os.path.join(current_app.root_path + '/static/languages/' + language)
    try:
        files = os.listdir(language_folder)
        return jsonify(files) , 200
    except FileNotFoundError:
        return jsonify({"error": "Folder not found"}), 404