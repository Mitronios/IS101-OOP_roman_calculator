import tkinter as tk
from calc.models.keys import Key, ButtonType
from calc.views import CalcButton, Calculator, Display, keyBoard

def fn_delegada(key: Key):
  calc.show(f"{key.valor}: {key.tipo.name}")

#Root
root = tk.Tk()
root.pack_propagate(True)
#Create
calc = Calculator(root, fn_delegada)
# #Show, place
calc.pack()


#Execute
root.mainloop()