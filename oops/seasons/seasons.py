from datetime import date
import re
import sys
import inflect

def main():
    dob = input("Date of Birth: ")
    if not re.match(r'^[\d]{4}-[\d]{2}-[\d]{2}$',dob):
        sys.exit("Invalid date")
    else:
        age_in_min = age(dob)
        
        print(in_words(age_in_min))


def age(dob):
    yr,mnth,day = map(int,dob.split("-"))
    birth_date = date(yr,mnth,day)
    cur = date.today()
    # cur = date(day=1, month=1,year=2000)
    age_in_days = (cur - birth_date).days
    age_in_min = age_in_days*24*60
    return age_in_min

def in_words(num):
    p = inflect.engine()
    age_in_words = p.number_to_words(num)
    return  age_in_words.replace(" and "," ").capitalize() + " minutes"

if __name__ == "__main__":
    main()