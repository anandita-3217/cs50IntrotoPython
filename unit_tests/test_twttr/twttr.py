def main():
    word = input("Enter words")
    print(shorten(word))


def shorten(word):
    output=""
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    for i in word:
        if i not in vowels:
            output +=i
    return output


if __name__ == "__main__":
    main()