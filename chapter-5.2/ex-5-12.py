# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.



# define the main function
def main():
    # Define local variables to hold two integers
    integer_one = 0
    integer_two = 0
    # prompt the user for the first integer
    first_integer = int(input("First integer: "))
    
    # prompt the user for the second integer
    second_integer = int(input("Second integer: "))

    # print the return value from calling a function to find the greater of two integers
    # the two integers are passed as arguments
    compare_two_integers(integer_one, integer_two, first_integer, second_integer)
    result = compare_two_integers(integer_one, integer_two, first_integer, second_integer)
    print(result, "is the greater integer")

 
# Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.
def compare_two_integers(integer_one, integer_two, first_integer, second_integer):
    if first_integer > second_integer:
        result = first_integer
        return result
        
    else:
        result = second_integer
        return result

	# if the first integer is greater, return the first integer

	# else, return the second integer



# Call the main function to start the program
main()




