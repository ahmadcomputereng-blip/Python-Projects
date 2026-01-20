import fuel
import pytest
def test_convert():
    assert fuel.convert("4/4") == 100
    assert fuel.convert("3/4") == 75
def test_errors():
    with pytest.raises(ValueError):
        fuel.convert("100/4")
    with pytest.raises(ValueError):
        fuel.convert("-5/4")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("0/0")
def test_gauge():
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(50) == "50%"
