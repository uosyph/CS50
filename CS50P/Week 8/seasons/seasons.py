from sys import exit
from re import search
from datetime import date
import inflect

inflect = inflect.engine()

def main():
    try:
        year, month, day = get_dob(input('Date of Birth: '))
        alive = (date.today() - date(int(year), int(month), int(day))).days * 24 * 60
        mins = inflect.number_to_words(alive, andword='')
        print(mins.capitalize() + ' minutes')
    except:
        exit('Invalid date')


def get_dob(dob):
    if search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', dob):
        year, month, day = dob.split('-')
        return year, month, day


if __name__ == '__main__':
    main()