# size=int(input("Computer:What's the size of the square? \nYou:"))
size=10

#concept:
#exista 4 structuri importante:
# A=\up         condition   x>=y
# B=down\       condition   x<=y
# I=up/         condition   x<=size-1-y
# J=/down       condition   x>=size-1-y
#restul sunt structuri derivate:

def conditions(x,y,condition):
    if condition=="\up":
        if x>=y:
                print ("*",end="")

def figureA(size): # diagonal \up
    # FIGURE 1 (A)
    # separation diagonal:  x=y
    # condition: x>y
    y=0
    x=0
    while y<size:    
        while x<size: #printer machine
            if x>=y:
                print ("*",end="")            
            # else:
            #     print(" ",end="")
                
            x+=1
        x=0 #reset the printer machine
        print() #go to the next line, in order to resume printing
        y+=1

def figureB(size): # diagonal down\
    # FIGURE 1 (A)
    # separation diagonal:  x=y
    # condition: x<=y
    y=0
    x=0
    while y<size:    
        while x<size: #printer machine
            if x<=y:
                print ("*",end="")            
            else:
                print(" ",end="")
                
            x+=1
        x=0 #reset the printer machine
        print() #go to the next line, in order to resume printing
        y+=1

def figureC(size): # diagonal \up and up/
    # FIGURE 1 (A)
    # separation diagonal:  x=y
    # condition: x<=y
    y=0
    x=0
    while y<size:    
        while x<size: #printer machine
            if x<=y:
                print ("*",end="")            
            else:
                print(" ",end="")
                
            x+=1
        x=0 #reset the printer machine
        print() #go to the next line, in order to resume printing
        y+=1


def figureI(size): # diagonal up/
    # FIGURE (I)
    # separation diagonal:  x=size-(y+1)
    # condition: x<=size-(y+1)
    y=0
    x=0
    while y<size:    
        while x<size: #printer machine
            if x<=size-1-y:
                print ("*",end="")            
            else:
                print("-",end="")
                
            x+=1
        x=0 #reset the printer machine
        print() #go to the next line, in order to resume printing
        y+=1

def figureJ(size): # diagonal /down
    # FIGURE 1 (B)
    # separation diagonal:  x=size-(y+1)
    # condition: x>=size-(y+1)
    y=0
    x=0
    while y<size:    
        while x<size: #printer machine
            if x>=size-1-y:
                print ("*",end="")            
            else:
                print("-",end="")
                
            x+=1
        x=0 #reset the printer machine
        print() #go to the next line, in order to resume printing
        y+=1



figureA(5)