# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.
user_input = input("Enter an integer from 1 to 1,000,000,000: ")
# 'n' is divisible by 3 iff the sum of its digits are too.
sum = 0
for char in user_input:
    sum += int(char)
if sum % 3 == 0:
    print(user_input, "is divisible by 3")
else:
    print(user_input, "is not divisble by 3")