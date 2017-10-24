import random

# Programming Exercise 5-16
#
# Program to compare the proportion of odd and even random integers.
# This program accepts no input.
# It uses a loop and the random library to generate 100 random integers,
# counts the number of odd and even results,
# and displays the total of each.

# To use the random integer function, import the random library


def main():
    even = 0
    odd = 0
    for number in range(100):
        number = random.randint(1, 10000)
        check_even_number(number)
        check = check_even_number(number)
        
        if check == True:
            even += 1
        else:
            odd += 1
    print("Even: ", even)
    print("Odd: ", odd)
    
    
def check_even_number(number):
    if (number % 2) == 0:
        return(True)
    else:
        return(False)


# define the main function
    # define local int variable for number, odd and even totals
    # define a constant to hold how many numbers to compare (100)
    # loop through the range of numbers to compare
        # get a random integer from the random library function
        # if the check for even function returns true, increment even counter
        # else increment odd counter.

    # display the results on the screen


# Define a function to check for even numbers
# This function accepts one integer parameter,
# uses the mod operater to see if can be evenly divided by two,
# and return true if it can, false it cannot

    # if dividing the number by two yields no remainder, return true
    # else return false

# Call the main function to begin the program


main()