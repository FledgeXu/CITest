from testpackage.number import square


def test_square():
    assert square(2) == 4
    assert square(1) == 3

def test_add():
    assert add(100) == 1
