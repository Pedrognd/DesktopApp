# Antes de executar o codigo. Realizar os pip's:
# pip install pytube
# pip install moviepy

# Importações Necessárias.
from tkinter import *
from tkinter import ttk as c
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

# Definição da class da janela. 
class AppDownload(Tk):
    def __init__(self):
        super().__init__()
        
        # Definições Padrões
        self.title('Download Mp3/Mp4')
        self.geometry('375x312')
        self.resizable(0,0)
        self.DefaultFont = ('Arial',10,'bold')
        self.EntryFont = ('Arial',10)
        s = c.Style()

        self.DefaultPadding = {'padx': 10,
                               'pady': 10}
        
        # Configurando as coluna aparente na janela
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Declarações de Variaveis 
        self.Url = StringVar()
        self.CheckVar = IntVar()

        # Primeiro Texto
        self.FirstText = c.Label(self)
        self.FirstText['text'] = 'Downloads do Youtube'
        self.FirstText['font'] = ('Arial',20,'bold')
        self.FirstText['anchor'] = CENTER
        self.FirstText.grid(column=0,row=0,columnspan=2,pady=5,sticky=N)

        # Scripts para Parte de inserção de link
        self.Urls = c.Label(self)
        self.Urls['text'] = 'Link do Youtube:'
        self.Urls['font'] = self.DefaultFont
        self.Urls.grid(column=0,row=1,sticky=W, **self.DefaultPadding)

        self.UrlsEntry = c.Entry(self)
        self.UrlsEntry['textvariable'] = self.Url
        self.UrlsEntry['font'] = self.EntryFont
        self.UrlsEntry['width'] = 34
        self.UrlsEntry.grid(column=1,row=1,sticky=E, **self.DefaultPadding)
        
        # Scripts para selecionar uma pasta/diretorio
        self.FindDir = c.Button(self)
        self.FindDir['text'] = 'Selecione a pasta de download'
        s.configure('TButton', font=(self.DefaultFont))
        self.FindDir['command'] = self.SelectDir
        self.FindDir.grid(column=0,row=2,columnspan=2,sticky=N, **self.DefaultPadding)

        self.SelectOptions = c.Label(self)
        self.SelectOptions['text'] = 'Selecione uma das opções:'
        self.SelectOptions['font'] = self.DefaultFont
        self.SelectOptions.grid(column=0,row=3,sticky=N,columnspan=2, **self.DefaultPadding)

        # Scripts para escolha entre mp3 e mp4
        self.SelectOptions0 = c.Radiobutton(self)
        self.SelectOptions0['text'] = 'Video/Mp4'
        self.SelectOptions0['variable'] = self.CheckVar
        self.SelectOptions0['value'] = 0
        self.SelectOptions0.grid(column=0,row=4,sticky=E)

        self.SelectOptions1 = c.Radiobutton(self)
        self.SelectOptions1['text'] = 'Audio/Mp3'
        self.SelectOptions1['variable'] = self.CheckVar
        self.SelectOptions1['value'] = 1
        self.SelectOptions1.grid(column=1,row=4,sticky=E,padx=(50))

        # Botão onde chama a função pra fazer o download e conversão do arquivo.
        self.DownloadBtt = c.Button(self)
        self.DownloadBtt['text'] = 'Baixar!'
        s.configure('TButton', font=(self.DefaultFont))
        self.DownloadBtt['command'] = self.DownloadFunction
        self.DownloadBtt.grid(column=0,row=5,columnspan=2,sticky=N, **self.DefaultPadding)

        # Botão onde abre o local do arquivo baixado.
        self.Aleatorio = c.Button(self)
        self.Aleatorio['text'] = 'Em Processo!'
        s.configure('TButton', font=(self.DefaultFont))
        self.Aleatorio['command'] = self.OpenFileLocation
        self.Aleatorio.grid(column=0,row=6,columnspan=2,sticky=N, **self.DefaultPadding)

    # Função que seleciona o diretorio
    def SelectDir(self):

        file = dlg.askdirectory(initialdir= '/')
        if file == '':
            pass
        else:
            self.FindDir['text'] = file

    # Onde "tudo acontece", função onde acontece o downloads e conversões.
    def DownloadFunction(self):
        if self.CheckVar.get() == 0:
            link = self.UrlsEntry.get()
            path = self.FindDir['text'] +'/Downloads'
            yt = YouTube(link)
            #Fazer o dowload
            ys = yt.streams.filter(only_audio=True).first().download(path)
            self.Aleatorio['text'] = 'Download Completo!'

        elif self.CheckVar.get() == 1:
            link = self.UrlsEntry.get()
            path = self.FindDir['text'] + '/Downloads'
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
            self.Aleatorio['text'] = 'Download Completo!'
    
    # Função que abri a pasta do local do arquivo.
    def OpenFileLocation(self):
        webbrowser.open(os.path.realpath(self.FindDir['text'] + '/Downloads'))

# Função onde chama o "app" em si e faz o programa funcionar.
if __name__ == "__main__":
    root = AppDownload()
    root.mainloop()