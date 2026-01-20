from jar import Jar


def test_init():
    jar = Jar(10)
    assert str(jar) == ""

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(2)
    assert str(jar) == "🍪🍪"

def test_withdraw():
    jar = Jar(10)
    jar.deposit(2)
    jar.withdraw(1)
    assert str(jar) == "🍪"
