from enum import Enum

class ButtonType(Enum):
    RESET = 1
    EQUAL = 2
    DIGITS = 3
    OPERATIONS = 4

class Key:
    def __init__(self, valor: str, tipo: ButtonType):
        self.valor = valor
        self.tipo = tipo