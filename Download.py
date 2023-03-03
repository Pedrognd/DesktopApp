# Antes de executar o codigo. Realizar os pip's:
# pip install pytube
# pip install moviepy
# from tkinter import ttk as c

# Importações Necessárias.
from tkinter import *
from tkinter import filedialog as dlg
from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import webbrowser, os
import re
import http.client

# Correção de erro, recorrente a versão do http.
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

class AppDownload(Tk):
    def __init__(self):
        super().__init__()

        # Definindo padrões
        self.geometry('375x340')
        self.title('Download')
        # self.iconbitmap('.\\baixar.ico')
        self.configure(bg='#3F3C52')
        self.DefaultBg = '#3F3C52'

        self.DefaultPadding = {'padx': 10,
                               'pady': 10}
        
        self.DefaultFont = 'Arial'

        # Declarando Variaveis
        self.CheckVar = IntVar()

        # Separando Blocos
        self.FirstContanier = Frame(self)
        self.FirstContanier['bg'] = self.DefaultBg
        self.FirstContanier.pack()

        self.SecondContanier = Frame(self)
        self.SecondContanier['bg'] = self.DefaultBg
        self.SecondContanier.pack()

        self.ThirdContanier = Frame(self)
        self.ThirdContanier['bg'] = self.DefaultBg
        self.ThirdContanier.pack()

        self.FourthContanier = Frame(self)
        self.FourthContanier['bg'] = self.DefaultBg
        self.FourthContanier.pack()

        self.FifthContanier = Frame(self)
        self.FifthContanier['bg'] = self.DefaultBg
        self.FifthContanier.pack()

        self.SixthContanier = Frame(self)
        self.SixthContanier['bg'] = self.DefaultBg
        self.SixthContanier.pack()

        # Inicio das customização
        self.Label0 = Label(self.FirstContanier)
        self.Label0['text'] = 'Download do Youtube'
        self.Label0['font'] = (self.DefaultFont,20,'bold')
        self.Label0['foreground'] = 'white'
        self.Label0['bg'] = self.DefaultBg
        self.Label0.pack(side=LEFT,**self.DefaultPadding)
        
        self.Label01 = Label(self.SecondContanier)
        self.Label01['text'] = 'Link do video:'
        self.Label01['font'] = (self.DefaultFont,10)
        self.Label01['foreground'] = 'white'
        self.Label01['bg'] = self.DefaultBg
        self.Label01.pack(side=LEFT, **self.DefaultPadding)

        self.Entry0 = Entry(self.SecondContanier)
        self.Entry0['width'] = 35
        self.Entry0['font'] = (self.DefaultFont,10)
        self.Entry0.pack(**self.DefaultPadding)

        self.BttDir = Button(self.ThirdContanier)
        self.BttDir['text'] = 'Selecione a pasta de destino'
        self.BttDir['font'] = (self.DefaultFont,10,'bold')
        self.BttDir['command'] = self.SelectDir
        self.BttDir.pack(**self.DefaultPadding)

        self.Label02 = Label(self.ThirdContanier)
        self.Label02['text'] = 'Selcione uma das opções:'
        self.Label02['font'] = (self.DefaultFont,10,'bold')
        self.Label02['foreground'] = 'white'
        self.Label02['bg'] = self.DefaultBg
        self.Label02.pack(**self.DefaultPadding)

        self.RadioBtt0 = Radiobutton(self.FourthContanier)
        self.RadioBtt0['text'] = 'Video/Mp4'
        self.RadioBtt0['font'] = (self.DefaultFont,10,'bold')
        self.RadioBtt0['value'] = 0
        self.RadioBtt0['variable'] = self.CheckVar
        # self.RadioBtt0['foreground'] = 'white'
        self.RadioBtt0['bg'] = self.DefaultBg
        self.RadioBtt0.pack(side=LEFT,**self.DefaultPadding)

        self.RadioBtt01 = Radiobutton(self.FourthContanier)
        self.RadioBtt01['text'] = 'Audio/Mp3'
        self.RadioBtt01['font'] = (self.DefaultFont,10,'bold')
        self.RadioBtt01['value'] = 1
        self.RadioBtt01['variable'] = self.CheckVar
        # self.RadioBtt01['foreground'] = 'white'
        self.RadioBtt01['bg'] = self.DefaultBg
        self.RadioBtt01.pack(side=LEFT,**self.DefaultPadding)

        self.BttDowload = Button(self.FifthContanier)
        self.BttDowload['text'] = 'Baixar'
        self.BttDowload['font'] = (self.DefaultFont,10,'bold')
        self.BttDowload['command'] = self.DownloadFunction
        self.BttDowload.pack(**self.DefaultPadding)

        self.BttOpen = Button(self.SixthContanier)
        self.BttOpen['text'] = 'Em Processo..'
        self.BttOpen['font'] = (self.DefaultFont,10,'bold')
        self.BttOpen['command'] = self.OpenFileLocation
        self.BttOpen.pack(**self.DefaultPadding)

    def SelectDir(self):

      file = dlg.askdirectory(initialdir= '/')
      if file == '':
          pass
      else:
          self.BttDir['text'] = file

    def DownloadFunction(self):
            if self.CheckVar.get() == 0:
                link = self.Entry0.get()
                path = self.BttDir['text'] +'/Downloads'
                yt = YouTube(link)
                #Fazer o dowload
                ys = yt.streams.filter(only_audio=True).first().download(path)
                self.BttOpen['text'] = 'Download Completo'

            elif self.CheckVar.get() == 1:
                link = self.Entry0.get()
                path = self.BttDir['text'] + '/Downloads'
                yt = YouTube(link)
                #Fazer o dowload
                ys = yt.streams.filter(only_audio=True).first().download(path)
                #Converter o video(mp4) para mp3
                for file in os.listdir(path):                  #For para percorrer dentro da pasta passada anteriormente
                    if re.search('mp4', file):                 #If verificando se o arquivo e .MP4                    
                        mp4_path = os.path.join(path , file)   #Cria uma variavel para armazenar o arquivo .MP4
                        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3') #Variavel que cria o nome do arquivo e adiciona .MP3 ao final
                        new_file = mp.AudioFileClip(mp4_path)  #Cria o arquivo de áudio (.MP3)
                        new_file.write_audiofile(mp3_path)     #Renomeia o arquivo, setando o nome criado anteriormente
                        os.remove(mp4_path)                    #Remove o arquivo .MP4
                self.BttOpen['text'] = 'Download Completo!'

    def OpenFileLocation(self):
        webbrowser.open(os.path.realpath(self.BttDir['text'] + '/Downloads'))

if __name__ == "__main__":
  root = AppDownload()
  root.mainloop()