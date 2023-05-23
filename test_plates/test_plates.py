import plates

def test_valid():
    assert plates.is_valid("CS50") == True

def test_leading_zero():
    assert plates.is_valid("CS05") == False

def test_numbers():
    assert plates.is_valid("CS50P") == False

def test_symbols():
    assert plates.is_valid("PI3.14") == False

def test_short():
    assert plates.is_valid("P") == False

def test_long():
    assert plates.is_valid("PPPPPPP") == False

def test_start_letters():
    assert plates.is_valid("P1") == False
    assert plates.is_valid("11") == False
