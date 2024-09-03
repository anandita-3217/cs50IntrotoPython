import sys
import os
import csv
from tabulate import tabulate
def make_table(file_name):
    with open(file_name,'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data =[row for row in reader]
        print(tabulate(data,headers,tablefmt="grid"))
def main():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")
    file = sys.argv[1]
    if not os.path.isfile(file):
        sys.exit("File does not exist")
    if not file.endswith(".csv"):
        sys.exit("Not a CSV file")
    make_table(file)
if __name__ == "__main__":
    main()