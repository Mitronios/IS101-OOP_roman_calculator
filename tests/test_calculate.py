def test_create_calc():
    
    calc = calculate(1,2, Operation.ADD)

    assert calc.op1 == 1
    assert calc.op2 == 2
    assert calc,operation == Operation.ADD
    assert calc.result == 3