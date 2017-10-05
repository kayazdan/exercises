# Programming Exercise 3-5
#
# Program to convert a value in kilograms to Newtons, then check whether it is in range.
# This program will prompt a user for a mass in kilograms,
# convert it to Newtons and use constants to check if the weight is within range,
# then display the weight and a range message.



# Global constants for minimum, maximum and mass multiplier values


# Variables for weight and mass initialized as floats   


# Get mass from user and convert it to a float


# Calculate weight using the mass multiplier constant


# Display the weight

# If weight > maximum or < than minimum display an appropriate message

minimum = 0
maximum = 10000000000000000


newton = 9.81
mass = input("What is the mass?: ")
f_mass = float(mass)

weight = f_mass * newton

print(weight)

if weight > maximum:
    print("That is too big you idiot")
elif weight < minimum:
    print("That's too small")
else:
    print("It's fine")
    






