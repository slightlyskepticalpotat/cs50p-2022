import twttr

def test_upper():
    assert twttr.shorten("AB") == "B"

def test_lower():
    assert twttr.shorten("ab") == "b"

def test_num():
    assert twttr.shorten("1") == "1"

def test_punc():
    assert twttr.shorten(",") == ","