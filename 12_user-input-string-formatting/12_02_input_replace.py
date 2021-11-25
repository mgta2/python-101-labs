# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please
input_1 = input("Enter a string of words: ")
input_2 = input("Enter a symbol: ")
first_letter = input_1[0]
sol = ""
for char in input_1:
    if char == first_letter:
        sol += input_2
    else:
        sol += char
print(sol)