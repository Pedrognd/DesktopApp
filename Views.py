#### Importações ####
from pandastable import Table
from tkinter import *
import pandas as pd
import sqlite3 as sql
import os

#### Create DataBase ####
def CreateDB(File):

    if os.path.isdir(f'.\\Gen'):
        pass
    else:
        os.makedirs(f'.\\Gen')

    con = sql.connect(f'.\\Gen\\{File}')
    cur = con.cursor()

    Table = '''
                CREATE TABLE IF NOT EXISTS ACCOUNTS(
                    ID      INTEGER PRIMARY KEY AUTOINCREMENT,
                    LOCAL   TEXT NOT NULL,
                    USER    TEXT NOT NULL,
                    EMAIL   TEXT NOT NULL,
                    PASSWORD   TEXT NOT NULL
                )
    '''
    
    cur.execute(Table)

#### Conexão ####

def ConnectDb(File):

    con = sql.connect(f'./Gen/{File}')
    cur = con.cursor()
    return cur


#### Crud ####

def Select(i):
    con = sql.connect(f'.\\Gen\\Account.db')
    cur = con.cursor()

    Query = '''
                SELECT ? FROM ACCOUNTS
    '''
    cur.execute(Query,i)

def Insert(i):
    con = sql.connect(f'.\\Gen\\Account.db')
    cur = con.cursor()

    Query = '''
                INSERT INTO ACCOUNTS(LOCAL,
                                     USER,
                                     EMAIL,
                                     PASSWORD)
                               VALUES(?,?,?,?)
    '''
    cur.execute(Query,i)
    con.commit()
    con.close()

def Update(i):
    con = sql.connect(f'.\\Gen\\Account.db')
    cur = con.cursor()

    Query = '''
                UPDATE ACCOUNTS SET LOCAL = ?,
                                    USER = ?,
                                    EMAIL = ?,
                                    PASSWORD = ?
                                    WHERE ID = ?    
    '''
    cur.execute(Query,i)
    con.commit()
    con.close()

def Delete(i):
    con = sql.connect(f'.\\Gen\\Account.db')
    cur = con.cursor()

    Query = '''
                DELETE FROM ACCOUNTS WHERE ID = ?
    '''
    cur.execute(Query,i)
    con.commit()
    con.close()

#### Funcs Proprias ####

def ViewsAccounts():

    Data = []
    Cur = ConnectDb('Account.db')
    Query = '''
                SELECT * FROM ACCOUNTS
            '''
    Cur.execute(Query)
    rows = Cur.fetchall()
    for row in rows:
        Data.append(row)
    df = pd.DataFrame(Data)
    df = df.rename(columns={0:'Id',
                            1:'Local',
                            2:'Usuario',
                            3:'Email',
                            4:'Senha'})
    class View(Tk):
        def __init__(self):
            super().__init__()

            self.title('Contas Salvas')
            
            self.FrameView = Frame(self)
            self.FrameView.pack(fill=BOTH,expand=1)
            self.Table = pt = Table(self.FrameView,dataframe=df,showstatusbar=False,showtoolbar=False,editable=False)
            pt.show()
    
    return View()