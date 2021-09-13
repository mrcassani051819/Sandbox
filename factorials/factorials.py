#!/usr/bin/env python3

# Factorials
# for any real integer 1 to n where n! is no larger than a 64-bit integer, print n!

number = int(input("Enter a number: "))
factorial = 1
if number < 0:
    print("Error: Non-negative numbers only")
elif number == 0 or number == 1:
    print(1)
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print(factorial)
        