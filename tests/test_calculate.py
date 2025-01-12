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

def test_add_digits_to_rc_partial():
    rc = RomanCalculo(Roman_Number(1))

    rc.add_key(Key("V", ButtonType.DIGITS))
    assert rc.num_1 == Roman_Number(4)
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.state == Status.PARTIAL
    assert rc.get_display() == "IV"

def test_add_digits_to_rc_pending():
    rc = RomanCalculo(Roman_Number(1), operation=Operations.ADD)

    rc.add_key(Key("V", ButtonType.DIGITS))
    assert rc.num_1 == Roman_Number(1)
    assert rc.operation == Operations.ADD
    assert rc.num_2 == Roman_Number(5)
    assert rc.state == Status.COMPLETED

    assert rc.get_display() == "V"

def test_add_digits_to_rc_completed():
    rc = RomanCalculo(Roman_Number(1), Roman_Number(5), Operations.ADD)
    rc.add_key(Key("I", ButtonType.DIGITS))

    assert rc.num_1 == Roman_Number(1)
    assert rc.operation == Operations.ADD
    assert rc.num_2 == Roman_Number(6)
    assert rc.state == Status.COMPLETED

    assert rc.get_display() == "VI"

def test_add_digits_to_rc_finished():
    rc = RomanCalculo(Roman_Number(1), Roman_Number(6), Operations.ADD)
    rc.result

    rc.add_key(Key("I", ButtonType.DIGITS))

    assert rc.num_1 == Roman_Number(1)
    assert rc.operation is None
    assert rc.num_2 is None
    assert rc.state == Status.PARTIAL

    assert rc.get_display() == "I"
