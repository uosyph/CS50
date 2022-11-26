import random

def main():
    generate_integer(get_level())


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1,2,3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    score = 0
    for _ in range(10):
        if level == 1:
            fNum = random.randint(0, 9)
            sNum = random.randint(0, 9)
        elif level == 2:
            fNum = random.randint(10, 99)
            sNum = random.randint(10, 99)
        else:
            fNum = random.randint(100, 999)
            sNum = random.randint(100, 999)

        counter = 0
        for _ in range(3):

            try:
                print(fNum, '+', sNum, '= ', end='')
                answer = int(input())
                if answer == fNum + sNum:
                    score += 1
                    break
                else:
                    print('EEE')
                    counter += 1
            except ValueError:
                print('EEE')
                counter += 1
                pass

            if counter == 3:
                print(fNum, '+', sNum, '= ', fNum + sNum)

    print('Score: ', score)


if __name__ == '__main__':
    main()