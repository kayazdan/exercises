# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.




# Get the person's age.
# remember to convert the input to an int.

p_age = input("What is this person's age?: ")
i_age = int(p_age)


# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.

if i_age <2:
    print("This person is an infant")
elif i_age <13:
    print("This person is a child")
elif i_age <20:
    print("This person is a teenager")
elif i_age <200:
    print("This person is an adult")
else:
    print("This person is probably dead")





# display a message with the age category.



