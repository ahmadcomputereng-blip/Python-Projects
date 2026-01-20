from bank import value

def test_pay_0():
    assert value("hello") == 0
    assert value("Hello") == 0
def test_pay_20():
    assert value("Hi") == 20
    assert value("how are you") == 20
def test_pay_100():
    assert value("whats up") == 100
