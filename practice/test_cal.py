from calculator import square
def main():
    test_square()


def test_square():
    # if square(2) != 4:
    #     print("Error! 2^2 was not 4")
    # if square(3) != 9:
    #     print("Error! 3^2 was not 9")
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0



    # try:
    #     assert square(2) == 4
    # except AssertionError:
    #     print("2^2 is not 4")
    # try:
    #     assert square(3) == 9
    # except AssertionError:
    #     print("3^2 is not 9")
    # try:
    #     assert square(-2) == 4
    # except AssertionError:
    #     print("-2^2 is not 4")
    # try:
    #     assert square(-3) == 9
    # except AssertionError:
    #     print("-3^2 is not 4")
    # try:
    #     assert square(0) == 0
    # except AssertionError:
    #     print("0^2 is not 0")

if __name__ == "__main__":
    main()
