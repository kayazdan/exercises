# Programming Exercise 5-2
#
# Program to calculate final purchase details.
# This program takes a purchase amount from a user,
# then calculates state tax, county tax and total tax,
# 	and passes them to a function to be totaled
# and displayed



# Global constants for the state and county tax rates
STATE_TAX = 0.06
f_STATE_TAX = float(STATE_TAX)

COUNTY_TAX = 0.01
f_COUNTY_TAX = float(COUNTY_TAX)

# define the main function

    # Define local float variables for purchase, state tax and county tax
    
    # Get the purchase amount from the user
    
    # Calculate the state tax using the global constant for state tax rate
    
    # Calculate the county tax using the global constant for county tax rate
    
    # Call the sale details function, passing the purchase, state tax and county tax
    
    
def main():
    
    
    purchase_amount = 0.0
    
    purchase_amount = float(input("Purchase amount: "))
    
    total_state_tax = f_STATE_TAX * purchase_amount
    total_county_tax = f_COUNTY_TAX * purchase_amount
    print("Purchase price: ", format(purchase_amount, '.2f'))
    print("State tax: ", format(STATE_TAX, '.2f'))
    print("County tax: ", format(COUNTY_TAX, '.2f'))
   
    purchase_details(purchase_amount, total_county_tax, total_state_tax)

def purchase_details(purchase_amount, total_county_tax, total_state_tax):
    
    total_tax = total_county_tax + total_state_tax
    sale_total = total_tax + purchase_amount
    print("Total tax: ", format(total_tax, '.2f')) 
    print("Total purchase amount: ", format(sale_total, '.2f'))
    
# define a function to display purchase details
# this function accepts purchase, stateTax, and countyTax as arguments,
# calculates the total tax and sale total,
# then displays the purchase details

    # Define local float variables for total tax and sale total

	# Calculate the total tax
	
	# Calculate the total sale

    # Display the purchase details, including purchase, state tax, county tax,
    #	total tax, and sale total, each on a line.  Format floats to 2 decimal places.



# Call the main function to start the program.

main()