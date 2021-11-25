# Demonstrate how to:
# -------------------
# 1) Convert an int to a float
# 2) Convert a float to an int
# 3) Perform division using a float and an int.
# 4) Use two variables to perform a multiplication.
#
# What information is lost during which conversions?

#1
x = 5
y = float(x)
print(y)

#2
x = 2.0
y = int(x)
print(y)

#3
x = 5
y = 2.5
print(x/y)

#4
x = 5
y = 2.1
print(x*y)

#What info do we lose?
#1: 2.0 as a float isn't as precise as 2 as an integer (2.0 could be 2+-epsilon)
#2: We lose the decimal part. e.g. int(2.1) = 2
#3: We lose info on the integer being precise (as in #1).
#4: (We lose info on what the original variables were, only getting the product.)