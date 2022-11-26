import sys

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1].endswith('.py') == False:
        sys.exit('Not a Python file')
    else:
        print(count_lines(sys.argv[1]))


def count_lines(path):
    lines = 0
    try:
        with open(path) as file:
            for line in file:
                if line.lstrip().startswith('#') or line.startswith('\n') or line.isspace():
                    pass
                else:
                    lines += 1
    except FileNotFoundError:
        sys.exit('File does not exist')

    return lines


if __name__ == '__main__':
    main()