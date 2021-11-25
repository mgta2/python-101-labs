# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings
input_1 = input("Enter a string: ")
input_2 = input("Enter another string: ")
input_3 = input("Enter yet another string: ")
length_1 = len(input_1)
length_2 = len(input_2)
length_3 = len(input_3)
the_max = max(length_1, length_2, length_3)
if the_max == length_1:
    print(the_max, input_1)
elif the_max == length_2:
    print(the_max, input_2)
else:
    print(the_max, input_3)