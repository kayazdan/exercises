# A cookie recipe calls for the following ingredients:
# 1.5 cups of sugar
# 1 cup of butter
# 2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients. 
# Write a program that asks the user how many cookies he or she wants to make, 
# and then displays the number of cups of each ingredient needed for the specified number of cookies


SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75

COOKIES = 48

sugar_for_one = SUGAR/COOKIES
butter_for_one = BUTTER/COOKIES
flour_for_one = FLOUR/COOKIES


amnt_cookies = input("How many cookies do you want to make?: ")
f_amnt_cookies = float(amnt_cookies)

amnt_sugar = f_amnt_cookies * sugar_for_one 
amnt_butter = f_amnt_cookies * butter_for_one 
amnt_flour = f_amnt_cookies * flour_for_one

print("Here is how much sugar you should use: ", amnt_sugar, "Here is how much butter you should use: ", amnt_butter, "Here is how much flour you should use: ", amnt_flour)



