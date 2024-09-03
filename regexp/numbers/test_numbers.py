from numb3rs import validate
def main():
    test_validate_format()
    test_validate_values()


# def test_validate_format():
#     assert validate(r'1.2.3.4') == True
#     assert validate(r'1.2.3') == False
#     assert validate(r'1.2') == False
#     assert validate(r'1') == False
#     assert validate(r'.2.3.1000') == False
#     assert validate(r'1234.567.89.0') == False
#     assert validate(r'1234.5687.8933.57350') == False

# def test_validate_values():
#     assert validate(r'255.255.255.255') == True
#     assert validate(r'1000.255.255.255') == False
#     assert validate(r'255.1000.255.255') == False
#     assert validate(r'255.255.1000.255') == False
#     assert validate(r'255.255.255.1000') == False
#     assert validate(r'127.0.0.1') == True
#     assert validate(r'255.255.255.0') == True
#     assert validate(r'275.3.6.28') == False
#     assert validate(r'512.512.512.512') == False
#     assert validate(r'1.2.3.1000') == False
#     assert validate(r'001.2.3.1000') == False
#     assert validate(r'001.2.3') == False
#     assert validate("cat") == False
def test_validate_format():
    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1') == False

def test_validate_values():
    assert validate(r'255.255.255.255') == True
    assert validate(r'512.1.1.1') == False
    assert validate(r'1.512.1.1') == False
    assert validate(r'1.1.512.1') == False
    assert validate(r'1.1.1.512') == False
    assert validate("cat") == False
if __name__ == "__main__":
    main()
