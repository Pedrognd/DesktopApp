from random import choice
import string
from tkinter import ttk as c

tamanho = 20

from tkinter import *

class AppPasswordGenerator(Tk):
  def __init__(self):
    super().__init__()

    # Definições Padrões
    self.title('Gerador de Senha')
    self.geometry('375x312')
    self.resizable(0,0)
    self.DefaultFont = ('Arial',10,'bold')
    self.EntryFont = ('Arial',10)
    s = c.Style()

    self.DefaultPadding = {'padx': 10,
                            'pady': 10}
    
    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)
    
    self.BttGenerator = c.Button(self)
    self.BttGenerator['text'] = 'Gerar Senha!'
    self.BttGenerator['command'] = self.Generator
    self.BttGenerator.grid(column=0,row=0,columnspan=2,sticky=N, **self.DefaultPadding)

    self.CopyPassword =  c.Entry(self)
    self.CopyPassword['width'] = 50
    self.CopyPassword.grid(column=0,row=2,columnspan=2,sticky=N, **self.DefaultPadding)

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