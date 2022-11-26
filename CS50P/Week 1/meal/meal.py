def main():
    answer = convert(input('What time it is? '))

    if answer >= 7 and answer <= 8:
        print('breakfast time')

    if answer >= 12 and answer <= 13:
        print('lunch time')

    if answer >= 18 and answer <= 19:
        print('dinner time')

def convert(time):
    hours, minutes = time.split(':')

    new_minute = float(minutes) / 60

    return float(hours) + new_minute


if __name__ == "__main__":
    main()