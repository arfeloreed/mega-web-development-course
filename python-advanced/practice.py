# #  profit margin

# #  function to calculate profit margin
# def cal_profit(made, cost):
#     net_income = made - cost
#     profit_margin = (net_income / made) * 100
#     return profit_margin

# revenue = int(input("What is your business's revenue this month?\n"))
# expenses = int(input("What is your business's expenses this month?\n"))

# # print(f"\nYour profit margin this month is {int(cal_profit())}")
# print(f"\nYour profit margin this month is {round(cal_profit(), 2)}")


#  profit margin

#  function to calculate profit margin
# def cal_profit(made, cost):
#     net_income = made - cost
#     # return round((net_income / made) * 100)
#     # return round((net_income / made) * 100, 2)
#     return round((net_income / made) * 100, 1)

# revenue = int(input("What is your business's revenue this month?\n"))
# expenses = int(input("What is your business's expenses this month?\n"))

# print(f"This is you month's profit margin {cal_profit(revenue, expenses)}%")



# [Easy] - Sum of Even Numbers in a List
# Write a program that takes in a list of numbers and returns the sum of all the even numbers in the list.

# Input: A list of integers

# Output: The sum of all the even numbers in the list

# Example:

# Input: [2, 4, 7, 8, 9, 10]
# Output: 24

def sum_of_even_numbers(lst):
    total = 0
    for i in lst:
        if not i % 2:
            total += i
    
    return total

print(f"sum of even is {sum_of_even_numbers([2, 4, 7, 8, 9, 10, 1, 6])}")