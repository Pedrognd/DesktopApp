from tkinter import * 

class AppCalculoJuros:
    def __init__(self, master=None):
        self.DefaultFont = ('Arial','10')
        
        self.FirstContainer = Frame(master)
        self.FirstContainer['pady'] = 10
        self.FirstContainer.pack()

        self.SecondContainer = Frame(master)
        self.SecondContainer['padx'] = 20
        self.SecondContainer.pack()

        self.ThirdContainer = Frame(master)
        self.ThirdContainer['padx'] = 20
        self.ThirdContainer.pack()

        self.FourthContainer = Frame(master)
        self.FourthContainer['padx'] = 20
        self.FourthContainer.pack()

        self.FifthContainer = Frame(master)
        self.FifthContainer['padx'] = 20
        self.FifthContainer.pack()

        self.title =Label(self.FirstContainer, text='Calculo de Juros')
        self.title['font'] = ('Arial', '10', 'bold')
        self.title.pack()

        self.ValueLabel = Label(self.SecondContainer, text='Valor Inicial: R$', font=self.DefaultFont)
        self.ValueLabel.pack(side=LEFT)

        self.Value = Entry(self.SecondContainer)
        self.Value['width'] = 30
        self.Value['font'] = self.DefaultFont
        self.Value.pack(side=LEFT)

        self.InterestRatesLabel = Label(self.ThirdContainer, text='Taxa de juros: ', font=self.DefaultFont)
        self.InterestRatesLabel.pack(side=LEFT)

        self.InterestRates = Entry(self.ThirdContainer)
        self.InterestRates['width'] = 30
        self.InterestRates['font']  = self.DefaultFont
        self.InterestRates.pack(side=LEFT)

        self.Calculation = Button(self.FourthContainer)
        self.Calculation['text'] = 'Calcular'
        self.Calculation['font'] = ('Calibri','8')
        self.Calculation['width'] = 12
        self.Calculation['command'] = self.CalculationFunction
        self.Calculation.pack()

        self.message = Label(self.FifthContainer, text='', font=self.DefaultFont)
        self.message.pack()

    def CalculationFunction(self):
        InitialValue = float(self.Value.get())
        InterestRate = float(self.InterestRates.get())

        Equa = InitialValue * 30 * (InterestRate/100) / 30
        Amount= InitialValue + Equa
        
        EquaFormat = f'Juros do mês: R$ {Equa:_.2f}'
        EquaFormat = EquaFormat.replace('.',',').replace('_','.')
        AmountFormat = f'Valor do mês com juros: R$ {Amount:_.2f}'
        AmountFormat = AmountFormat.replace('.',',').replace('_','.')

        self.message['text'] = f'''
                
{EquaFormat}
{AmountFormat}

        '''

root = Tk()
AppCalculoJuros(root)
root.title('Calculo de Juros')
root.mainloop()