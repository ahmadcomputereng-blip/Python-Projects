from twttr import shorten
def test_upper():
    assert shorten("TWITTER") == "TWTTR"
def test_lower():
    assert shorten("twitter") == "twttr"
def test_notletter():
    assert shorten("53.4") == "53.4"
