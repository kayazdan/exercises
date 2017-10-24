# Programming Exercise 5-13
#
# Program to display a table of times and falling distances for a specific range in seconds.
# This program accepts no input,
# but uses a loop to pass a range of times in seconds to a function
# 	that returns the falling distance for that amount of time,
# and displays the results as a table.



# define the main function
def main():
    pass
    # define a local float variable to hold distance
    distance = 0.0
    g = 9.81

    # Set up results chart, printing time and falling distance separated by a tab
    # include a separator line made with a row of underscores
    print("Time\tFalling Distance",)
    print("______________________")
    
    
    # loop through a range of time values (in seconds)
    for time in range(1, 10):
        #return time
        # pass the time to a falling distance function and assign result to distance
        calc_falling_distance(time)
        falling_distance_answer = calc_falling_distance(time)
		# print the time and distance formatted to two places, separated by a tab
        print(format(time, '.2f'), format(falling_distance_answer, '.2f'))

# Define a function to calculate the falling distance for a time in seconds
# The function accepts a time in seconds as a parameter,
# computes the distance,
# and returns the distance it has fallen in that time
def calc_falling_distance(time):
    g = 9.81

# define a local float variable to hold falling distance
# compute the falling distance using a formula and the time
    falling_distance_answer = 0.5*g*time**2
# return the falling distance
    return falling_distance_answer


# Call the main function to start the program


main()


