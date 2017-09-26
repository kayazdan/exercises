# Programming Exercise 2-2
#
# Program to compute expected profit from sales.
# This program will prompt a user for a sales projection
# and use it to calculate expected profit from a predefined profit margin
# then display the result.


# Variables to hold the sales total and the profit
# initialize them as float values
sales_projection = input("What is the sales projection?: ")

f_sales_projection = float(sales_projection)


# Get the amount of projected sales.
# be sure to convert the input to a float


# Calculate the projected profit using a 23% profit margin.
projected_profit = (f_sales_projection*0.230)
profit = (f_sales_projection + projected_profit)


# Print the projected profit.
# be sure to format the output to two decimal places

print("The profit is:", format(profit, '.2f'))
    



