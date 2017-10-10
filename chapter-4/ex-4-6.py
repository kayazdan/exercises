# Programming Exercise 4-6
#
# Program to display a table of Celsius and Fahrenheit equivalents.
# This program takes no input.
# It calculates a series of Fahrenheit equivalents for a range of Celsius temperatures
# then displays them in a table.


# Declare a float variable to hold the Fahrenheit temperature.


# Declare a constant to hold the max celsius value

celsius = 101

# Display a table header with Celsius and Fahrenheit separated by two tabs.
# Display a line separator made of underscores

print("Celsius\tFahrenheit")
print("_____________________________")

# Use a for loop to iterate from 0 through the range of Celsius temperatures
for celsius in range(1, celsius):
    fahrenheit = celsius * 9/5 + 32
    print(celsius, '\t', fahrenheit)

# 	Calculate the Fahrenheit temperature for the current Celsius value

#	Display the current Celsius and Fahrenheit values, separated by two tabs





