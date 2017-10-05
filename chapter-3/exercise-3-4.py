# Programming Exercise 3-4
#
# Program to convert a number from 1 to 10 to a Roman numeral.
# This program will accept an integer from 1 to 10 from the user
# and use it to choose an appropriate Roman numeral
# to display on the screen.

# Variables to hold a number and a numeral.
# initialize the number as an int and the numeral as a string.

# Get number from user and convert it to an int


# Set numeral to a Roman numeral value based on the value of number
# use a set of if ... elif .... etc. statements.

numeral = input("Put in the number you want to convert to a Roman Numeral: ")
i_numeral = int(numeral)

if i_numeral == 1:
    print("I")
elif i_numeral == 2:
    print("II")
elif i_numeral == 3:
    print("III")
elif i_numeral == 4:
    print("IV")
elif i_numeral == 5:
    print("V")
elif i_numeral == 6:
    print("VI")
elif i_numeral == 7:
    print("VII")
elif i_numeral == 8:
    print("VIII")
elif i_numeral == 9:
    print("IX")
elif i_numeral == 10:
    print("X")
else:
    print("Out of range")

# use a final else to display an error if number is out of range.


# display the numeral on the screen.






