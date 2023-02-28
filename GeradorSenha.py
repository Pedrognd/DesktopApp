from random import choice
import string
from tkinter import ttk as c

tamanho = 20

from tkinter import *

class AppPasswordGenerator(Tk):
  def __init__(self):
    super().__init__()

    # Definições Padrões
    self.title('Gerenciador de Contas')
    self.geometry('800x600')
    self.DefaultFont = ('Arial',10,'bold')
    self.EntryFont = ('Arial',10)
    s = c.Style()

    self.DefaultPadding = {'padx': 10,
                            'pady': 10}
    
    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)
    
    self.FirstLabel = c.Label(self)
    self.FirstLabel['text'] = 'Gerador de senha'
    self.FirstLabel['font'] = ('Arial',20,'bold')
    self.FirstLabel.grid(column=0,row=0,sticky=W, **self.DefaultPadding)

    self.BttGenerator = c.Button(self)
    self.BttGenerator['text'] = 'Gerar Senha!'
    self.BttGenerator['command'] = self.Generator
    # self.BttGenerator['state'] = DISABLED
    self.BttGenerator.grid(column=0,row=1,sticky=W, **self.DefaultPadding)

    self.CopyPassword =  c.Entry(self)
    self.CopyPassword['width'] = 40
    self.CopyPassword.grid(column=0,row=2,sticky=W, **self.DefaultPadding)

    self.QuestionLabel = c.Label(self)
    self.QuestionLabel['text'] = ('Deseja vincular a uma conta existente?')
    self.QuestionLabel['font'] = self.DefaultFont
    self.QuestionLabel.grid(column=0,row=3,sticky=W, **self.DefaultPadding)

    self.SelectOption0 = c.Radiobutton(self)
    self.SelectOption0['text'] = 'Sim'
    self.SelectOption0.grid(column=0,row=4,sticky=W, **self.DefaultPadding)

    self.SelectOption1 = c.Radiobutton(self)
    self.SelectOption1['text'] = 'Não'
    self.SelectOption1.grid(column=1,row=4,sticky=W, **self.DefaultPadding)   
    
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