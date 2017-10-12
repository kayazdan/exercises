# Programming Exercise 5-6
#
# Program to compute calories from fat and carbohydrate.
# This program accepts fat grams and carbohydrate grams consumed from a user,
# uses global constants to calculate the fat calories and carb calories,
# then passes them to a function for formatted display on the screen.


# Global constants for fat calories per gram and carb calories per gram
fat_calories_per_gram = 9
carb_calories_per_gram = 4


# define the main function
    # Define local float variables for grams of fat, grams of carbs, calories from fat,
    # and calories from carbs
    # Get grams of fat from the users
    # Get grams of carbs from the user.
    # Calculate calories from fat.
    # Calculate calories from carbs.
    # Call the display calorie detail function, passing grams of fat, grams of carbs,
    # calories from fat and calories from carbs as arguments
def main():
    fat_grams = float(input("Grams of fat: "))
    carb_grams = float(input("Grams of carbs: "))
    fat_calories = fat_grams * fat_calories_per_gram
    carb_calories = carb_grams * carb_calories_per_gram
    calorie_detail(fat_calories, carb_calories, fat_grams, carb_grams)
    
def calorie_detail(fat_calories, carb_calories, fat_grams, carb_grams):
    print("Calories in", fat_grams, "grams of fat: ", format(fat_calories, '.2f'))
    print("Calories in", carb_grams, "grams of carbs: ", format(carb_calories, '.2f'))
# Define a function to display calorie detail.
# This function accepts grams of fat, grams of carbs, calories from fat,
# and calories from carbs as parameters,
# performs no calculations,
# but displays this information formatted for the user.

# print each piece of information with floats formatted to 2 decimal places.



# Call the main function to start the program

main()