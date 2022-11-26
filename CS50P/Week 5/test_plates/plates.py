def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if  len(s) < 2 or len(s) > 6:
        return False
    elif s[0].isnumeric() == True or s[1].isnumeric() == True:
        return False

    for char in s:
        if char in '''!()-[]{};:'"\,<>./?@#$ %^&*_~''':
            return False

    i = 0
    while i < len(s):
        if s[i].isnumeric() == True:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    for i in range(len(s)):
        if s[i].isnumeric():
            if not s[i:].isnumeric():
                return False

    return True


if __name__ == '__main__':
    main()