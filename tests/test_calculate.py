from calc.models.calculations import Calculate, Operations, Status


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
    assert calc.num_1 == None
    assert calc.num_2 == None
    assert calc.operation == None
    assert calc.result== None
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