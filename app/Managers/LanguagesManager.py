import os

EXTENSIONS_PATH = {
    '.py': 'python',
    '.java': 'java',
    '.c': 'c',
    '.cpp': 'c++',
}


class LanguagesManager:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__))
        print(path)
    # verify languages folders by list

    def create_language_folder(self):
        pass

    def verify_file(self, filename):
        pass