from plates import is_valid
def main():
    test_length()
    test_firstletters()
    test_punctation()
    test_nums_middle()
    test_zero_first()

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFGH") == False
    assert is_valid("A") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False

def test_firstletters():
    assert is_valid("CS50") == True
    assert is_valid("AA") == True
    assert is_valid("50CS") == False
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("2345") == False

def test_punctation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3 14") == False
    assert is_valid("PI3]14") == False

def test_nums_middle():
    assert is_valid("AAA222") == True
    assert is_valid("CS50P") == False
    assert is_valid("AAA22A") == False

def test_zero_first():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

if __name__ == "__main__":
    main()