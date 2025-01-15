from calc.models.calculations import Calculate, Operations, RomanCalculo, Status
from calc.models.keys import ButtonType, Key
from calc.models.roman_number import Roman_Number


def test_create_calc():
    #Addition
    calc = Calculate(1,2, Operations.ADD)

    assert calc.num_1 == 1
    assert calc.num_2 == 2
    assert calc.operation == Operations.ADD
    assert calc.result == 3

    #Substraction
    calc = Calculate(1,2, Operations.SUB)

    assert calc.num_1 == 1
    assert calc.num_2 == 2
    assert calc.operation == Operations.SUB
    assert calc.result == -1

def test_create_incomplete_calcs():
    calc = Calculate()
    assert calc.num_1 is None
    assert calc.num_2 is None
    assert calc.operation is None
    assert calc.result is None
    #Test Status
    assert calc.state == Status.EMPTY#Enum

#num_1 exist
def test_create_calc_num_1():
    calc = Calculate(1)
    assert calc.num_1 == 1
    assert calc.num_2 is None
    assert calc.operation is None
    assert calc.result is None
    
    assert calc.state == Status.PARTIAL

#operator exist
def test_create_calc_operation():
    calc = Calculate(1, operation=Operations.ADD)
    assert calc.num_1 == 1
    assert calc.num_2 is None
    assert calc.operation is Operations.ADD
    assert calc.result is None
    
    assert calc.state == Status.PENDING

#num_1. op and num_2 exists
def test_create_calc_all():
    calc = Calculate(1, 2, Operations.SUB)
    assert calc.num_1 == 1
    assert calc.num_2 == 2
    assert calc.operation is Operations.SUB
    calc.state == Status.COMPLETED
    assert calc.result == -1
    
    #When user press equal 
    assert calc.state == Status.FINISHED

#Roman Calculations
def test_create_roman_calc():
    rc = RomanCalculo()
    assert rc.num_1 is None
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.state == Status.EMPTY

    assert rc.get_display() == ""

def test_add_digits_to_rc_empty():
    rc = RomanCalculo()
    rc.add_key(Key("I", ButtonType.DIGITS))

    assert rc.num_1 == Roman_Number(1)
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.state == Status.PARTIAL

    assert rc.get_display() == "I"
    assert rc.get_resume() == ""

def test_add_digits_to_rc_partial():
    rc = RomanCalculo(Roman_Number(1))

    rc.add_key(Key("V", ButtonType.DIGITS))
    assert rc.num_1 == Roman_Number(4)
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.state == Status.PARTIAL
    assert rc.get_display() == "IV"
    assert rc.get_resume() == ""

def test_add_digits_to_rc_pending():
    rc = RomanCalculo(Roman_Number(1), operation=Operations.ADD)

    rc.add_key(Key("V", ButtonType.DIGITS))
    assert rc.num_1 == Roman_Number(1)
    assert rc.operation == Operations.ADD
    assert rc.num_2 == Roman_Number(5)
    assert rc.state == Status.COMPLETED

    assert rc.get_display() == "V"
    assert rc.get_resume() == ""

def test_add_digits_to_rc_completed():
    rc = RomanCalculo(Roman_Number(1), Roman_Number(5), Operations.ADD)
    rc.add_key(Key("I", ButtonType.DIGITS))

    assert rc.num_1 == Roman_Number(1)
    assert rc.operation == Operations.ADD
    assert rc.num_2 == Roman_Number(6)
    assert rc.state == Status.COMPLETED

    assert rc.get_display() == "VI"
    assert rc.get_resume() == ""

def test_add_digits_to_rc_finished():
    rc = RomanCalculo(Roman_Number(1), Roman_Number(6), Operations.ADD)
    rc.result
    assert rc.get_resume() == "I + VI = VII"

    rc.add_key(Key("I", ButtonType.DIGITS))

    assert rc.num_1 == Roman_Number(1)
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.state == Status.PARTIAL

    assert rc.get_display() == "I"
    assert rc.get_resume() == ""

#Operations tests
def test_add_operations_to_rc_empty():
    rc = RomanCalculo()
    rc.add_key(Key("+", ButtonType.OPERATIONS))

    assert rc.num_1 is None
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.state == Status.EMPTY

    assert rc.get_display() == ""
    assert rc.get_resume() == ""

