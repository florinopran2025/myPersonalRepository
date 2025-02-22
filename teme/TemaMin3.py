# CALCULATE THE MINIMUM OF 3 NUMBERS

#SOLUTION 1
# a=input("a=")
# b=input("b=")
# c=input("c=")

# if a<b:
#     if a<c:
#         min=a
#     else:
#         min=c
# else:
#     if b<c:
#         min=b
#     else:
#         min=c

# print("Minimum from",a,",",b,",",c," este",min)

# #SOLUTION 2
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))

# def findMin(x,y):
#     if x<y:
#         return x
#     else:
#         return y

# min=findMin(a,b)
# min=findMin(min,c)
# print("Minimum from",a,",",b,",",c," este",min)

#SOLUTION 3
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=int(input("d="))
# e=int(input("e="))

# def findMin(x,y):
#     if x<y:
#         return x
#     else:
#         return y

# min=findMin(a,b)
# min=findMin(min,c)
# min=findMin(min,d)
# min=findMin(min,e)
# print(f"Minimum from {a},{b},{c},{d},{e} is {min}")

# SOLUTION 4
# def findMin(x,y):
#     if x<y:
#         return x
#     else:
#         return y
# stringX=input("List of numbers (separated by comma):")
# listX=stringX.split(",")
# listX=[int(i) for i in listX]

# min=listX[0]
# i=1
# while i<len(listX):
#     min=findMin(min,listX[i])
#     i+=1
# print(f"Min from {stringX} is {min}.")

