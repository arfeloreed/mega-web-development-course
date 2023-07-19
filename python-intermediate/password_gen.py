# from random import choices


# characters = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#     's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
#     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1',
#     '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+'
# ]

# # ask the user for how many characters the password would have
# char_num = int(input("How many characters for your password?\n"))

# # take the user input and use it to choose random characters from the list and made a list
# pass_list = choices(characters, k=char_num)
# print(pass_list)

# # join the elements of the list generated intp 1 string
# password = "".join(pass_list)
# print(password)


import string
import random as rd


# Ask the user for how long the password is
print("Welcom to Reed's password generator")
numb = int(input("How many characters do you want?\n"))

# assigning variables
letters = string.ascii_letters
digits = string.digits
punctuations = string.punctuation
# combine all into 1 string
all_char = letters + digits + punctuations

# get the password for the user
pass_list = rd.sample(all_char, k=numb)
# print(pass_list)
password = "".join(pass_list)
print(password)