#implement a program in Python that prompts the user for mass as an integer (in kilograms) and
# then outputs the equivalent number of Joules as an integer.
#Assume that the user will input an integer.
# the formula is E =MC**2



speed = 300000000**2 #calculation of the speed which is approximately 300 000 000 to the power 2
mass = int(input("m:"))
energy = int(mass * speed)
print("e:", energy)