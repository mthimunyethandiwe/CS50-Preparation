def convert(time):
    time = time.strip().lower()
    if "a.m." in time:
        time = time.replace(" a.m.", "")
    elif "p.m." in time:
        time = time.replace(" p.m.", "")
        hours, minutes = time.split(":")
        hours = int(hours)
        if hours != 12:
            hours += 12
        minutes = int(minutes)
        return hours + minutes / 60

    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60

def main():
    time = input("What time is it? ")
    converted_time = convert(time)

    if 7 <= converted_time <= 8:
        print("Breakfast time")
    elif 12 <= converted_time <= 13:
        print("Lunch time")
    elif 18 <= converted_time <= 19:
        print("Dinner time")

if __name__ == "__main__":
    main()



