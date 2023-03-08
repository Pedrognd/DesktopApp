import sqlite3 as sql
import os

def Connect_db():
    dire = f'.\\Gen'
    if os.path.isdir(dire):
        pass
    else:
        os.mkdir(dire)

    con = sql.connect('./Gen/accounts.db')
    cur = con.cursor()

    table = """CREATE TABLE IF NOT EXISTS CONTAS
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    LOCAL TEXT NOT NULL,
    USER  TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    SENHA TEXT NOT NULL )"""

    cur.execute(table)