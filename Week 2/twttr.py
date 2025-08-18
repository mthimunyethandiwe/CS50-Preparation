# implement a program that prompts the user for a str of text and then outputs that same text but with 
# all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


def main():
    word = input("Input: ")
    response = ""

    for letter in word:
        if letter not in ["a", "e", "i", "o", "u"]:
            response += letter #if it is not a vowel, it adds the letters

    print(f"Output: {response}")

if __name__ == "__main__":
    main()
