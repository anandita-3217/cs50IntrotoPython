from twttr import shorten

def test_shorten():
    assert shorten("") == ""
    assert shorten("Twitter") == "Twttr"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("PYTHON") == "PYTHN"
    assert shorten("12345") == "12345"
