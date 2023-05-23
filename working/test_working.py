import pytest, working

def test_long():
    assert working.convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_short():
    assert working.convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_error():
    with pytest.raises(ValueError):
        working.convert("09:00 AM - 17:00 PM")

def test_error2():
    with pytest.raises(ValueError):
        working.convert("9:60 AM to 5:60 PM")
