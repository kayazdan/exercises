# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.




# Constant for the sales tax rate.

tax = 0.6

# Get the price of each item by prompting the user.
# You will need to convert each input to a float.

price_one = input("What is the first price?: ")
f_p_one = float(price_one)

price_two = input("What is the second price?: ")
f_p_two = float(price_two)

price_three = input("What is the third price?: ")
f_p_three = float(price_three)

price_four = input("What is the fourth price?: ")
f_p_four = float(price_four)

price_five = input("What is the fifth price?: ")
f_p_five = float(price_five)


# Calculate the subtotal by adding up the item prices.

price_total = (f_p_one + f_p_two + f_p_three + f_p_four + f_p_five)

# Calculate the sales tax by multiplying the subtotal by the tax rate.

sales_tax = (price_total * 0.6)

# Calculate the total by adding the subtotal and tax.

total = sales_tax + price_total


# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 

print("Here is your total", format(total, '.2f'), "Here is your tax", format(sales_tax, '.2f'), "Here is your subtotal", format(price_total, '.2f'))



