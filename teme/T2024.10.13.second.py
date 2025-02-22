# Task 1
# The user types in a number. 
# Check if it is even or odd. 
# If the number is even, print the number and the text "Even number." 
# If the number is odd, print the number and the text "Odd number."
#  
# no=int(input("no="))
# if no%2==0:
#     print("Even number.")
# else:
#     print("Odd number.")

# Task 2
# The user types in a number. 
# Check if it is a multiple of 7. 
# If it is, print the number and the text "Your number is a multiple of 7." 
# If it is not, print the number and the text "Your number is not a multiple of 7." 

# no=int(input("no="))
# if no%7==0:
#     print("Your number is a multiple of 7.")
# else:
#     print("Your number is not a multiple of 7.")

# Task 3
# The user types in two numbers. 
# Find the maximum of two numbers and print it.

# a=int(input("a="))
# b=int(input("b="))
# max=a
# if a<b:
#     max=b
# print("Max=",max)

# Task 4
# The user types in two numbers. 
# Find the minimum of two numbers and print it.

# a=int(input("a="))
# b=int(input("b="))
# min=a
# if a>b:
#     min=b
# print("Min=",min)

# Task 5
# The user types in two numbers. 
# Based on the user's choice, 
# print the result of the sum, difference, product 
# of these numbers or their arithmetic mean.
a=int(input("a="))
b=int(input("b="))
opt=input("What do you want to calculate?\n"
          "(sum/difference/product/mean)")
if opt=="sum":
    print(f"{a}+{b}= {a+b}")
if opt=="difference":
    print(f"{a}-{b}= {a-b} \n{b}-{a}= {b-a}")
if opt=="product":
    print(f"{a}*{b}= {a*b}")
if opt=="mean":
    print(f"Mean of {a} and {b} is {(a+b)/2}")

