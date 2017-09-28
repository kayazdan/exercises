# Last month Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:

#The number of shares that Joe purchased was 2,000
#When Joe purchased the stock, he paid $40.00 per share
# Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid for the stock

#Two weeks later Joe sold the stock. Here are the details of the sale

# The number of shares that Joe sold was 2,000
# He sold the stock for $42.75 per share
# He paid his stockbroker another commision that amounted to 3 percent of the amount he received for the stock.

# Write a program that displays the following information:
# The amount of money Joe paid for the stock.
# The amount that Joe sold the stock for.
# The amount of commission Joe paid his broker when he sold the stock
# Display the amount of money that Joe had left when he sold the stock and paid his broker (both times)
# If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money

stock = 2000
joe_paid = 40
joe_sold = 42.75
broker = 0.03

stock_paid = stock*joe_paid
commission_paid = stock_paid*broker

stock_sold = joe_sold*stock

commission_sold = stock_sold*broker
commission_total = commission_sold+commission_paid

stock_total = stock_sold - stock_paid

grand_total = stock_total - commission_total



#joe_stock_paid = 2,000/40
#joe_stock_sold = 2000/42.75

#f_joe_stock_paid = float(joe_stock_paid)
#f_joe_stock_sold = float(joe_stock_sold)


#broker_paid = f_joe_stock_paid * 0.03


#broker_sold = f_joe_stock_sold * 0.03


#broker_total = broker_sold + broker_paid

#total_joe = joe_stock_sold - joe_stock_paid

#grand_total = total_joe - broker_total



print("This is how much Joe paid for the stock", stock_paid, "This is how much Joe sold the stock for", stock_sold, "This is how much Joe paid in commission to the stockbroker", commission_total, "Here is Joe's grand total", grand_total)




