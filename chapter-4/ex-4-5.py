# Programming Exercise 4-5
#
# Program to compute total and average monthly rainfall over a span of years.
# This program gets a number of years from a user,
# then uses nested loops to prompt for rainfall for each month in each year
#	and calculate the total and the average monthly rainfall,
# then displays the number of months, total rainfall and average monthly rainfall

# Create float variables for total rainfall, monthly rainfall, average monthly rainfall

# Create int variables for number of years and number of months.



# Get number of years from the user
years = int(input("Number of years?: "))

# Nested loop logic to loop through the years and their months
#
# Outer for loop for the number of years

total = 0.0

for yr in range(years):
	
	print("Year", yr+1)
	print("______________")
	for month in range(12):
		print("Month", month+1,)
		rainfall = float(input("What is the rainfall for this month?: "))
		total += rainfall
		average = total/years

print("__________________________________________")
print("This is the average rainfall", format(average, '.2f'))
print("This is the total rainfall", format(total, '.2f'))
print("This is the total number of months", format(years*12, '.2f'))
	
	
		

	# Print the current year message

	# Inner loop for 12 months 

		# Get monthly rainfall for current month from the user
		
		# add monthly rainfall to total rainfall
		
		# increment number of months
		
			
# Calculate the average rainfall using total rainfall and number of months

# print the results on the screen, including details for total months, total rainfall,
#	and average monthly rainfall, formatting any floats to 2 decimal places.

