import tkinter as tk

BUTTON_WIDTH = 90
BUTTON_HEIGHT = 50

#Buttons
class CalcButton(tk.Frame):
    def __init__(self, parent, text: str, command: callable): #"Cuelga del padre", root.
        super().__init__(parent, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        self.pack_propagate(False)#Que mantenga sus dimensiones aunequ el tamaño del contenedor cambie.
        btn = tk.Button(self, text=text, command=self.__handle_click)
        btn.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.text = text
        self.command = command

    def __handle_click(self): #Utilizando __ antes del nombre de la función le decimos que esta es privada.
        self.command(self.text)

#Keyboard
class keyBoard(tk.Frame):
    def __init__(self, parent, command: callable):
        super().__init__(parent, width=3 * BUTTON_WIDTH, height=5 * BUTTON_HEIGHT)
        self.grid_propagate(False)

        self.buttons = []
        text_buttons = ("Clear", "%", "/",
                         "I", "V", "*", 
                         "X", "L", "-", 
                         "C", "D", "+", 
                         "M", ".", "=")

        ix = 0
        for row in range(5):
            for column in range (3):
                btn = CalcButton(self, text_buttons[ix], command=command)
                btn.grid(column=column, row=row)
                ix +=1

#Display
class Display(tk.Frame):
    #Esta es la caja "contenedora"
    def __init__(self, parent, text: str=""):
        super().__init__(parent, width=BUTTON_WIDTH*3, height=BUTTON_HEIGHT) # es lo mismo que escribir tk.Frame.__init__(self, parent,etc)
        self.pack_propagate(False)
    #Esto es lo que meto dentro de la caja para que sea lo que se ve
        self.lbl_display = tk.Label(self, text=text, fg="white", bg="black", font=("Arial", 36), anchor=tk.E)
        self.lbl_display.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def show(self, text: str):
        self.lbl_display.config(text=text)

#Calculator: "Interfaz"
class Calculator(tk.Frame):
    def __init__(self, parent, command: callable):
        super().__init__(parent)
        self.display = Display(self)
        self.display.pack()
        keyboard = keyBoard(self, command)
        keyboard.pack()

    def show(self, text: str):
        self.display.show(text)