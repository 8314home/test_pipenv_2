# Given is a list of numbers , we need find the best time to buy and sell (days) from given list
# Note - buy price must be lower, than sell price so in list buy day will be before sell day
# finding highest difference between two values from a list given, values are at lower level.


LIST_OF_VALUES = [7,1,4,2,6,3]

# Using dynamic programming we can solve this
# Two variables we need to take - buyprice, profit
# We need to get a combination which will result max profit

buyprice = 99999 # taken a very high value
profit = 0


for x in LIST_OF_VALUES:
    if buyprice > x:
        buyprice = x
    else:
        profit = max(profit, x - buyprice)  # here we are trying to sell at x value

print("max profit - {0}".format(profit))


# Time complexity - O(n) as we need to traverse the list once
# Space complexity - O(1) as we just need to create two variables
