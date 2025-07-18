# Using if, or and else conditionals

answer = input(
    "What is the Answer to the Greatest Question of life, the Universe and Everything:")

# use the strip for no space between and converted the output to lower, whenever the input is in caps
converted_answer = answer.strip().lower()

if converted_answer == "42" or converted_answer == "forty-two" or converted_answer == "forty two":
    print("Yes")

else:
    print("No")
