import os
from flask import current_app

EXTENSIONS_PATH = {
    '.py': 'python',
    '.java': 'java',
    '.c': 'c',
    '.cpp': 'c++',
}


class LanguagesManager:
    def __init__(self):
        path = os.path.join(current_app.root_path, 'static', 'languages')
        print("LanguagesManager | ",path)

        for language in EXTENSIONS_PATH.values():
            if not os.path.exists(os.path.join(path, language)):
                os.makedirs(os.path.join(path, language))
                print(f"Folder '{path, language}' created.")

            print("LanguagesManager | ", language)

    # verify languages folders by list

    def get_extensions_path(self):
        return EXTENSIONS_PATH

    def create_language_folder(self):
        pass

    def verify_file(self, filename):
        pass

    def add_file(self, file):

        if file.filename == '':
            pass

        file_extension = os.path.splitext(file.filename)[1]
        file_path = os.path.join(current_app.root_path, 'static', 'languages', EXTENSIONS_PATH[file_extension], file.filename)

        if os.path.exists(file_path):
            pass
        else:
            try:
                file.save(file_path)
            except Exception as e:
                pass



    def remove_file(self, language, filename):
        file_path = os.path.join(current_app.root_path + "/static/languages/" + language + "/" + filename)

        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"File '{file_path}' deleted.")
            except Exception as e:
                pass
        else:
            pass

    def get_file(self, language, filename):
        file_path = os.path.join(current_app.root_path + "/static/languages/" + language + "/" + filename)

        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    code = file.read()
                return code
            except Exception as e:
                return False
        else:
            return False