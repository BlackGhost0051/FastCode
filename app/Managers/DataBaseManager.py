import os
import sqlite3


class DataBaseManager:
    DATABASE = 'database.db'

    def __init__(self):
        self.db_path = self.db_init()

    def db_init(self):
        path = os.path.join(os.path.dirname(__file__)) + "/../" + self.DATABASE
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
                ''')
                connect.commit()
                print("Database and table created successfully.")
            except sqlite3.Error as e:
                print(f"Error creating database: {e}")
            finally:
                connect.close()
        else:
            print("Database already exists.")
        return path

    def verify_password(self):
        self


    def loginUser(self):
        self

    def registerUser(self):
        self

