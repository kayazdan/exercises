# Programming Exercise 6-3
#
# Program to open a file and display its contents with line numbers.
# This program prompts the user for a file name,
# reads the file until it ends
# then displays each line with its line number before closing the file.

# define the main function
def main():
    line = ""
    filename = ""
    counter = 0
    
    filename = input("File name: ")
    file = open(filename, "r")
    line = file.readlines()
    for line in line:
        counter += 1
        line = line.strip('\n')
        print(counter, line, sep=') ')
    file.close()


    
    

    # Define local variables for line and filename (strings) and counter (int)

    
    # Prompt the user for a file name


    # Open the specified file for reading

    # use a for loop to loop through all the lines

        # increment the counter

        # print the current line number without carriage return
       
        # Strip the '\n' from the end of the line

        # display the line (should be on same line as line number)


    # Close file


# Call the main function to start the program

main()
