# Programming Exercise 3-6
#
# Program to check if a date is 'magic' (day * month = year).
# This program takes a month, day and year from the user as integers,
# Checks to see if each is in range, then checks whether month * day = year,
# then displays an appropriate message depending on the result

# Variables for month, day, year and message
# initialize month, day and year as integers, message as a string


# Get month and cast it to int

month = input("What is the month?: ")
i_month = int(month)

# Get day and cast it to int

day = input("What is the day?: ")
i_day = int(day)

# Get year and cast it to int

year = input("What is the year?: ")
i_year = int(year)

# This problem can be solved with if-else logic by the reducing the problem domain
# if month input is out of range

	# set message to hold "invalid month" message
	
if i_month <1 or i_month >12:
    print("invalid month")
elif i_day <1 or i_month>31:
    print("invalid day")
elif i_year <0 or i_year >99:
    print("invalid year")
else:
    if i_year == i_day * i_month:
        print( i_month, "/", i_day, "/", i_year, sep='')
        print("This is a magic date")
        
    else:
        print(i_month, "/", i_day, "/", i_year, sep='')
        print("This is not a magic date")
        
    



# else if day input is out of range

    # set message to hold "invalid day" message

# else if  year input is out of range (greater than 99 or less than 0)

    # set message to hold "invalid year" message

# else 

    # set message to hold the date in 00/00/00 form
    
    # if day * month equals year, add " is a magic date" to message
    
    # else add " is not a magic date" to message


# print message for the user


