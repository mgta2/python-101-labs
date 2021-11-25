# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.
user_num = int(input("Enter an integer between 0 and 1,000,000,000: "))
my_num = 0
while my_num < 1000000001:
    if my_num == user_num:
        print(my_num)
        break
    my_num += 1