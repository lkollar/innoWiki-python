import sqlite3

class SQLiteDataStore(object):
    
    def __init__(self):
        #TODO error handling
        self.connection = sqlite3.connect("innowiki.sqlite")
        self.c = self.connection.cursor()

    def addPage(self, title, summary, content, editor, date, history_id):
        self.c.execute("insert into pages values(NULL,?,?,?,?,?,?)", (title, summary, content, editor, date, history_id,))
        self.connection.commit()

    def __del__(self):
        self.c.close()
