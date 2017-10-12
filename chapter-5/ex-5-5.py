# Programming Exercise 5-5
#
# Program to compute assessed value and property tax.
# This program accepts a property value from a user,
# uses global constants to calculate an assessed value and property tax,
# then passes them to a function to display the results for the user.



# Global constants for assessment percentage and property tax rate
assessment_percentage = 0.9
property_tax_rate = 0.1


# define the main function

    # Define local float variables for property value, assessed value and property tax
    # Get the property value from the users
    # Calculate the assessed value using the global constant
    # Calculate the property tax using the global constant
    # Call the function to display property tax information, 
    # passing assessed value and property tax as arguments


    
# Define a function to display property tax information.
# This function accepts the assessed value and property tax as parameters,
# performs no calculations,
# but displays the information with float variables formatted to 2 decimal places.

	# display the assessed value
	
	# display the property tax
	
def main():
    property_value = float(input("Property value: "))
    assessed_value = property_value*assessment_percentage
    property_tax = property_value*property_tax_rate
    property_tax_information(property_tax, property_value, assessed_value)
    
def property_tax_information(property_tax, property_value, assessed_value):
    print("Assessed value: ", format(assessed_value, '.2f'))
    print("Property tax: ", format(property_tax, '.2f'))



# Call the main function to begin the program.
main()
