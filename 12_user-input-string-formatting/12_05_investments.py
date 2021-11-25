# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
capital = float(input("How much will you invest?: "))
interest = float(input("What is the interest rate?: "))
years = int(input("How many years?: "))
for i in range(1,years+1):
    capital += capital*interest
    print(f"Money at year {i} is", capital)