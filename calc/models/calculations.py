"""
Create the necessary objets to solve the tests that will be used when controller is created.
"""
import enum

from calc.models.keys import ButtonType, Key
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
    def __init__(self, num_1: object=None, num_2: object=None, operation: Operations=None):
        self.num_1 = num_1
        self.num_2 = num_2
        self.operation = operation
        self.__is_solved = False

    @property
    def result(self) ->object:
        result = None
        if self.state in (Status.COMPLETED, Status.FINISHED):
            if self.operation == Operations.ADD:
                result = self.num_1 + self.num_2
            elif self.operation == Operations.SUB:
                result = self.num_1 - self.num_2
            elif self.operation == Operations.PROD:
                result = self.num_1 * self.num_2
            elif self.operation == Operations.DIV:
                result = self.num_1 / self.num_2
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
    __description: str = ""

    def add_key(self, key: Key):
        if key.tipo == ButtonType.DIGITS:
            self.__description = ""
            if self.state == Status.EMPTY:
                self.num_1 = Roman_Number(key.valor)
            elif self.state == Status.PARTIAL:
                nuevo_valor = self.num_1.representacion + key.valor
                self.num_1 = Roman_Number(nuevo_valor)
            elif self.state == Status.PENDING:
                self.num_2 = Roman_Number(key.valor)
            elif self.state == Status.COMPLETED:
                nuevo_valor = self.num_2.representacion + key.valor
                self.num_2 = Roman_Number(nuevo_valor)
            elif self.state == Status.FINISHED:
                self.num_1 = None
                self.num_2 = None
                self.operation = None
                self.add_key(key)
        elif key.tipo == ButtonType.OPERATIONS:
            if self.state == Status.PARTIAL:
                self.operation = Operations(key.valor)
            elif self.state == Status.PENDING:
                self.operation = Operations(key.valor)
            elif self.state in (Status.COMPLETED, Status.FINISHED):
                result = self.result
                super().__init__()
                self.num_1 = result
                self.operation = Operations(key.valor)
        elif key.tipo == ButtonType.EQUAL:
            if self.state == Status.COMPLETED:
                self.result
        elif key.tipo == ButtonType.RESET:
            super().__init__()
            self.__description = ""


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
            result = self.result.representacion

        return result

    #Resume
    def get_resume(self) -> str:
        return self.__description

    #Redifining result
    @property
    def result(self):
        res = super().result
        if res is not None:
            self.__description = f"{self.num_1} {self.operation.value} {self.num_2} = {res}"
        return res


