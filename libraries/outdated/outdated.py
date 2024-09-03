months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    while True:
        date_input = input("Date: ")

        # Try handling MM/DD/YYYY format
        try:
            if "/" in date_input:
                month, day, year = date_input.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            else:
                month_str, day_year = date_input.split(" ", 1)
                day, year = day_year.split(", ")
                month = months.index(month_str) + 1
                day = int(day)
                year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
        except ValueError:
            pass

if __name__ == "__main__":
    main()
