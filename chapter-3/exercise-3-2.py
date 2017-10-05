# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats


# Get length A from the user and convert it to a float

length_a = input("What is the length for area A?: ")
f_length_a = float(length_a)


# Get width A from the user and convert it to a float

width_a = input("What is the width for area A?: ")
f_width_a = float(width_a)

# Get length B from the user and convert it to a float

length_b = input("What is the length for area B?: ")
f_length_b = float(length_b)

# Get width B from the user and convert it to a float

width_b = input("What is the width of Area B?: ")
f_width_b = float(width_b)

# Calculate area A
area_a = f_length_a*f_width_a


# Calculate area B
area_b = f_length_b*f_width_b

# Print each area, formatting the values to 2 decimal places

print(format(area_a, '.2f'), format(area_b, '.2f'))

# if area A is greater, print "A is greater" message.
if area_a > area_b:
    print("A is greater")
elif area_b > area_a:
    print("B is greater")
else:
    print("A and B are equal")

# else if area B is greater, print "B is greater" message.

# else print "A and B are equal" message.

