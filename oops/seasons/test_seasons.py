from seasons import in_words,age
import pytest

def main():
    test_in_words()
    test_age()
    

def test_age():
    assert age("1999-01-01") == 13507200

def test_in_words():
    assert in_words(13507200) == "Thirteen million, five hundred seven thousand, two hundred minutes"

if __name__ == "__main__":
    main()