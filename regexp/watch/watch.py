import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
   pattern_in = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"' 
   match = re.search(pattern_in,s)
   if match:
       pattern_out = match.group(1)
       return f"https://youtu.be/{pattern_out}"
   return None
#Cant believe ive been rickrolled in 2024!
#Well played

if __name__ == "__main__":
    main()
