# TASK 1
# The user types in three numbers. 
# The program prints the sum or product 
# of these numbers based on the user's choice.

# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# opt=input("What do you want? (min/product)")

# def findMin(x,y):
#     if x<y:
#         return x
#     else:
#         return y

# def product(x,y,z):
#     return x*y*z

# if opt=="min":
#     min=findMin(a,b)
#     min=findMin(min,c)
#     print("Minimum from",a,",",b,",",c," is",min)
# if opt=="product":
#     print("Product of",a,",",b,",",c," esiste",product(a,b,c))



# Task 2
# The user types in three numbers. 
# Based on the user's choice, 
# the program prints a maximum of three, 
# a minimum of three, or arithmetic mean of three numbers.

# def findMin(x,y):
#     if x<y:
#         return x
#     else:
#         return y

# def findMax(x,y):
#     if x>y:
#         return x
#     else:
#         return y

# def mean(x,y,z):
#     return (x+y+z)/3

# gameOn=True
# while gameOn:
#     a=int(input("a="))
#     b=int(input("b="))
#     c=int(input("c="))
#     opt=input("What do you want? (min/max/mean/exit)")
#     if opt=="exit":
#         gameOn=False
#     if opt=="min":
#         min=findMin(a,b)
#         min=findMin(min,c)
#         print("Minimum from",a,",",b,",",c," is",min)
#     if opt=="max":
#         max=findMax(a,b)
#         max=findMax(max,c)
#         print("Maximum from",a,",",b,",",c," is",max)
#     if opt=="mean":
#         print("Product of",a,",",b,",",c," esiste",mean(a,b,c))

# Task 3
# The user types in the number of meters. 
# Based on the user's choice, 
# the program converts meters to miles, inches, or yards
mToMiles=0.000621371192
mToInches=39.3700787
mToYards=1.0936133
def convertor(distance,opt):
    if opt=="miles":
        return distance*mToMiles
    if opt=="inches":
        return distance*mToInches
    if opt=="yards":
        return distance*mToYards
gameOn=True
while gameOn:
    opt=input("In what do you want to convert your distance?(miles/inches/yards/exit)")
    if opt=="exit":
        print("Come back when you need to convert distances.")
        exit()
    m=int(input("What is your distance in meters?"))
    print(f"{m} meters = {convertor(m,opt)} {opt}")
    