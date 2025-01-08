import tkinter as tk
from calc.views import CalcButton, Calculator, Display, keyBoard

def fn_delegada(btn_clickado):
  calc.show(btn_clickado)

#Root
root = tk.Tk()
root.pack_propagate(True)
#Create
calc = Calculator(root, fn_delegada)
#Show, place
calc.pack()


#Execute
root.mainloop()