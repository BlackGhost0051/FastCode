import os
from flask import render_template, current_app, jsonify

@current_app.route('/')
def home():
    return render_template('index.html')

@current_app.route('/python')
def python():
    return render_template('/languages/python/main.html')

@current_app.route('/java')
def java():
    return  render_template('/languages/java/main.html')
@current_app.route('/<language>/list')
def send_list(language):
    language_folder = os.path.join(current_app.root_path + '/static/languages/' + language)
    try:
        files = os.listdir(language_folder)
        return jsonify(files) , 200
    except FileNotFoundError:
        return jsonify({"error": "Folder not found"}), 404