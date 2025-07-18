#In a file called bank.py, implement a program that prompts the user for a greeting. 
# If the greeting starts with “hello”, output $0. 
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
# ing case-insensitively.

greet = input("greeting: ")

greet_converted = greet.strip().lower()

if greet_converted.startswith("hello"):
    print("$0")

elif greet_converted.startswith("h"):
    print("$20")


else:
    print("$100")