import validators

def main():
        print(validation(input('What\'s your email address? ')))


def validation(email):
    return 'Valid' if validators.email(email) else 'Invalid'


if __name__ == '__main__':
    main()