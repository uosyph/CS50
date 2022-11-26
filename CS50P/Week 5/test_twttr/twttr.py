def main():
    text = input('Input: ')
    print(shorten(text))


def shorten(text):
    vowels = 'aeiouAEIOUE'
    for char in vowels:
        text = text.replace(char, '')
    return text


if __name__ == '__main__':
    main()