import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex = r"^(" \
              r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
              r"){3}" \
              r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"

    if re.match(regex,ip):
        return True
    return False
    # if re.search("^[0-9]+\.^[0-9]+\.^[0-9]+\.^[0-9]+$",ip):
    #     list_of_numbers = ip.split(".")
    #     for num in list_of_numbers:
    #         if int(num) <0 or int(num) >255:
    #             return False
    #     return True
    # else:
    #     return False

if __name__ == "__main__":
    main()