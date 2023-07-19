# even_numbers = []

# numb1 = int(input("Give me 2 numbers separately.\n1st number:\n"))
# numb2 = int(input("2nd number:\n"))
# if not numb1 % 2:
#     even_numbers.append(numb1)
# if not numb2 % 2:
#     even_numbers.append(numb2)

# print(even_numbers)


# while loop
# even_numbers = []

# while True:
#     numb1 = int(input("Give a number:\n"))
#     if not numb1 % 2:
#         even_numbers.append(numb1)
#     print(even_numbers)

#     stop = input("Do you want to continue?(Yes or No)\n").lower()
#     if stop == "no":
#         break

# even_numbers = []
# count = 0

# while count < 3:
#     count += 1
#     print(f"Round: {count}")
#     numb1 = int(input("Give a number:\n"))
#     if not numb1 % 2:
#         even_numbers.append(numb1)

# print(even_numbers)

# for loop
# for count in range(1, 4):
#     numb1 = int(input(f"Round {count}\nGive me a number:\n"))
#     if not numb1 % 2:
#         even_numbers.append(numb1)

# print(even_numbers)

# odd or even numbers
# even_numbers = []
# odd_numbers = []

# for numb in range(1, 101):
#     if numb % 2:
#         odd_numbers.append(numb)
#     else:
#         even_numbers.append(numb)

# print(f"Even numbers are:\n{even_numbers}")
# print(f"Odd numbers are:\n{odd_numbers}")


# squared numbers
# Square list items
# Turn every item of a list into its square:

# Write codes that get the given list, square each list item, and then add them to a new list called "result".

# Steps:

# create a new list called "result"

# write a code that squares each item in the given list and adds it to the new list (you must use for loop).

# Print the new list to the terminal.

# numbers = [1, 2, 3, 4, 5, 6, 7]
# add your code below this line:
# result = []
# for n in numbers:
#     result.append(n**2)

# print(result)


# exercise
# count the words given by the user
words = input("Enter some random words:\n")
word_list = words.split()
print(word_list)
print(f"\nYou've given {len(word_list)} words.")