# Task 1
# Write a program that requests two integers x and y, 
# and then calculates and prints the value of x raised to the power of y.

# x=int(input("x="))
# y=int(input("y="))
# if y==0:
#     result=1
# else:
#     result=x
#     for i in range (1,y):
#         result=result*x
# print (f"{x} raised to the power of {y} is {result}")

# Task 2
# Count the number of integers in the range from 100 to 999 that have two identical digits.
# INTERPRETARE PERSONALA: ENUNTUL NU SPUNE "DOAR DOUA CIFRE IDENTICE", 
# PRIN URMARE UN NUMAR CU 3 CIFRE IDENTICE RESPECTA ENUNTUL.
# (UN NUMAR CU 3 CIFRE IDENTICE RESPECTA ENUNTUL DE A AVEA DOUA CIFRE IDENTICE)
# TOTUSI: CERINTA CU "DOAR DOUA CIFRE IDENTICE" ESTE MAI DIFICILA, PRIN URMARE 
# VOI APLICA ACEASTA CONDITIE

digits=[]
numberOfNumbers=0
numberOfNumbersDD=0 #number of numbers with different digits
for no in range (100,999+1):
    numberOfNumbers+=1
    currentNo=no
    i=0
    digits=[]
    #verify each number    
    while currentNo>0: 
        eachDigit=currentNo%10   
        # print(eachDigit,end=" ")
        currentNo=int(currentNo/10)  
        digits.append(eachDigit) # add eachDigit to the list
        i+=1 #for the list
    valid=True # if the number is ok
    if digits[0]==digits[1] and digits[1]==digits[2]: #all 3 digits are the same => invalid
        valid=False
    if digits[0]!=digits[1] and digits[1]!=digits[2] and digits[0]!=digits[2]: 
        #all digits are different => invalid
        valid=False
    if valid==True:
        numberOfNumbersDD+=1
print (f"There are {numberOfNumbers} in your interval.")
print(f"Number of numbers in your interval that passed the test is {numberOfNumbersDD}.")

# Task 3
# Count the number of integers in the range from 100 to 9999 that have different digits.

# digits=[]
# numberOfNumbers=0
# numberOfNumbersDD=0 #number of numbers with different digits
# for no in range (100,9999+1):
#     numberOfNumbers+=1
#     currentNo=no
#     i=0
#     validNumber=True
#     digits=[]
#     #verify each number    
#     while currentNo>0: 
#         eachDigit=currentNo%10   
#         # print(eachDigit,end=" ")
#         currentNo=int(currentNo/10)        
#         if eachDigit in digits: # TEST if there is any duplicate in it's digits, the number is not valid
#             validNumber=False
#             # print(validNumber)
#         digits.append(eachDigit) # add eachDigit to the list, only after you applied the TEST
#         i+=1 #for the list
#     if validNumber==True: #if the number is valid, we count it
#         numberOfNumbersDD+=1
# print (f"There are {numberOfNumbers} in your interval.")
# print(f"Number of numbers in your interval that passed the test is {numberOfNumbersDD}.")


# Task 4
# The user types in an integer value. Remove all 3s and 6s from this integer and print it. 

# x=int(input("Type your integer: "))
# xi=x
# digits=[]
# while xi>0:
#     d=xi%10
#     if d!=3 and d!=6:
#         digits.append(d)
#     xi=int(xi/10)
# # print(digits)

# result=0
# i=len(digits)-1
# while i>=0:
#     result=result*10+digits[i]
#     # print(result)
#     i-=1

# print("Your number (with no 3s or 6s) is:",result)