import sys
import os
import csv

def read_write(input_filename, output_filename):
    """Reads input CSV, processes it, and writes output CSV."""
    rows = []
    
    
    with open(input_filename, 'r') as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            last, first = row['name'].split(", ")
            rows.append({"first": first, "last": last, "house": row['house']})
    
    
    with open(output_filename, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(rows)


def main():
    if len(sys.argv) !=3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")
    initial_file = sys.argv[1]
    final_file = sys.argv[2]
    if not os.path.isfile(initial_file):
        sys.exit(f"Could not read {initial_file}")
    
    read_write(initial_file,final_file)
if __name__ == "__main__":
    main()