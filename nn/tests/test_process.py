from nn import process


def test_add():
    assert process.add(1, 1) == 2
    assert process.add(1, 0) != 0
