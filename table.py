# Program to print multiplication table of a number

# Input from user
num = int(input("Enter a number to print its multiplication table: "))

# Printing table
print(f"\nMultiplication Table of {num}:\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
