from flask import render_template, current_app

@current_app.route('/')
def home():
    return render_template('index.html')

@current_app.route('/python')
def python():
    return render_template('/languages/python/main.html')

@current_app.route('/java')
def java():
    return  render_template('/languages/java/main.html')