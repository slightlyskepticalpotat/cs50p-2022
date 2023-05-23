import um

def test_basic():
    assert um.count("um") == 1

def test_medium():
    assert um.count("um?") == 1

def test_advanced():
    assert um.count("Um, thanks for the album.") == 1
    assert um.count("Um, thanks, um...") == 2