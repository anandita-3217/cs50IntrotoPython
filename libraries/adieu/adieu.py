import sys

def main():
    name_list = []
    try:
        while True:
            name = input("Name: ").strip().title()
            name_list.append(name)
    except EOFError:
        pass

    
    if name_list:
        if len(name_list) == 1:
            message = f"Adieu, adieu, to {name_list[0]}"
        elif len(name_list) == 2:
            message = f"Adieu, adieu, to {name_list[0]} and {name_list[1]}"
        else:
            message = f"Adieu, adieu, to {', '.join(name_list[:-1])}, and {name_list[-1]}"
        print(message)

if __name__ == "__main__":
    main()
