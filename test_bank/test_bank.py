import bank

def test_h():
    assert bank.value("h") == 20
    assert bank.value("H") == 20

def test_hello():
    assert bank.value("hello") == 0
    assert bank.value("HELLO") == 0
    assert bank.value("hello world") == 0

def test_other():
    assert bank.value("a") == 100
    assert bank.value("A") == 100
    assert bank.value("Aaa aaaaa") == 100