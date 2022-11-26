def main():
    text = input('Gretting: ').lower().strip()
    print(value(text))


def value(text):
    if 'hello' in text:
        return '$0'
    elif 'h' == text[0]:
        return '$20'
    else:
        return '$100'


if __name__ == '__main__':
    main()