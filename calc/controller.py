import tkinter as tk
from calc.models.calculations import Calculate, Status
from calc.models.roman_number import Roman_Number
from calc.views import ButtonTypes, Calculator

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Roman Calculator")
        self.calc = Calculator(self, self.handle_button_click)
        self.calc.pack()

        self.calculo = Calculate()

    #Cuando se presiona un boton que se hace?    
    def handle_button_click(self, id_btn: str):
        if id_btn in self.calc.keyboard.button_type[ButtonTypes.DIGITS]:
            if self.calculo.state == Status.EMPTY:
                self.calculo.num_1 = Roman_Number(id_btn)
            elif self.calculo.state == Status.PARTIAL:
                new_text = F"{self.calculo.num_1}{id_btn}"#nuevo texto a mostrar más otro valor pulsado
                self.calculo.num_1 = Roman_Number(new_text)
            elif self.calculo.state == Status.PENDING: #Ya se ha pulsado un operador
                pass
        elif id_btn in self.calc.keyboard.button_type[ButtonTypes.OPERATIONS]:#Si vacío ignora si estado parcial se almacena
            pass#completarlo
        self.calc.show(self.calculo.num_1)

    def run(self):
        self.mainloop()

    