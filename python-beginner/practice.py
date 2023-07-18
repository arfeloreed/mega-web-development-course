# print ("Hello world once again!! I'm back.")

# your_age = input("How old are you:\n")
# print(f"\nI am {your_age} years old too.")

# name = input("Enter your name:\n")
# print(f"Your name {name} has {len(name)} letters on it.")

# print(len(input("What is your name?\n")))


# Breakeven practice
# rent = 2500
# coffee_cost = 1.40
# coffee_per_cup = 2.95

# breakeven = round(rent / (coffee_per_cup - coffee_cost))
# print(f"You need to sell approximately {breakeven} cups of coffee each month to breakeven.")


# conditional statement
# hour = int(input("How many hours passed the last time you ate?\n"))

# if hour >= 5:
#     print("Order some food now!!")
# else:
#     print("Keep working.")

# discount
product_cost = 50
number_of_products = int(input("How many products did you buy?\n"))
total_cost = product_cost * number_of_products

if total_cost >= 500:
    discount = 0.15 #15%
    discounted_amount = total_cost * discount
    print(f"The cost is ${total_cost} and you have a ${discounted_amount} discount.")
elif total_cost >= 200:
    discount = 0.05 #5%
    discounted_amount = total_cost * discount
    print(f"The cost is ${total_cost} and you have a ${discounted_amount} discount.")
else:
    print(f"You don't have any discount. You should pay ${total_cost}")