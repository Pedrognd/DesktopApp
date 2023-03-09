#### Importações ####
import sqlite3 as sql
import os
#### Create DataBase ####
def CreateDB(File):
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
    Cur = ConnectDb('Account.db')

    Query = '''
                SELECT ? FROM ACCOUNTS
    '''
    Cur(Query,i)

def Insert(i):
    Cur = ConnectDb('Account.db')

    Query = '''
                INSERT INTO ACCOUNTS(LOCAL,
                                     USER,
                                     EMAIL,
                                     PASSWORD)
                               VALUES(?,?,?,?)
    '''
    Cur.execute(Query,i)

def Update(i):
    Cur = ConnectDb('Account.db')

    Query = '''
                UPDATE ACCOUNTS SET LOCAL = ?,
                                    USER = ?,
                                    EMAIL = ?,
                                    PASSWORD = ?
                                    WHERE ID = ?    
    '''
    Cur.execute(Query,i)

def Delete(i):
    Cur = ConnectDb('Account.db')

    Query = '''
                DELETE FROM ACCOUNTS WHERE ID = ?
    '''
    Cur.execute(Query)

#### Funcs Proprias ####

# dados = []
# cur.execute('SELECT * FROM CONTAS')
# rows = cur.fetchall()
# for i in rows:
#     dados.append(i)
# df = pd.DataFrame(dados)
# df = df.rename(columns={0:'Id',
#                         1:'Local',
#                         2:'Usuario',
#                         3:'Email',
#                         4:'Senha'})
# f = Frame(self)
# f.pack(fill=BOTH,expand=1)
# self.table = pt = Table(f,dataframe=df,showstatusbar=False,showtoolbar=False)
# pt.show()