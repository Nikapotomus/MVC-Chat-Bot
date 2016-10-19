import sqlite3

class DB_Handler:
    def __init__(self):
        # Connecting to the database file
        sqlite_file = 'chat_bot_db.sqlite'    # name of the sqlite database file

        self.conn = sqlite3.connect(sqlite_file)
        self.c = self.conn.cursor()


    def get_all_phrases(self):

        self.c.execute("SELECT * FROM phrases")
        all_rows = self.c.fetchall()

        return all_rows
