# Antes de executar o codigo. Realizar os pip's:
# pip install pytube
# pip install moviepy
# from tkinter import ttk as c

# Importações Necessárias.
from tkinter import *
from tkinter import messagebox
from datetime import date, timedelta,datetime
import pandas as pd
import webbrowser, os
import http.client

# Correção de erro, recorrente a versão do http.
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

class AppDownload(Tk):
    def __init__(self):
        super().__init__()

        # Definindo padrões
        self.geometry('450x340')
        self.title('Calculo de Juros')
        self.configure(bg='#3F3C52')
        self.DefaultBg = '#3F3C52'

        self.DefaultPadding = {'padx': 10,
                               'pady': 10}
        
        self.DefaultFont = 'Arial'

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

        # Inicio de Customização
        self.FirstLabel = Label(self.FirstContainer)
        self.FirstLabel['text'] = 'Calculo de juros'
        self.FirstLabel['font'] = (self.DefaultFont, 20, 'bold')
        self.FirstLabel['foreground'] = 'white'
        self.FirstLabel['bg'] = self.DefaultBg
        self.FirstLabel.pack(**self.DefaultPadding)

        self.ValueLabel = Label(self.SecondContainer)
        self.ValueLabel['text'] = 'Valor incial:      R$'
        self.ValueLabel['font'] = (self.DefaultFont, 10, 'bold')
        self.ValueLabel['foreground'] = 'white'
        self.ValueLabel['bg'] = self.DefaultBg
        self.ValueLabel.pack(side=LEFT,**self.DefaultPadding)

        self.ValueEntry = Entry(self.SecondContainer)
        self.ValueEntry['font'] = (self.DefaultFont, 10, 'bold')
        self.ValueEntry.pack(side=LEFT,**self.DefaultPadding)

        self.RateLabel = Label(self.ThirdContainer)
        self.RateLabel['text'] = 'Taxa de Juros:      '
        self.RateLabel['font'] = (self.DefaultFont, 10, 'bold')
        self.RateLabel['foreground'] = 'white'
        self.RateLabel['bg'] = self.DefaultBg
        self.RateLabel.pack(side=LEFT,**self.DefaultPadding)

        self.RateEntry = Entry(self.ThirdContainer)
        self.RateEntry['font'] = (self.DefaultFont, 10, 'bold')
        self.RateEntry.pack(side=LEFT,**self.DefaultPadding)

        self.MonthsLabelstart = Label(self.FourthContainer)
        self.MonthsLabelstart['text'] = 'Data de Inicio:'
        self.MonthsLabelstart['font'] = (self.DefaultFont, 10, 'bold')
        self.MonthsLabelstart['foreground'] = 'white'
        self.MonthsLabelstart['bg'] = self.DefaultBg
        self.MonthsLabelstart.pack(side=LEFT,**self.DefaultPadding)

        self.MonthsEntrystart = Entry(self.FourthContainer)
        self.MonthsEntrystart['font'] = (self.DefaultFont, 10, 'bold')
        self.MonthsEntrystart['width'] = 10
        self.MonthsEntrystart.pack(side=LEFT,**self.DefaultPadding)

        self.MonthsLabelend = Label(self.FourthContainer)
        self.MonthsLabelend['text'] = 'Data Final:'
        self.MonthsLabelend['font'] = (self.DefaultFont, 10, 'bold')
        self.MonthsLabelend['foreground'] = 'white'
        self.MonthsLabelend['bg'] = self.DefaultBg
        self.MonthsLabelend.pack(side=LEFT,**self.DefaultPadding)

        self.MonthsEntryend = Entry(self.FourthContainer)
        self.MonthsEntryend['font'] = (self.DefaultFont, 10, 'bold')
        self.MonthsEntryend['width'] = 10
        self.MonthsEntryend.pack(side=LEFT,pady=10)

        self.ObsLabel = Label(self.FifthContainer)
        self.ObsLabel['text'] = 'Exemplo: 01.01.1999'
        self.ObsLabel['font'] = (self.DefaultFont, 10, 'bold')
        self.ObsLabel['foreground'] = 'white'
        self.ObsLabel['bg'] = self.DefaultBg
        self.ObsLabel.pack(**self.DefaultPadding)

        self.BttCalculate = Button(self.FifthContainer)
        self.BttCalculate['text'] = 'Calcular'
        self.BttCalculate['font'] = (self.DefaultFont, 10, 'bold')
        self.BttCalculate['command'] = self.Calculate
        self.BttCalculate.pack(**self.DefaultPadding)

    # Função para fazer o calculo de juros.
    def Calculate(self):
      try:
        Value = int(self.ValueEntry.get())
        Rate = int(self.RateEntry.get())
        DataInicio = self.MonthsEntrystart.get()
        DataFinal = self.MonthsEntryend.get()
      except ValueError:
         messagebox.showerror('Alerta','Preencha todos os campos!')

      # Formatação de data para transformar em date() 
      dt1dia,dt1mes,dt1ano = int(DataInicio[0:2]), int(DataInicio[3:5]), int(DataInicio[6:10])      
      dt2dia,dt2mes,dt2ano = int(DataFinal[0:2]), int(DataFinal[3:5]), int(DataFinal[6:10])

      # Passando date-> string para date->date() 
      Data1f = date(dt1ano,dt1mes,dt1dia)
      Data2f = date(dt2ano,dt2mes,dt2dia) 
      
      # Subtração das datas para saber a diferença entre elas 
      Delta = Data2f - Data1f
      DataTra = Data1f
      DataTra = DataTra.month -1 # Pegando apenas os meses

      ListaDatas = []

      # Estrutura de repetição para adicionar as datas em uma lista 
      for i in range(Delta.days + 1):
          DataAtu = Data1f +timedelta(days=i)
          if DataTra != DataAtu.month:
              DataTra += 1
              if DataTra > 12:
                  DataTra = 1
              ListaDatas.append(DataAtu)
      ListaDatasStr = [datetime.strftime(dt,format='%d/%m/%Y') for dt in ListaDatas]

      # Criação de um dicionario e estrutura de repetição para calculo de juros e criação de arquivo .xlsx
      dic ={}   
      for i in ListaDatasStr:
          DataIns = date(int(i[6:10]),int(i[3:5]),int(i[:2]))

          Fees = Value * 30 * (Rate/100) / 30
          ValueIni = Value
          Value = Fees + Value

          Ins = {
          'Data': i,
          'Taxa': f'{Rate}%',
          'Valor Incial': f'{ValueIni:.2f}',
          'Juros do Mês': f'{Fees:.2f}',
          'Valor Total' : f'{Value:.2f}',
          }

          dic[i] = Ins
          Plan = pd.DataFrame.from_dict(dic,orient='index')
          Plan.to_excel(f'.\\DesktopApp\\Calculo de Juros\\Juros.xlsx',index=False)

      messagebox.showinfo('Aviso','Arquivo Gerado com Sucesso')
      webbrowser.open(os.path.realpath('.\\DesktopApp\\Calculo de Juros'))

# Loop para inicializção da janela
if __name__ == "__main__":
  root = AppDownload()
  root.mainloop()