# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
user_input = input("Enter a string: ")
a = 0
i = 0
o = 0
e = 0
u = 0
my_str = "aioeu"
for char in user_input:
    if char == "a":
        a += 1
    if char == "i":
        i += 1
    if char == "o":
        o += 1
    if char == "e":
        e += 1
    if char == "u":
        u += 1
print("There are", a, "copies of a in:", user_input)
print("There are", i, "copies of i in:", user_input)
print("There are", o, "copies of o in:", user_input)
print("There are", e, "copies of e in:", user_input)
print("There are", u, "copies of u in:", user_input)