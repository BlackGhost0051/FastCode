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

    def create_language_folder(self):
        pass

    def verify_file(self, filename):
        pass