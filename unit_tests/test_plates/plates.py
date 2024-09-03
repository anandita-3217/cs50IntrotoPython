def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
  # vanity plates may contain a maximum of 6 characters 
  # (letters or numbers) and a minimum of 2 characters
  if len(s) < 2 or len(s) > 6:
      return False
  # # All vanity plates must start with at least two letters
  if s[0].isalpha() == False or s[1].isalpha() == False:
      return False
  # No periods, spaces, or punctuation marks are allowed
  for i in s:
      if not i.isalnum():
          return False

  # Numbers cannot be used in the middle of a plate; they must come at the end. 
  # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’
  start = -1
  for i in range(len(s)):
      if s[i].isdigit():
          start = i
          break
  if start != -1:
      # The first number used cannot be a ‘0’
      if s[start] == '0':
          return False
      for i in range (start,len(s)):
          if not s[i].isdigit():
              return False
  return True
      
if __name__ == "__main__":
    main()
