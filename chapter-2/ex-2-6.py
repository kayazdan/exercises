# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats


# Constants for the state and county tax rates

state_tax = 0.6
county_tax = 0.7

# Get the amount of purchase from the user, casting it to a float.

purchase_amount = input("How much was your purchase?: ")
f_purchase_amount = float(purchase_amount)

# Calculate the state sales tax.

state_sales_tax = state_tax * f_purchase_amount


# Calculate the county sales tax.

county_sales_tax = county_tax * f_purchase_amount

# Sum the total tax.

total_tax = county_sales_tax + state_sales_tax

# Calculate the total of the sale.

grand_total = total_tax + f_purchase_amount


# Print detailed information about the sale, formatting all values to two decimal places.

print("Here is your grand total:", format(grand_total, '.2f'), "Here is your total tax: ", format(total_tax, '.2f'), "Here is your purchase amount: ", format(f_purchase_amount, '.2f'))



