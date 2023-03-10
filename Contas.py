import sqlite3 as sql
import pandas as pd
import string
import os
from tkinter import ttk as c, messagebox
from pandastable import Table
from random import choice
from tkinter import *
from Views import *


class AppLinkScreen(Tk):
    def __init__(self):
        super().__init__()

        # Definições Padrões
        self.title('Vincular Contas')
        self.geometry('450x300')
        self.DefaultFont = 'Arial'
        self.configure(bg='#3F3C52')
        self.DefaultBg = '#3F3C52'

        self.DefaultPadding = {'padx': 10,
                                'pady': 10}
        
        # Separando o blocos
        self.FirstContainer = Frame(self)
        self.FirstContainer['bg'] = self.DefaultBg
        self.FirstContainer.pack()

        self.SecondContainer = Frame(self)
        self.SecondContainer['bg'] = self.DefaultBg
        self.SecondContainer.pack()

        self.ThirdContainer = Frame(self)
        self.ThirdContainer['bg'] = self.DefaultBg
        self.ThirdContainer.pack()

        self.FourthContainer = Frame(self)
        self.FourthContainer['bg'] = self.DefaultBg
        self.FourthContainer.pack()

        self.FifthContainer = Frame(self)
        self.FifthContainer['bg'] = self.DefaultBg
        self.FifthContainer.pack()

        self.SixthContainer = Frame(self)
        self.SixthContainer['bg'] = self.DefaultBg
        self.SixthContainer.pack()

        self.SeventhContainer = Frame(self)
        self.SeventhContainer['bg'] = self.DefaultBg
        self.SeventhContainer.pack()

        self.FirstLabel = Label(self.FirstContainer)
        self.FirstLabel['text'] = 'Salvar conta'
        self.FirstLabel['font'] = (self.DefaultFont, 20, 'bold')
        self.FirstLabel['foreground'] = 'white'
        self.FirstLabel['bg'] = self.DefaultBg
        self.FirstLabel.pack(**self.DefaultPadding)

        self.LocalLabel = Label(self.SecondContainer)
        self.LocalLabel['text'] = 'Local da Conta:'
        self.LocalLabel['font'] = (self.DefaultFont, 10, 'bold')
        self.LocalLabel['foreground'] = 'white'
        self.LocalLabel['bg'] = self.DefaultBg
        self.LocalLabel.pack(side=LEFT,padx=11,pady=10)

        self.LocalEntry = Entry(self.SecondContainer)
        self.LocalEntry['font'] = (self.DefaultFont, 10)       
        self.LocalEntry.pack(side=LEFT)

        self.UserLabel = Label(self.ThirdContainer)
        self.UserLabel['text'] = 'Usuario da Conta:'
        self.UserLabel['font'] = (self.DefaultFont, 10, 'bold')
        self.UserLabel['foreground'] = 'white'
        self.UserLabel['bg'] = self.DefaultBg
        self.UserLabel.pack(side=LEFT,padx=5,pady=10)

        self.UserEntry = Entry(self.ThirdContainer)
        self.UserEntry['font'] = (self.DefaultFont, 10)       
        self.UserEntry.pack(side=LEFT)

        self.EmailLabel = Label(self.FourthContainer)
        self.EmailLabel['text'] = 'Email da Conta:'
        self.EmailLabel['font'] = (self.DefaultFont, 10, 'bold')
        self.EmailLabel['foreground'] = 'white'
        self.EmailLabel['bg'] = self.DefaultBg
        self.EmailLabel.pack(side=LEFT,padx=11,pady=10)

        self.EmailEntry = Entry(self.FourthContainer)
        self.EmailEntry['font'] = (self.DefaultFont, 10)       
        self.EmailEntry.pack(side=LEFT)

        self.PassWordLabel = Label(self.SixthContainer)
        self.PassWordLabel['text'] = 'Senha da Conta:'
        self.PassWordLabel['font'] = (self.DefaultFont, 10, 'bold')
        self.PassWordLabel['foreground'] = 'white'
        self.PassWordLabel['bg'] = self.DefaultBg
        self.PassWordLabel.pack(side=LEFT,padx=8,pady=10)

        self.PassWordEntry = Entry(self.SixthContainer)
        self.PassWordEntry['width'] = 25
        self.PassWordEntry['font'] = (self.DefaultFont, 10)       
        self.PassWordEntry.pack(side=LEFT)

        self.PassWordBtt = Button(self.SixthContainer)
        self.PassWordBtt['text'] = 'Gerar'
        self.PassWordBtt['font'] = (self.DefaultFont, 10, 'bold')   
        self.PassWordBtt['command'] = self.Gerar    
        self.PassWordBtt.pack(side=LEFT, **self.DefaultPadding)

        self.BttSave = Button(self.SeventhContainer)
        self.BttSave['text'] = 'Salvar'
        self.BttSave['font'] = (self.DefaultFont, 10, 'bold')
        self.BttSave['command'] = self.Save
        self.BttSave.pack(side=LEFT,**self.DefaultPadding)

        self.BttEdit = Button(self.SeventhContainer)
        self.BttEdit['text'] = 'Editar'
        self.BttEdit['font'] = (self.DefaultFont, 10, 'bold')
        self.BttEdit['command'] = self.Delete
        self.BttEdit.pack(side=LEFT,**self.DefaultPadding)

        self.BttView = Button(self.SeventhContainer)
        self.BttView['text'] = 'Visualizar'
        self.BttView['font'] = (self.DefaultFont, 10, 'bold')
        self.BttView['command'] = self.View
        self.BttView.pack(side=LEFT,**self.DefaultPadding)

    def Gerar(self):

        valores = string.ascii_letters + string.digits
        senha = ''
        for i in range(20):
            senha += choice(valores)

        self.PassWordEntry.delete(0,END)
        self.PassWordEntry.insert(0,senha)

    def Save(self):
        # Salvar conts no banco de dados
        Local = self.LocalEntry.get()
        User = self.UserEntry.get()
        Email = self.EmailEntry.get()
        PassWord = self.PassWordEntry.get()

        if (Local != '') & (User != '') & (Email != '') & (PassWord  != ''):
            Insert((Local,User,Email,PassWord))
            messagebox.showinfo("Cadastro", "Cadastro efetuado com sucesso.")
        else:
            messagebox.showinfo("Cadastro", "Preencha todos os campos!")
    
    def Delete(self):
        # digitar o id e deletar a conta do db
        pass

    def View(self):
        # Chamar tela de visualização das contas salvas
        if __name__ == '__main__':
            root0 = ViewsAccounts()
            root0.mainloop()

if __name__ == "__main__":
  root = AppLinkScreen()
  root.mainloop()