import os
import sys
def lines_in_file(filename):
    count = 0
    with open(filename,'r') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line and not stripped_line.startswith("#"):
                count += 1
    return count
def main():
    # print("hehe")
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments" if len(sys.argv)< 2 else "Too many command-line arguments")
    file = sys.argv[1]
    if not file.endswith(".py"):
        sys.exit("Not a Python file")
    if not os.path.isfile(file):
        sys.exit("File does not exist")
    lines_of_code = lines_in_file(file)
    print(lines_of_code)

if __name__ == "__main__":
    main()