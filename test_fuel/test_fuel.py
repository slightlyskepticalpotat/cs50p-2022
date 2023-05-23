import pytest, fuel

def test_convert():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/3") == 33
    assert fuel.convert("2/3") == 67

def test_gauge():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(50) == "50%"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("100/0")

def test_value_error():
    with pytest.raises(ValueError):
        fuel.convert("cats/dogs")