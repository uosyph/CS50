def main():
    fraction = fuel('Fraction: ')
    if fraction <= 1:
        print("E")
    elif fraction >= 99:
        print("F")
    else: print(f"{fraction:.0f}%")

def fuel(prompt):
    while True:
        try:
            x, y = input(prompt).split('/')
            x = int(x)
            y = int(y)
            if x <= y and y != 0:
                return (x/y)*100
        except (ValueError, ZeroDivisionError):
            pass

main()