from bank import value


def test_value():
    assert value("hello")==0
    assert value("howdy")==20
    assert value("supp")==100
    assert value("Hi")==20
    
