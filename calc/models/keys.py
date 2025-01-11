from enum import Enum

class ButtonType(Enum):
    RESET = 1
    EQUAL = 2
    DIGITS = 3
    OPERATIONS = 4

class Key:
    def __init__(self, value: str, type: ButtonType):
        self.value = value
        self.type = type