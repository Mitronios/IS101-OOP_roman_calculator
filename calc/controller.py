import tkinter as tk
from calc.models.calculations import Calculate, RomanCalculo, Status
from calc.models.keys import Key, ButtonType
from calc.models.roman_number import Roman_Number
from calc.views import Calculator

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Roman Calculator")
        self.calc = Calculator(self, self.handle_button_click)
        self.calc.pack()

        self.calculo = RomanCalculo()

    #Cuando se presiona un boton que se hace?    
    def handle_button_click(self, key: Key):
        self.calculo.add_key(key)
        self.calc.show(self.calculo.get_display())

    def run(self):
        self.mainloop()

    