def test_add_operations_to_rc_partial():
    rc = RomanCalculo(Roman_Number(1))
    rc.add_key(Key("+", ButtonType.OPERATIONS))

    assert rc.num_1 == Roman_Number(1)
    assert rc.operation == Operations.ADD
    assert rc.num_2 is None
    assert rc.state == Status.PENDING

    assert rc.get_display() == "I"
    assert rc.get_resume() == ""

def test_add_operations_to_rc_pending():
    rc = RomanCalculo(Roman_Number(1), operation=Operations.SUB)
    assert rc.num_1 == Roman_Number(1)
    assert rc.operation == Operations.SUB

    rc.add_key(Key("+", ButtonType.OPERATIONS))

    assert rc.num_1 == Roman_Number(1)
    assert rc.operation == Operations.ADD
    assert rc.num_2 is None
    assert rc.state == Status.PENDING

    assert rc.get_display() == "I"
    assert rc.get_resume() == ""

def test_add_operations_to_rc_completo():
    rc = RomanCalculo(Roman_Number(1), Roman_Number(2), Operations.PROD)
    rc.add_key(Key("+", ButtonType.OPERATIONS))

    assert rc.num_1 == Roman_Number(2)
    assert rc.operation == Operations.ADD
    assert rc.num_2 is None
    assert rc.state == Status.PENDING

    assert rc.get_display() == "II"
    assert rc.get_resume() == "I * II = II"

def test_add_operations_to_rc_finished():
    rc = RomanCalculo(Roman_Number(1), Roman_Number(2), Operations.PROD)
    rc.result
    rc.add_key(Key("+", ButtonType.OPERATIONS))

    assert rc.num_1 == Roman_Number(2)
    assert rc.operation == Operations.ADD
    assert rc.num_2 is None
    assert rc.state == Status.PENDING

    assert rc.get_display() == "II"
    assert rc.get_resume() == "I * II = II"

def test_add_equal_to_rc():
    rc = RomanCalculo()
    rc.add_key(Key("=", ButtonType.EQUAL))
    #Empty state
    assert rc.num_1 is None
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.state == Status.EMPTY

    assert rc.get_display() == ""
    assert rc.get_resume() == ""

    #Partial State
    rc.num_1 = Roman_Number(1)
    rc.add_key(Key("=", ButtonType.EQUAL))

    assert rc.num_1 == Roman_Number(1)
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.state == Status.PARTIAL

    assert rc.get_display() == "I"
    assert rc.get_resume() == ""

    #Pending state
    rc.operation = Operations.ADD
    rc.add_key(Key("=", ButtonType.EQUAL))

    assert rc.num_1 == Roman_Number(1)
    assert rc.operation == Operations.ADD
    assert rc.num_2 is None
    assert rc.state == Status.PENDING

    assert rc.get_display() == "I"
    assert rc.get_resume() == ""

    #Finished state
    rc.num_2 = Roman_Number(3)
    rc.add_key(Key("=", ButtonType.EQUAL))

    assert rc.num_1 == Roman_Number(1)
    assert rc.operation == Operations.ADD
    assert rc.num_2 == Roman_Number(3)
    assert rc.state == Status.FINISHED
    assert rc.result == Roman_Number(4)

    assert rc.get_display() == "IV"
    assert rc.get_resume() == "I + III = IV"

    #After getting result 
    rc.add_key(Key("=", ButtonType.EQUAL))

    assert rc.num_1 == Roman_Number(1)
    assert rc.operation == Operations.ADD
    assert rc.num_2 == Roman_Number(3)
    assert rc.state == Status.FINISHED
    assert rc.result == Roman_Number(4)

    assert rc.get_display() == "IV"
    assert rc.get_resume() == "I + III = IV"


#Reset
def test_add_key_reset():
    rc = RomanCalculo(Roman_Number(1), Roman_Number(9), Operations.PROD)
    rc.add_key(Key("clear", ButtonType.RESET))
    
    assert rc.num_1 is None
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.state == Status.EMPTY

    assert rc.get_display() == ""
    assert rc.get_resume() == ""