def main():
    fraction = input('Fraction: ')
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)


def convert(fraction):
    while True:
        try:
            numerator, denominator = fraction.split('/')
            numerator = int(numerator)
            denominator = int(denominator)

            f = numerator / denominator

            if f <= 1:
                return int(f * 100)
            else:
                fraction = input('Fraction: ')
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return str(percentage) + '%'


if __name__ == '__main__':
    main()