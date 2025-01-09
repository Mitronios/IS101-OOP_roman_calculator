"""
Create the necessary objets to solve the tests, check init and roman numbers to take the proper functions created.
"""
import enum

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
        if self.num_1 and self.num_2 != None:
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



