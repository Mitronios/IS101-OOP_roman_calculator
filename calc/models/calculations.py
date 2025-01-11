"""
Create the necessary objets to solve the tests that will be used when controller is created.
"""
import enum

from calc.models.keys import Key
from calc.models.roman_number import Roman_Number

class Status(enum.Enum):
    EMPTY = enum.auto()
    PARTIAL = enum.auto()
    PENDING = enum.auto()
    COMPLETED = enum.auto()
    FINISHED = enum.auto()

class Operations(enum.Enum):
    ADD = "+"
    SUB = "-"
    DIV = "/"
    PROD = "*"
    MOD = "%"

class Calculate:
    def __init__(self, num_1: object=None, num_2: object=None, operation:Operations=None):
        self.num_1 = num_1
        self.num_2 = num_2
        self.operation = operation
        self.__is_solved = False

    @property
    def result(self) ->object:
        result = None
        if self.state == Status.COMPLETED:
            if self.operation == Operations.ADD:
                result = self.num_1 + self.num_2
            elif self.operation == Operations.SUB:
                result = self.num_1 - self.num_2
            elif self.operation == Operations.DIV:
                result = self.num_1 / self.num_2
            elif self.operation == Operations.PROD:
                result = self.num_1 * self.num_2
            elif self.operation == Operations.MOD:
                result = self.num_1 % self.num_2
            self.__is_solved = True

        return result
        
    @property
    def state(self):
        status = Status.FINISHED
        if self.num_1 is None:
            status = Status.EMPTY
        elif self.operation is None:
            status = Status.PARTIAL
        elif self.num_2 is None:
            status = Status.PENDING
        elif not self.__is_solved:
            status = Status.COMPLETED
       
        return status 
    
    class RomanCalculo(Calculate):
        def add_key(self, key: Key):
            if Key.type == ButtonType.DIGITS:
                if self.state == Status.Empty:
                    self.num_1 = Roman_Number(key.value)
                elif self.state == Status.PARTIAL:
                    new_value = self.num_1.representacion + key.value
                    self.num_1 = Roman_Number(new_value)
                elif self.state == Status.PENDING:
                    self.num_2 = Roman_Number(key.value)
                elif self.state == Status.COMPLETED:
                    new_value = self.num_2.representacion + key.value
                    self.num_2 = Roman_Number(new_value)
                elif self.state == Status.FINISHED:
                    self.num_1 = None
                    self.num_2 = None
                    self.operation = None
                    self.add_key(Key)

        #Display
        def get_display(self) -> str:
            result = ""
            if self.state == Status.EMPTY:
                result = ""
            elif self.state == Status.PARTIAL:
                result = self.num_1.representacion
            elif self.state == Status.PENDING:
                result = self.num_1.representacion
            elif self.state == Status.COMPLETED:
                result = self.num_2.representacion
            elif self.state == Status.FINISHED:
                result = self.result.representación

            return result





