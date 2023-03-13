from tkinter import ttk as s, messagebox
from tkinter import *
from Contas import *
from Download import *
from Juros import *

class AppMain(Tk):
    def __init__(self):
        super().__init__()

        # Definições Padrões
        self.title('Aplicação Principal')
        # self.geometry('450x300')
        self.DefaultFont = 'Arial'
        self.configure(bg='#3F3C52')
        self.DefaultBg = '#3F3C52'

        self.DefaultPadding = {'padx': 10,
                                'pady': 10}

        self.ContasBtt = Button(self)
        self.ContasBtt['text'] = 'Gerenciador de Contas'
        self.ContasBtt['command'] = self.StartContas
        self.ContasBtt.pack()

        self.DownloadBtt = Button(self)
        self.DownloadBtt['text'] = 'Download de Audio/Video'
        self.DownloadBtt['command'] = self.StartDownload
        self.DownloadBtt.pack()

        self.JurosBtt = Button(self)
        self.JurosBtt['text']= 'Simulação de juros'
        self.JurosBtt['command'] = self.StartJuros
        self.JurosBtt.pack()

    def StartContas(self):
        if __name__ == "__main__":
            root = AppLinkScreen()
            root.mainloop()

    def StartDownload(self):
        if __name__ == "__main__":
            root = AppDownload()
            root.mainloop()

    def StartJuros(self):
        if __name__ == "__main__":
            root = AppDownload()
            root.mainloop()
            
if __name__ == '__main__':
    root = AppMain()
    root.mainloop()