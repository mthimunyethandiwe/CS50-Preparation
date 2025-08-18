# implement a program that prompts the user for a str of text and then outputs that same text but with 
# all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


def main():
    word = input("Input: ")
    result = ""

    for letter in word:
        if letter not in ["a", "e", "i", "o", "u"]:
            result += letter #if it is not a vowel, it adds the letters

    print(f"Output: {result}")

if __name__ == "__main__":
    main()
