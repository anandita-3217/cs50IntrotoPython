from fuel import gauge,convert

import pytest
def main():
    test_convert_invalid()
    test_convert()
    test_guage()


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("99/100") == 99
    assert convert("100/100") == 100

def test_convert_invalid():

    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("three/four")

def test_guage():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(60) == "60%"

    


if __name__ == "__main__":
    main()
