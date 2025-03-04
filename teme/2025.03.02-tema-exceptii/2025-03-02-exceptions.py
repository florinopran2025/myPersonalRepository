# Module 7. Exceptions
# Part 2
 

# Task 1
# Write a program that asks a user for a number and calculates its factorial. 
# Handle an exception that occurs when a negative number is entered, and print an error message.

# class NegativeNumberError(Exception):
#     pass

# def checkNo(no):
#     if no<0:
#         raise NegativeNumberError("Should not be a negative number.")

# no=int(input("Your number is:"))

# try:
#     checkNo(no)
#     result=1
#     for i in range (1,no+1):
#         result=result*i
#     print(f"Factorial of {no} is {result}.")
# except NegativeNumberError as e:
#     print("Error: Negative number input.")
#     print("Details about the error:",e)


# Task 2
# Implement the first task through a function. 
# The function should take a number as a parameter and return the factorial. 
# The correctness check of the data obtained must be inside the function. 
# Create two versions of the function implementation:
# --  The first version does not handle the exception inside the function. All handling is on the outside;
# --  The second version handles the exception inside the function.


# class NegativeNumberError(Exception):
#     pass

# no=int(input("Your number is:"))

# def returnFactorial_v2(no):  
#     """Version 2: handle the exception inside the function"""
#     try:
#         if no<0:
#             raise NegativeNumberError("Should not be a negative number.")        
#         result=1
#         for i in range (1,no+1):
#             result=result*i        
#         return result
#     except NegativeNumberError as e:
#         return f"Error: Negative number input.\nDetails:{e}"   
# def returnFactorial_v1(no):  
#     """Version 1: handle the exception outside the function"""      
#     result=1
#     for i in range (1,no+1):
#         result=result*i        
#     return result
       

# #version 2 - handle exceptions inside the function
# print(returnFactorial_v2(no))
# #version 1 - handle exceptions outside the function
# try:
#     if no<0:
#         raise NegativeNumberError("Should not be a negative number.") 
#     print(returnFactorial_v1(no))
# except NegativeNumberError as e:
#     print(f"Error: Negative number input.\nDetails:{e}")

        

# Task 3
# Write a program that allows a user to fill a list from the keyboard with numbers. 
# After receiving the data, display a menu that allows you to perform the following operations:
# - Displaying the list;
# - Obtaining the maximum value in a list;
# - Obtaining the minimum value in a list;
# - Displaying the value of an element by an index entered by a user;
# - Deleting an element by an index entered by a user.
# *** Handle an exception that occurs when an element is out of a list 
# (a user entered an invalid value for an element index in a list) 
# and print an error message.

# import os

# class ErrorIndex(Exception):
#     pass

# def menu():
#     print("1. Display list")
#     print("2. Obtain the maximum value")
#     print("3. Obtain the minimum value")
#     print("4. Display the value of an element by an index")
#     print("5. Delete an element by an index")

# running=True
# numbers=[]
# while running:
#     number=input("Type a number: ")
#     if number!="exit":
#         numbers.append(int(number))
#     else:
#         running=False

# running=True
# while running:
#     os.system("cls")
#     menu()
#     option=input("What do you want to do?")
#     if option=="1":
#         print(numbers)
#     if option=="2":
#         print (max(numbers))
#     if option=="3":
#         print (min(numbers))
#     if option=="4":
#         nIndex=int(input("Index="))
#         try:
#             if nIndex>len(numbers)-1 or nIndex<0:
#                 raise ErrorIndex("No such index")    
#             print(numbers[nIndex])
#         except ErrorIndex as e:
#             print("There is a problem:",e)


#     if option=="5":
#         nIndex=int(input("Index="))
#         try:
#             if nIndex>len(numbers)-1 or nIndex<0:
#                 raise ErrorIndex("No such index.")
#             print("Deleting...", numbers[nIndex])
#             numbers.pop(nIndex)
#             print ("Deleted!")
#         except ErrorIndex as e:
#             print("There is an error:",e)
#     input("Type enter to return to the menu.")
        
    

# Task 4
# Implement the third task through functions. Create two versions of the function implementation:
# -- The first version does not handle exceptions inside the functions. All handling is on the outside;
# -- The second version handles exceptions inside functions. 

# import os

# class ErrorIndex(Exception):
#     pass

# def menu():
#     print("1. Display list")
#     print("2. Obtain the maximum value")
#     print("3. Obtain the minimum value")
#     print("4. Display the value of an element by an index")
#     print("5. Delete an element by an index")

# def enterToContinue():
#     input("Type enter to return to the menu.")

# def constructList(numbers):
#     number=input("Type a number: ")
#     if number!="exit":
#         numbers.append(int(number))
#         constructList(numbers)
#     return numbers

# def testIndex(index, numbers):
#     if 0<=index<len(numbers):
#         return True
#     else:
#         return False
    
# # for option 4
# def option4Inside(nIndex,numbers):
#     """Handle exceptions inside of the function (for option 4) """
#     try:
#         if testIndex(nIndex,numbers)==False:
#             raise ErrorIndex("No such index")    
#         print(numbers[nIndex])
#     except ErrorIndex as e:
#         print("There is a problem:",e)

# def option4Outside(nIndex,numbers):
#     """Handle exceptions outside of the function (for option 4)"""
#     print(f"The number with index {nIndex} is {numbers[nIndex]}")

# # for option 5
# def option5Inside(nIndex,numbers):
#     """Handle exceptions inside of the function (for option 5) """
#     try:
#         if nIndex>len(numbers)-1 or nIndex<0:
#             raise ErrorIndex("No such index.")
#         print("Deleting...", numbers[nIndex])
#         numbers.pop(nIndex)
#         print ("Deleted!")
#     except ErrorIndex as e:
#         print("There is an error:",e)

# def option5Outside(nIndex,numbers):
#     """Handle exceptions outside of the function (for option 5)"""
#     print("Deleting...", numbers[nIndex])
#     numbers.pop(nIndex)
#     print ("Deleted!")

# numbers=constructList([])
# print(numbers)
# enterToContinue()

# running=True
# while running:
#     os.system("cls")
#     menu()
#     option=input("What do you want to do?")
#     if option=="1":
#         print(numbers)
#     if option=="2":
#         print (max(numbers))
#     if option=="3":
#         print (min(numbers))
#     if option=="4":
#         nIndex=int(input("Index="))
#         #version 2 (inside the function)
#         option4Inside(nIndex,numbers)
#         #version 1 (outside the function)
#         try:
#             if testIndex(nIndex,numbers)==False:
#                 raise ErrorIndex("No such index")    
#             option4Outside(nIndex,numbers)
#         except ErrorIndex as e:
#             print("There is a problem:",e)
#     if option=="5":
#         nIndex=int(input("Index="))
#         #version 2 (inside the function)
#         option5Inside(nIndex,numbers)
#         #version 1 (outside the function)
#         try:
#             if nIndex>len(numbers)-1 or nIndex<0:
#                 raise ErrorIndex("No such index.")
#             option5Inside(nIndex,numbers)
#         except ErrorIndex as e:
#             print("There is an error:",e)
#     enterToContinue()