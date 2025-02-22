# -------------------------------------------------------------
# ---------------- Task 1 -------------------------------------
# -------------------------------------------------------------
# Write a function that calculates the product of the elements from a list of integers. 
# The list is passed as a parameter. The result is returned from the function.

# def productList(list):
#     product=1
#     for i in list:
#         product*=i
#     return product

# print ("Type \"exit\" to stop:")
# gameon=True
# i=0
# list=[]
# while gameon:
#     x=input(f"Number {i+1} is: ")
#     i+=1
#     if x=="exit":
#         gameon=False
#     else:
#         list.append(int(x))
# print (f"Product is: {productList(list)}")
        

# -------------------------------------------------------------
# ---------------- Task 2 -------------------------------------
# -------------------------------------------------------------
# Write a function to find the minimum in a list of integers. 
# The list is passed as a parameter. The result is returned from the function.

# def minList(list):
#     min=list[0]
#     for i in list:
#         if i<min:
#             min=i
#     return min

# print ("Type \"exit\" to stop:")
# gameon=True
# i=0
# list=[]
# while gameon:
#     x=input(f"Number {i+1} is: ")
#     i+=1
#     if x=="exit":
#         gameon=False
#     else:
#         list.append(int(x))
# print (f"Min is: {minList(list)}")

# -------------------------------------------------------------
# ---------------- Task 3 -------------------------------------
# -------------------------------------------------------------
# Write a function that determines how many prime numbers there are in the list of integers. 
# The list is passed as a parameter. The result is returned from the function.

# def checkPrime(x):
#     div=0
#     for i in range (2,x):
#         if x%i==0:
#             div+=1
#     if div==0 and x!=1: 
#         print(x)
#         return True
#     else:
#         return False

# def primeList(list):   
#     no=0
#     for x in list:
#        if checkPrime(x):
#            no+=1
#     return no

# print ("Type \"exit\" to stop:")
# gameon=True
# i=0
# list=[]
# while gameon:
#     x=input(f"Number {i+1} is: ")
#     i+=1
#     if x=="exit":
#         gameon=False
#     else:
#         list.append(int(x))
# print (f"Number of prime elements: {primeList(list)}")

# -------------------------------------------------------------
# ---------------- Task 4 -------------------------------------
# -------------------------------------------------------------
# Write a function that removes a given number from the list of integers. 
# Return the number of removed elements from the function.


# def eliminateFromList(list,removeX):   
#     no=0
#     for x in list:
#        if x==removeX:
#            list.remove(removeX)
#            no+=1
#     return no

# print ("Type \"exit\" to stop:")
# gameon=True
# i=0
# list=[]
# while gameon:
#     x=input(f"Number {i+1} is: ")
#     i+=1
#     if x=="exit":
#         gameon=False
#     else:
#         list.append(int(x))
# removeX=int(input("What number do you want to eliminated?"))
# print (f"Number of eliminated occurences of {removeX}: {eliminateFromList(list,removeX)}")

# -------------------------------------------------------------
# ---------------- Task 5 -------------------------------------
# -------------------------------------------------------------
# Write a function that takes two lists as a parameter and 
# returns a list containing the elements of both lists.

# def newList():
#     gameon=True
#     i=0
#     list=[]
#     while gameon:
#         x=input(f"Number {i+1} is: ")
#         i+=1
#         if x=="exit":
#             gameon=False
#         else:
#             list.append(int(x))
#     return list

# def commonElementsList(list1,list2):   
#     list3=[x for x in list1 if x in list2]
#     return list3

# def allElementsOnce(list1, list2):
#     list3=commonElementsList(list1,list2)
#     list4=[x for x in list1 if x not in list3]
#     list5=[x for x in list2 if x not in list3]
#     return list3+list4+list5

# def allElements(list1, list2):    
#     return list1+list2

# print ("Type \"exit\" to stop:")
# # list 1
# print ("First list:")
# list1=newList()
# # list 2
# print ("Second List:")
# list2=newList()
# # generate list with common elements
# print (f"List with common elements: {commonElementsList(list1,list2)}")
# print (f"List with all elements from both lists (one appearence): {allElementsOnce(list1, list2)}")
# print (f"List with all elements from both lists (all apearences):{allElements(list1,list2)}")

# -------------------------------------------------------------
# ---------------- Task 6 -------------------------------------
# -------------------------------------------------------------
# Write a function that calculates the power of each element from the list of integers. 
# A value for the power is passed as a parameter, the list is also passed as a parameter. 
# The function returns a new list containing the results.

def newList():
    gameon=True
    i=0
    list=[]
    while gameon:
        x=input(f"Number {i+1} is: ")
        i+=1
        if x=="exit":
            gameon=False
        else:
            list.append(int(x))
    return list

def powerOf(list,x):
    result=[i**x for i in list]
    return result

print ("Type \"exit\" to stop:")
# list 1
print ("List of numbers:")
list=newList()
# Raised at power
x=int(input("Raise these elements to the power of..."))

print(f"Your elements raised to the power of {x} are: {powerOf(list,x)}")




