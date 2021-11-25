# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4
input_1 = input("Enter a string of words: ")
input_2 = input("Enter a letter to search for: ")
print(input_1.find(input_2))