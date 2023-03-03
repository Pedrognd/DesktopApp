from random import choice
import string
from tkinter import ttk as c
from tkinter import *

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
    
  def Generator(self):  
    valores = string.ascii_letters + string.digits
    senha = ''
    for i in range(tamanho):
      senha += choice(valores)

    self.CopyPassword['state'] = 'only'
    self.CopyPassword.delete(0,END)
    self.CopyPassword.insert(0,senha)
    self.CopyPassword['state'] = 'readonly'
  
if __name__ == "__main__":
  root = AppPasswordGenerator()
  root.mainloop()