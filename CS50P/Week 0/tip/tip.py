def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_clean = d.replace('$', '')
    return float(d_clean)

def percent_to_float(p):
    p_clean = p.replace('%', '')
    return float(p_clean) / 100

main()
