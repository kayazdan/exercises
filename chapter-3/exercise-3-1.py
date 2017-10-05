# Programming Exercise 3-1
#
# Program to display the name of a week day from its number.
# This program prompts a user for the number (1 to 7)
# and uses it to choose the name of a weekday
# to display on the screen.

# Variables to hold the day of the week and the name of the day.
# Be sure to initialize the day of the week to an int and the name as a string.


# Get the number for the day of the week.
# be sure to format the input as an int

nmb_day = input("What number of the day is it?: ")
int_nmb_day = int(nmb_day)




# Determine the value to assign to the day of the week.
# use a set of if ... elif ... etc. statements to test the day of the week value.



if int_nmb_day == 1:
    print("Monday")
elif int_nmb_day == 2:
    print("Tuesday")
elif int_nmb_day == 3:
    print("Wednesday")
elif int_nmb_day == 4:
    print("Thursday")
elif int_nmb_day == 5:
    print("Friday")
elif int_nmb_day == 6:
    print("Saturday")
elif int_nmb_day == 7:
    print("Sunday")
else:
    print("Out of range")
    
    



# use the final else to display an error message if the number is out of range.


# display the name of the day on the screen.




