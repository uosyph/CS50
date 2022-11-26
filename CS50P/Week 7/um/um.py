import re

def main():
    while True:
        print(count(input('Text: ')))


def count(s):
    return len(re.findall(r'\b\W*um\b\W*', s, re.MULTILINE | re.IGNORECASE))


if __name__ == '__main__':
    main()