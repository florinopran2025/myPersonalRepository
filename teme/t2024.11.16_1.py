# Task 1
# The user types in the size of the square's sides. 
# Print a solid square. The size is equal to the typed in square's side. 
# Say the user typed in 3, the output will be as follows:

# size=int(input("Computer:What's the size of the square? \nYou:"))
# length=0
# width=0
# while length<size:    
#     while width<size: #printer machine
#         print("*",end="")
#         width+=1
#     width=0 #reset the printer machine
#     print() #go to the next line, in order to resume printing
#     length+=1

# Task 2
# The user types in the width and height of a rectangle. 
# Print a solid rectangle of the specified height and width. 
# Say the user typed in the height equal to 3, and width 5, 
# the output should be as follows:

# height=int(input("Computer:What's the height of the rectangle? \nYou:"))
# width=int(input("Computer:What's the width of the rectangle? \nYou:"))
# h=0
# w=0
# while h<height:    
#     while w<width: #printer machine
#         print("*",end="")
#         w+=1
#     w=0 #reset the printer machine
#     print() #go to the next line, in order to resume printing
#     h+=1

# Task 3
# The user types in the size of the square's sides. 
# Print an empty square (only its sides are displayed). 
# The side is equal to the typed in size.

# size=int(input("Computer:What's the size of the square? \nYou:"))
# height=0
# width=0
# while height<size:    
#     while width<size: #printer machine
#         if (width>0 and width<size-1) and (height>0 and height<size-1):
#             print(" ",end="")
#         else:
#             print ("*",end="")
#         width+=1
#     width=0 #reset the printer machine
#     print() #go to the next line, in order to resume printing
#     height+=1

# Task 4
# The user types in the length and width of a rectangle. 
# Print an empty rectangle (only its sides are displayed). 
# The length and width are equal to the typed in numbers.

length=int(input("Computer:What's the length of the rectangle? \nYou:"))
width=int(input("Computer:What's the width of the rectangle? \nYou:"))
l=0
w=0
while l<length:    
    while w<width: #printer machine
        
        if (w>0 and w<width-1) and (l>0 and l<length-1):
            print(" ",end="")
        else:
            print ("*",end="")
        w+=1
    w=0 #reset the printer machine
    print() #go to the next line, in order to resume printing
    l+=1