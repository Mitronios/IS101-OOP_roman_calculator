import tkinter as tk
from calc.models.calculations import Calculate, Status
from calc.models.keys import Key, ButtonType
from calc.models.roman_number import Roman_Number
from calc.views import Calculator

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Roman Calculator")
        self.calc = Calculator(self, self.handle_button_click)
        self.calc.pack()

        self.calculo = Calculate()

    #Cuando se presiona un boton que se hace?    
    def handle_button_click(self, key: Key):
        if key in self.calc.keyboard.button_type[ButtonTypes.DIGITS]:
            if self.calculo.state == Status.EMPTY:
                self.calculo.num_1 = Roman_Number(key)
            elif self.calculo.state == Status.PARTIAL:
                new_text = F"{self.calculo.num_1}{key}"#nuevo texto a mostrar más otro valor pulsado
                self.calculo.num_1 = Roman_Number(new_text)
            elif self.calculo.state == Status.PENDING: #Ya se ha pulsado un operador
                pass
        elif key in self.calc.keyboard.button_type[ButtonTypes.OPERATIONS]:#Si vacío ignora si estado parcial se almacena
            pass#completarlo
        self.calc.show(self.calculo.num_1)

    def run(self):
        self.mainloop()

    