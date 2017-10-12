# Programming Exercise 5-4
#
# Program to compute monthly and annual auto expenses.
# This program prompts a user for several auto monthly expense amounts,
# then passes them to a function to total the values, annualize them,
# and display the details and totals on the screen.



# define the main function

    # Define local float variables for loan, insurance, gas, oil, tires and maintenance


    # Get the amount of the monthly loan payment from the user.

    # Get the amount of the monthly insurance from the user.

    # Get the amount of the monthly gas from the user.

    # Get the amount of the monthly oil from the user.


    # Get the amount for monthly tire wear from the users.


    # Get the amount for monthly maintenance from the user.

        
    # Call the function to summarize car expenses,
    # passing the loan, insurance, gas, oil, tires and maintenance as arguments.



# Define a function to summarize car expenses,
# it accepts loan, insurance, gas, oil, tires, and maintenance as arguments,
# calculates a monthly total and an annual total,
# and displays these totals.

def main():
    loan = float(input("Monthly loan payment amount: "))
    insurance = float(input("Monthly insurance amount: "))
    gas = float(input("Monthly gas amount: "))
    oil = float(input("Monthly gas amount: "))
    tires = float(input("Monthly tire wear: "))
    maintenance = float(input("Monthly maintenence: "))
    summarize_car_expenses(loan, insurance, gas, oil, tires, maintenance)


def summarize_car_expenses(loan, insurance, gas, oil, tires, maintenance):
    # Define local float variables for monthly total and annual total

    # calculate the monthly total
    monthly_total = loan+insurance+gas+oil+tires+maintenance
    # calculate the annual total
    annual_total = monthly_total*12

    # Print monthly and annual information, formatting float value to 2 decimal places.
    print("Monthly total: ", format(monthly_total, '.2f'))
    print("Annual total: ", format(annual_total, '.2f'))


# Call the main function to start the program
main()
