# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.
user_num = int(input("Enter an integer between 1 and 12: "))
if user_num > 12 or user_num < 0:
    print("Error")
else:
    if user_num == 1:
        print("January")
    if user_num == 2:
        print("February")
    if user_num == 3:
        print("March")
    if user_num == 4:
        print("April")
    if user_num == 5:
        print("May")
    if user_num == 6:
        print("June")
    if user_num == 7:
        print("July")
    if user_num == 8:
        print("August")
    if user_num == 9:
        print("September")
    if user_num == 10:
        print("October")
    if user_num == 11:
        print("November")
    if user_num == 12:
        print("December")