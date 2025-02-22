# size=int(input("Computer:What's the size of the square? \nYou:"))
size=5

#concept:
#exista 4 structuri importante:
# A=\up         condition   x>=y
# B=down\       condition   x<=y
# I=up/         condition   x<=size-1-y
# J=/down       condition   x>=size-1-y
#restul sunt structuri derivate de 2 sau 4 conditii


def conditions(id,x,y,size):    
    if id=="a":     #figure A "\up"
        if x>=y:
            print ("*",end="")
        else:
            print(" ",end="")
    if id=="b":     #figure B "down\"
        if x<=y:
            print ("*",end="")
        else:
            print(" ",end="")
    if id=="i":       #figure I up/
        if x<=size-1-y:
            print ("*",end="")
        else:
            print(" ",end="")
    if id=="j":       #figure J /down
        if x>=size-1-y:
            print ("*",end="")
        else:
            print(" ",end="")

    if id=="c":       #figure C "\up" and up/
        if (x>=y) and (x<=size-1-y):
            print ("*",end="")
        else:
            print(" ",end="")
    if id=="d":       #figure d /down and down\
        if (x<=y) and (x>=size-1-y):
            print ("*",end="")
        else:
            print(" ",end="")
    if id=="e":       # conditiile de la c sau cele de la d
        if ((x>=y) and (x<=size-1-y)) or ((x<=y) and (x>=size-1-y)):
            print ("*",end="")
        else:
            print(" ",end="")

    if id=="g":       #figure C conditiile de la b si i
        if (x<=y) and (x<=size-1-y):
            print ("*",end="")
        else:
            print(" ",end="")
    if id=="h":       #figure d conditiile de la a si j
        if (x>=y) and (x>=size-1-y):
            print ("*",end="")
        else:
            print(" ",end="")
    if id=="f":       # figure f conditiile de  la g SAU conditiile de la h
        if ((x<=y) and (x<=size-1-y)) or ((x>=y) and (x>=size-1-y)):
            print ("*",end="")
        else:
            print(" ",end="")


def figure(id,size): # diagonal \up
    # FIGURE 1 (A)
    # separation diagonal:  x=y
    # condition: x>y
    y=0
    x=0
    while y<size:    
        while x<size: #printer machine
            conditions(id,x,y,size)  
            x+=1
        x=0 #reset the printer machine
        print() #go to the next line, in order to resume printing
        y+=1

size=0
while size<5:
    size=int(input("Set the size:"))
    if size>=5:
        gameOn=True
    else:
        print("Size should be at least 5.\n"
              "Please set a valid number.")
        
while gameOn:
    string=input("Computer: What is the figure that you want me to show you?\n"
                 "Type exit if you want to exit the game.\nYou: ")
    if string!="exit":
        figure(string,size)
    else:
        print("Hope you enjoyed the game. Please come back again.")
        gameOn=False
    

