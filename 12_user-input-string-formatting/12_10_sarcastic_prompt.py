# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
user_input = input("What is your honest opinion?: ")
user_input = user_input.lower()
length = len(user_input)
sol = ""
for i in range(0,length):
    if i % 2 == 0:
        sol += user_input[i]
    else:
        sol += user_input[i].capitalize()
print(sol)