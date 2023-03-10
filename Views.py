#### Importações ####
from pandastable import Table
from tkinter import *
from tkinter import messagebox
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
    con.commit()
    con.close()

#### CRUD ####

def Select(i):
    con = sql.connect(f'.\\Gen\\Account.db')
    cur = con.cursor()

    Query = '''
                SELECT * FROM ACCOUNTS WHERE ID=?
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
def DeleteAccount():
    class DeleteAccountId(Tk):
        def __init__(self):
            super().__init__()

            self.title('Deletar Conta')
            # self.geometry('450x300')
            self.DefaultFont = 'Arial'
            self.configure(bg='#3F3C52')
            self.DefaultBg = '#3F3C52'

            self.DefaultPadding = {'padx': 10,
                                    'pady': 10}

            self.FirstContainer = Frame(self)
            self.FirstContainer['bg'] = self.DefaultBg
            self.FirstContainer.pack()

            self.SecondContainer = Frame(self)
            self.SecondContainer['bg'] = self.DefaultBg
            self.SecondContainer.pack()

            self.IdLabel = Label(self.FirstContainer)
            self.IdLabel['text'] = 'Insira o Id:'
            self.IdLabel['font'] = (self.DefaultFont,10,'bold')
            self.IdLabel['foreground'] = 'white'
            self.IdLabel['bg'] = self.DefaultBg
            self.IdLabel.pack(side=LEFT,**self.DefaultPadding)

            self.IDEntry = Entry(self.FirstContainer)
            self.IDEntry['font'] = (self.DefaultFont, 10)       
            self.IDEntry.pack(side=LEFT,**self.DefaultPadding)      

            self.IdBtt = Button(self.SecondContainer)
            self.IdBtt['text'] = 'Confirmar'
            self.IdBtt['font'] = (self.DefaultFont, 10, 'bold')   
            self.IdBtt['command'] = self.GetId
            self.IdBtt.pack(side=LEFT, **self.DefaultPadding)     

        def GetId(self):
            Id = self.IDEntry.get()
            Delete(Id)
            messagebox.showinfo('Deletar Conta', 'Conta Deletada com sucesso!')

    return DeleteAccountId()

def ViewsAccounts():

    Data = []
    Con = sql.connect(f'.\\Gen\\Account.db')
    Cur = Con.cursor()

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
    
    Con.close()
    return View()