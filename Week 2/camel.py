#implement a program that prompts the user for the name of a variable in camel case and
# outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.



camel_displayed = input("camelCase:")
converted_to_snake = ""

for word in camel_displayed:
    if word.isupper():
        converted_to_snake += "_" + word.lower()
    else:
        converted_to_snake += word

print("snake_case:", converted_to_snake)

