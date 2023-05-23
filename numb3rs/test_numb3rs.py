import numb3rs

def test_a():
    assert numb3rs.validate("256.0.0.0") == False

def test_b():
    assert numb3rs.validate("0.256.0.0") == False

def test_c():
    assert numb3rs.validate("0.0.256.0") == False

def test_d():
    assert numb3rs.validate("0.0.0.256") == False

def test_5():
    assert numb3rs.validate("0.0.0.0.0") == False

def test_string():
    assert numb3rs.validate("cat") == False