# Task 1
# The user types in two numbers. 
# Print all the numbers in the specified range.

# a=int(input("a="))
# b=int(input("b="))
# min=0
# max=0
# if a>b:
#     max=a
#     min=b
# elif b>a:
#     max=b
#     min=a
# else:
#     print(a)

# if min!=max:
#     while min!=max+1:
#         print(min)
#         min+=1


# Task 2
# The user types in two numbers. 
# Print all odd numbers in the specified range.

# a=input("Type two numbers (separated by space):")
# a=a.split(" ")
# a=[int(i) for i in a]
# for i in range (min(a), max(a)+1):
#     if i%2==1:
#         print (i)

# Task 3
# The user types in two numbers. 
# Print all even numbers in the specified range.

# a=input("Type two numbers (separated by space):")
# a=a.split(" ")
# a=[int(i) for i in a]
# for i in range (min(a), max(a)+1):
#     if i%2==0:
#         print (i)

# Task 4
# The user types in two numbers. 
# Print all numbers in the specified range in descending order.

# a=int(input("Type a value for a:"))
# b=int(input("Type a value for b:"))
# min=min(a,b)
# max=max(a,b)
# if min==max:
#     print(min)
# else:
#     while max!=min:
#         print (max)
#         max-=1
#     print (max)


# Task 5
# The user types in two numbers. 
# Print all odd numbers in the specified range. 
# If the end and start points of the range are incorrect, normalize them. 
# Let's say the user typed in 33 and 13, 
# normalization will assign 13 to the start and 33 to the end of the range.

a=int(input("Type a value for a:"))
b=int(input("Type a value for b:"))
min=min(a,b)
max=max(a,b)
list=[]
if min==max:
    print(min)
else:
    while max!=min:
        if max%2==1:
            list.append(max)
        max-=1
    if max%2==1:
        list.append(max)
if list[0]>list[len(list)-1]:
    x=list[0]
    list[0]=list[len(list)-1]
    list[len(list)-1]=x

for i in list:
    print(i)
