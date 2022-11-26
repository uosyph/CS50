import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if isCorrectFormat := re.search(r'^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$', s):
        pieces = isCorrectFormat.groups()
        if int(pieces[1]) > 12 or int(pieces[5]) > 12:
            raise ValueError
        first_time = format(pieces[1], pieces[2], pieces[3])
        second_time = format(pieces[5], pieces[6], pieces[7])
        return first_time + ' to ' + second_time
    else:
        raise ValueError


def format(hour, min, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if min == None:
        new_min = ':00'
        new_time = f'{new_hour:02}' + new_min
    else:
        new_time = f'{new_hour:02}' + ':' + min
    return new_time


if __name__ == "__main__":
    main()