from nn import process


def test_add():
    assert process.add(1, 10) == 11
    assert process.add(0, 1) == 0
