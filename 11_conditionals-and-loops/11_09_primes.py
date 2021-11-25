# Print out every prime number between 1 and 1000.

# Number n is prime if n has no factors 2, ... , sqrt(n)

for i in range(2,1001):
    prime = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            prime = False
    if prime == True:
        print(i)