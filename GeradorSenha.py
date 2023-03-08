from random import choice
import string
from tkinter import ttk as c
from tkinter import *
from Connect_db import Connect_db

Connect_db()
tamanho = 20

class AppPasswordGenerator(Tk):
  def __init__(self):
    super().__init__()

    # Definições Padrões
    self.title('Gerenciador de Contas')
    self.geometry('400x400')
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

    self.FirstLabel = Label(self.FirstContainer)
    self.FirstLabel['text'] = 'Gerador de Senha'
    self.FirstLabel['font'] = (self.DefaultFont, 20, 'bold')
    self.FirstLabel['foreground'] = 'white'
    self.FirstLabel['bg'] = self.DefaultBg
    self.FirstLabel.pack(**self.DefaultPadding)

    self.CopyPassword = Entry(self.SecondContainer)
    self.CopyPassword['width'] = 25
    self.CopyPassword.pack(**self.DefaultPadding)

    self.BttGerar = Button(self.ThirdContainer)
    self.BttGerar['text'] = 'Gerar Senha'
    self.BttGerar['font'] = (self.DefaultFont, 10, 'bold')
    self.BttGerar['command'] = self.Generator
    self.BttGerar.pack(**self.DefaultPadding)

    self.SecondLabel = Label(self.FourthContainer)
    self.SecondLabel['text'] = 'Deseja vincular com uma conta?'
    self.SecondLabel['font'] = (self.DefaultFont, 10, 'bold')
    self.SecondLabel['foreground'] = 'white'
    self.SecondLabel['bg'] = self.DefaultBg
    self.SecondLabel.pack(**self.DefaultPadding)

    self.VincularBtt = Button(self.FifthContainer)
    self.VincularBtt['text'] = 'Vincular com uma conta'
    self.VincularBtt['font'] = (self.DefaultFont, 10, 'bold')
    # self.VincularBtt['command'] = self.Vincular
    self.VincularBtt.pack(side=LEFT,**self.DefaultPadding)

    self.VisuBtt = Button(self.FifthContainer)
    self.VisuBtt['text'] = 'Visualizar Contas'
    self.VisuBtt['font'] = (self.DefaultFont, 10, 'bold')
    # self.VisuBtt['command'] = self.Visu
    self.VisuBtt.pack(side=LEFT,**self.DefaultPadding)
    
  def Generator(self):  
    valores = string.ascii_letters + string.digits
    senha = ''
    for i in range(tamanho):
      senha += choice(valores)

    self.CopyPassword['state'] = 'normal'
    self.CopyPassword.delete(0,END)
    self.CopyPassword.insert(0,senha)
    self.CopyPassword['state'] = 'readonly'

  def Vincular(self):
    pass

  def Visu(self):
    pass
  
if __name__ == "__main__":
  root = AppPasswordGenerator()
  root.mainloop()