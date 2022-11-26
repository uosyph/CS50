import random

while True:
    try:
        level = int(input('Level: '))
        if level > 0:
            break
    except ValueError:
        pass

rand_num = random.randint(1,level)

while True:
    try:
        guess = int(input('Guess: '))
        if guess > 0:
            if guess == rand_num:
                print('Just right!')
                break
            elif guess < rand_num:
                print('Too small!')
            else:
                print('Too large!')
    except ValueError:
        pass