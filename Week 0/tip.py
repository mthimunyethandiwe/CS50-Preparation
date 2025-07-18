
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    amount = d.replace("$", "")
    return float(amount) # converting the string to float


def percent_to_float(p):
    percentage = p.replace("%", "")
    return float(percentage) / 100 # converting string to float and dividing by 100 to get the decimal


main() #main function running the program