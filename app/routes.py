import os
from flask import render_template, current_app, jsonify, request

EXTENSIONS_PATH = {
    '.py': 'python',
    '.java': 'java'
}


@current_app.route('/')
def home():
    return render_template('index.html')

@current_app.route('/python')
def python():
    return render_template('/languages/python/main.html')

@current_app.route('/java')
def java():
    return  render_template('/languages/java/main.html')

@current_app.route('/add_file', methods=['GET', 'POST'])
def edd_file():
    if request.method == 'POST':
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

    return "", 500

@current_app.route('/<language>/list')
def send_list(language):
    language_folder = os.path.join(current_app.root_path + '/static/languages/' + language)
    try:
        files = os.listdir(language_folder)
        return jsonify(files) , 200
    except FileNotFoundError:
        return jsonify({"error": "Folder not found"}), 404