import os
import sqlite3


class DataBaseManager:
    DATABASE = 'database.db'

    DATABASE_STRUCTURE = '''
                                CREATE TABLE statistics (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                    chars TEXT,
                                    typing_speed REAL,
                                    file_name TEXT
                                )
    '''

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

    def get_statistics(self):
        statistics_data = []

        try:
            connect = sqlite3.connect(self.db_path)

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

            return statistics_data

        except sqlite3.Error as e:
            print(f"Error get statistics: {e}")
        finally:
            connect.close()

    def send_statistic(self, data, chars, typing_speed, file_name, current_time):
        try:
            connect = sqlite3.connect(self.db_path)
            cursor = connect.cursor()
            cursor.execute('''
                        INSERT INTO statistics (time, chars, typing_speed, file_name)
                        VALUES (?, ?, ?, ?)
                    ''', (current_time, chars, typing_speed, file_name))
            connect.commit()
            return {"message": "Statistics saved successfully"}
        except sqlite3.Error as e:
            return {"error": str(e)}
        finally:
            connect.close()

    def statistics_clear(self):
        try:
            connect = sqlite3.connect(self.db_path)
            cursor = connect.cursor()
            cursor.execute('DELETE FROM statistics')
            connect.commit()
            return "Clear"
        except sqlite3.Error as e:
            return "Error"
        finally:
            connect.close()
    def verify_password(self):
        self


    def loginUser(self):
        self

    def registerUser(self):
        self

