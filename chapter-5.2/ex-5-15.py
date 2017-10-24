# Programming Exercise 5-15
#
# Program to find the average of five scores and output the scores and average with letter grade equivalents.
# This program prompts a user for five numerical scores,
# calculates their average, and assigns letter grades to each,
# and outputs the list and average as a table on the screen.

# define the main function
    # define local variables for average and five scores
    # Get five scores from the user
    # find the average by passing the scores to a function that returns the average
    # display grade and average information in tabular form
    # as score, numeric grade, letter grade, separated by tabs
    
        # display a line of underscores under this header
    
    # print data for all five scores, using the score,
    # with the result of a function to determine letter grade

    # display a line of underscores under this table of data

    # display the average and the letter grade for the average



# Define a function to return the average of 5 grades.
# This function accepts five values as parameters,
# computes the average,
# and returns the average.
    # define a local float variable to hold the average
    # calculate the average
    # return the average

# Define a function to return a numeric grade from a number.
# This function accepts a grade as a parameter,
# Uses logical tests to assign it a letter grade,
# and returns the letter grade.

    # if score is 90 or more, return A
    # 80 or more, return B
    # 70 or more, return C
    # 60 or more, return D
    # anything else, return F

# Call the main function to start the program

    
def main():
    
    average = 0
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0
    score5 = 0
    
    
    score1 = int(input("Score one: "))
    score2 = int(input("Score two: "))
    score3 = int(input("Score three: "))
    score4 = int(input("Score four: "))
    score5 = int(input("Score five: "))
    
    
    
    find_average(score1, score2, score3, score4, score5)
    average = find_average(score1, score2, score3, score4, score5)
    
    get_letter_grade(average)
    letter_grade = get_letter_grade(average)
    
    
    print("                         ")
    print("Average Grade: ", '\t', "Letter Grade: ")
    print("__________________________________________")
    print(average, '\t', "                     ", letter_grade)
    

def find_average(score1, score2, score3, score4, score5):
    average = 0.0
    all_score = score1 + score2 + score3 + score4 + score5
    average = all_score/5
    return average
    
    
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    


main()
