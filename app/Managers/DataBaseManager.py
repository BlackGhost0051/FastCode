import os
import sqlite3
import hashlib

from app.Managers.CryptoManager import CryptoManager


class DataBaseManager:
    DATABASE = 'database.db'

    DATABASE_STRUCTURE = """    
    
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        isAdmin BOOLEAN DEFAULT 0
    );

    CREATE TABLE statistics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL,
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        chars INTEGER,
        typing_speed REAL,
        file_name TEXT,
        FOREIGN KEY (login) REFERENCES users(login)
    );

    """


    def __init__(self):
        self.db_path = self.db_init()

    def db_init(self):
        path = os.path.join(os.path.dirname(__file__)) + "/../" + self.DATABASE
        print(path)
        if not os.path.exists(path):
            try:
                connect = sqlite3.connect(path)
                cursor = connect.cursor()
                cursor.execute(self.DATABASE_STRUCTURE)
                connect.commit()
                print("Database and table created successfully.")
            except sqlite3.Error as e:
                print(f"Error creating database: {e}")
            finally:
                connect.close()
        else:
            print("Database already exists.")
        return path

    def get_statistics(self, login: str):
        statistics_data = []

        try:
            connect = sqlite3.connect(self.db_path)
            connect.execute("PRAGMA foreign_keys = ON;")
            cursor = connect.cursor()

            cursor.execute("""
                SELECT time, chars, typing_speed, file_name
                FROM statistics WHERE login = ?;
            """, (login,))
            rows = cursor.fetchall()


            for row in rows:
                statistics_data.append({
                    "time": row[0],
                    "chars": row[1],
                    "typing_speed": row[2],
                    "file_name": row[3]
                })

            return statistics_data

        except sqlite3.Error as e:
            print(f"Error get statistics: {e}")
        finally:
            connect.close()

    def send_statistic(self, login: str, chars, typing_speed, file_name):
        try:
            connect = sqlite3.connect(self.db_path)
            connect.execute("PRAGMA foreign_keys = ON;")
            cursor = connect.cursor()
            cursor.execute("""
                            INSERT INTO statistics (login, chars, typing_speed, file_name)
                            VALUES (?, ?, ?, ?);
                        """, (login, chars, typing_speed, file_name))
            connect.commit()
            return {"message": "Statistics saved successfully"}
        except sqlite3.Error as e:
            return {"error": str(e)}
        finally:
            connect.close()

    def statistics_clear(self, login: str):
        try:
            connect = sqlite3.connect(self.db_path)
            connect.execute("PRAGMA foreign_keys = ON;")
            cursor = connect.cursor()
            cursor.execute("DELETE FROM statistics WHERE login = ?;", (login,))
            connect.commit()
            return "Clear"
        except sqlite3.Error as e:
            return "Error"
        finally:
            connect.close()

    def loginUser(self, login: str, password: str) -> bool:
        try:

            connect = sqlite3.connect(self.db_path)
            cursor = connect.cursor()
            cursor.execute('SELECT password FROM users WHERE login=?;', (login,))
            connect.commit()

            result = cursor.fetchone()
            if result:
                stored_password = result[0]
                return CryptoManager.verify_password(password, stored_password)
            else:
                return False
        except Exception as e:
            return False
        finally:
            connect.close()

    def addUser(self, login: str, password: str) -> bool:
        try:
            hashed_password = CryptoManager.make_hash(password)

            connect = sqlite3.connect(self.db_path)
            cursor = connect.cursor()
            cursor.execute('INSERT INTO users (login, password) VALUES (?, ?);', (login, hashed_password))
            connect.commit()

            return True
        except sqlite3.IntegrityError:
            return False
        except Exception as e:
            print(f"Error adding user: {e}")
            return False
        finally:
            connect.close()
