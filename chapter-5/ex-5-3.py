# Programming Exercise 5-3
#
# Program to compute recommended insurance to carry on an item.
# This program accepts a replacement cost from a user,
# calculates a minimum recommended insurance to carry from a global constant,
# then passes these values to a function to be displayed



# Global constant for the percent of replacement cost to insure



# Define the main function

    # Define local float variables for replacement cost and minimum insurance
def main():
    replacement_cost = float(input("Replacement cost: "))

    # Get the replacement cost from the user
    # Calculate the minimum insurance amount using the global constant
    MINIMUM_INSURANCE = 0.8
     
    # Call the function to display the insurance details, 
    # passing the replacement cost and minimum insurance to the function
    insurance_details(replacement_cost, MINIMUM_INSURANCE)

      
# Define a function to display the insurance details
# This function accepts the replacement cost and minimum insurance as parameters,
# uses the global constant to calculate percent insured,
# and displays the insurance details.
def insurance_details(replacement_cost, MINIMUM_INSURANCE):
    percent_insured = replacement_cost*MINIMUM_INSURANCE
    
    
	# display the replacement cost, formatting the value to 2 decimal places
    print("Replacement cost: ", format(replacement_cost, '.2f')) 
    # display the percent insured, formatting the value to 2 decimal places
    print("Percent insured: ", format(percent_insured, '.2f'))
	# display the minimum insurance, formatting the value to 2 decimal places
    print("Minimum insurace: ", format(MINIMUM_INSURANCE, '.2f'))


# Call the main function to start the program
main()
