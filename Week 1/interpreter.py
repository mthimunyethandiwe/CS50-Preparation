# Implement a program that prompts the user for an arithmetic expression
# and then calculates and outputs the result 
# as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, #
#with one space between x and y and one space between y and z, wherein:
# x and z are integers
# y is +, -, * or /

math = input("Expression: ")
x, y, z = math. split()

x = int(x)
z = int(z)

if y == "+" :
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print(f"{result:.1f}")