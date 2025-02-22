# Task 1
# Write a function that prints formatted text given below:
# "Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself."
#                               Bill Gates

# def printBill(text, author):
#     print(f"\"{text}\"")
#     print("                             ",author)

# text="Don't compare yourself with anyone in this world…\n"\
#     "if you do so, you are insulting yourself."
# author="Bill Gates"
# printBill(text,author)

# -------------------------------------------------------------
# ----------- second task -------------------------------------
# -------------------------------------------------------------
# Task 2
# Write a function that takes two numbers as a parameter and displays 
# all even numbers in between.

# def displayEvenNumbers(x):
#     print(f"Even numbers in the {x} interval:")
#     for i in range (x[0], x[1]):
#         if i%2==0:
#             print (i,end=" ")

# displayEvenNumbers((5,12))


# -------------------------------------------------------------
# ----------- third task -------------------------------------
# -------------------------------------------------------------
# Task 3
# Write a function that prints an empty or solid square 
# made out of some symbol. 
# The function takes the following as parameters: 
# the length of the side of the square, a symbol, and a boolean variable:
# if it is True, the square is solid;
# if False, the square is empty.

# def printSquare(length, symbol, texture):
#     for rowi in range (0,length):
#         print()
#         for columni in range (0,length):
#             if rowi>0 and rowi<length-1 and columni>0 and columni<length-1:
#                 if texture==True:
#                     print(symbol,end="")
#                 else:
#                     print(" ",end="")
#             else:
#                 print (symbol,end="")

# length=int(input("Type the length of the square:"))
# symbol=input("Type the symbol to use in design:")
# solid=input("Is the square solid? (yes/no):")
# if solid=="yes":
#     texture=True
# else:
#     texture=False
# printSquare(length,symbol,texture)

# -------------------------------------------------------------
# ----------- fourth task -------------------------------------
# -------------------------------------------------------------
# Task 4
# Write a function that returns the smallest of five numbers. 
# Numbers are passed as parameters.

# def detectMin(n):
#     min=n[0]
#     for i in range (1,5): #starts from second element
#         if n[i]<min:
#             min=n[i]
#     return min
# n=[0,0,0,0,0]
# for i in range (0,5):
#     n[i]=input(f"No.{i+1} is: ")
# print(f"Minimum number is: {detectMin(n)}")


# -------------------------------------------------------------
# ----------- fifth task -------------------------------------
# -------------------------------------------------------------
# Task 5
# Write a function that returns the product of numbers in a specified range. 
# The start and end points of the range are passed as parameters. 
# If the order of these points is incorrect 
# (e.g., 5 is the end, and 25 is the start), swap them.

# def productAB(a,b):
#     if a<b:
#         min=a
#         max=b
#     else:
#         min=b
#         max=a
#     product=1
#     for i in range (min,max+1):
#         product*=i
#     return (product)
    

# a=int(input("First number:"))
# b=int(input("Second number:"))

# print(f"Product of provided numbers is {productAB(a,b)}")

# -------------------------------------------------------------
# ----------- sixth task -------------------------------------
# -------------------------------------------------------------
# Task 6
# Write a function that counts how many digits a number has. 
# The number is passed as a parameter. 
# Return the received number of digits from the function. 
# For example, if the passed number is 3456, it has 4 digits.

# def returnNdigits(n):
#     i=0
#     while n>0:
#         n=int(n/10)
#         i+=1
#         # print(i,"...",n)
#     return i

# n=int(input("Type a number:"))
# print (f"{n} has {returnNdigits(n)} digits.")


# -------------------------------------------------------------
# ----------- seventh task -------------------------------------
# -------------------------------------------------------------
# Task 7
# Write a function that checks if a number is a palindrome. 
# The number is passed as a parameter. 
# If the number is a palindrome, return true, otherwise false.

# A palindrome is a number which reads the same backward as forward. 
# For instance, 123321 is a palindrome, 546645 is a palindrome, 
# but 421987 is not.

def checkN(n):
    n1=n
    n2=0
    while n1>0:
        digit=n1%10
        n1=int(n1/10)
        n2=n2*10+digit
    if n==n2:
        return True
    else:
        return False


n=int(input("Type a number to check:"))
print(f"Checking if {n} is a palindrome... ",checkN(n))