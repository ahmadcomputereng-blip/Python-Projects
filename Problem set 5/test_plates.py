from plates import is_valid

def test_all_sixletters():
    assert is_valid("HELLOY") == True
def test_more_than_six():
    assert is_valid("HELLOMYF") == False
def test_valid_numbers():
    assert is_valid("CS5050") == True
    assert is_valid("CSAD50") == True
def test_notvalid_numbers():
    assert is_valid("421100") == False
    assert is_valid("CS50P") == False
def test_zero_start():
    assert is_valid("CS05") == False
def test_non_alphanumeric():
    assert is_valid("CS.50") == False
