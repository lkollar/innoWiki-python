import sqlite3

"""
Schema:
CREATE TABLE history(id integer primary key, title varchar, summary text, content text, editor varchar, date text, historyid integer);
CREATE TABLE pages(id integer primary key, title varchar, summary text, content text, editor varchar, date text, historyid integer);
"""

class SQLiteDataStore(object):
    
    def __init__(self):
        #TODO error handling
        self.connection = sqlite3.connect("innowiki.sqlite")
        self.c = self.connection.cursor()


    def addActivePage(self, title, summary, content, editor, date, history_id):
        #TODO error handling
        self.c.execute("insert into pages values(NULL,?,?,?,?,?,?)", (title, summary, content, editor, date, history_id,))
        self.connection.commit()

    def getActivePage(self, title):
        self.c.execute("select * from pages where title=(?)", (title,))
        return self.c.fetchone()

    def getActivePageList(self):
        r = []
        self.c.execute("select id, title, summary, editor, date from pages order by id")
        for row in self.c:
            r.append(row)

        return r

    def addHistoryPage(self, title, summary, content, editor, date, history_id):
        self.c.execute("insert into history values(NULL,?,?,?,?,?,?)", (title, summary, content, editor, date, history_id,))
        self.connection.commit()

    def getHistoryPage(self, title):
        self.c.execute("select * from history where title=(?)", (title,))
        return self.c.fetchone()

    def getLastHistoryId(self):
        self.c.execute("select * from history order by id desc")
        row = self.c.fetchone()
        return row[0]

    def getHistoryPageListNewerThan(self, id):
        r = []
        self.c.execute("select id, title, summary, editor, date from pages where id > (?)", (id,))
        for row in self.c:
            r.append(row)

        return r


    def __del__(self):
        self.c.close()
