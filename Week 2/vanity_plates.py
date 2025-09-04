def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # the length
    if len(s) < 2 or len(s) > 6:
        return False

    # Checking if the first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # this is for only letters and numbers
    if not s.isalnum():
        return False

    # If there are numbers, they must be at the end and not start with 0
    if any(char.isdigit() for char in s):  # are there numbers
        first_digit_index = None
        for i in range(len(s)):
            if s[i].isdigit():
                first_digit_index = i
                break  # tells python to stop at first digit found

        # First number cannot be 0
        if s[first_digit_index] == "0":
            return False

        # After we find the first number, everything else must be a number
        if not s[first_digit_index:].isdigit():
            return False

    return True


if __name__ == "__main__":
    main()
