# Task
# Two lists of integers are filled with random numbers. Do the following:

# task 1 = Create the third list containing elements of both lists;
# task 2 = Create the third list containing elements of both lists without repetitions;
# task 3 = Create the third list containing elements common to both lists;
# task 4 = Create the third list containing elements that are unique to each list;
# task 5 = Create the third list containing only the smallest and the largest values of each list.

from random import *

list1=[]
for i in range (randint(1,20)):
    list1.append(randint(0,50))

list2=[]
for i in range (randint(1,20)):
    list2.append(randint(0,50))

print(list1)
print(list2)



list1duplicate=list1
list2duplicate=list2
list1No=len(list1)
list2No=len(list2)
totalNo=list1No+list2No
randomTotal=randint(2,totalNo)

# the generated list
generatedList=[]

def task1():
    """Create the third list containing elements of both lists"""
    # interpretation: elements, not all elements. I'll use a random algorithm for this.
    
    focusList=randint(1,2) # use to alternate through the two lists
    generatedList=[]
    for i in range(1,randomTotal):
        if focusList==1: #take a random no from list1            
            index=randint(0,len(list1duplicate)-1)
            generatedList.append(list1duplicate[index])    
            focusList=2 #switch to list2
        else: #take a random no from list2
            index=randint(0,len(list2duplicate)-1)
            generatedList.append(list2duplicate[index])
            focusList=1 #switch to list1
    print(f"Task1 ({len(generatedList)} elements) = ",generatedList)

def task2():
    """Create the third list containing elements of both lists without repetitions"""
    # interpretation: elements, not all elements. I'll use a random algorithm for this.
    randomTotal=randint(2,totalNo)

    focusList=randint(1,2) # use to alternate through the two lists
    generatedList=[]
    for i in range(1,randomTotal):
        if focusList==1: #take a random no from list1
            if len(list1duplicate)>0:
                index=randint(0,len(list1duplicate)-1)
                generatedList.append(list1duplicate[index])
                list1duplicate.pop(index)
                # print("list1=",list1duplicate)
            else:
                focusList=2
                # i-=1 #din not add the element.
            focusList=2 #switch to list2
        else: #take a random no from list2
            if len(list2duplicate)>0:
                index=randint(0,len(list2duplicate)-1)
                generatedList.append(list2duplicate[index])
                list2duplicate.pop(index)
                # print("list2=",list2duplicate)
            else:
                focusList=1
                # i-=1 #din not add the element.
            focusList=1 #switch to list1
    print(f"Task2 ({len(generatedList)} elements) = ",generatedList)

def task3():
    """Create the third list containing elements common to both lists"""
    # interpretation: elements, not all elements. 
    # I'll take all the common elements.
    generatedList=[]
    for index in range(0,len(list1duplicate)): #looks in list1
        x=list1duplicate[index]
        if x in list2duplicate and x not in generatedList:            
            generatedList.append(x)

    for index in range(0,len(list2duplicate)): #looks in list2
        x=list2duplicate[index]
        if x in list1duplicate and x not in generatedList:            
            generatedList.append(x)            

    print(f"Task3 ({len(generatedList)} elements) = ",generatedList)

def task4():
    """Create the third list containing elements that are unique to each list"""
    # interpretation: elements, not all elements. 
    # unique to each list = don't exist in the other list
    generatedList=[]
    for index in range(0,len(list1duplicate)): #looks in list1
        x=list1duplicate[index]
        if x not in list2duplicate and x not in generatedList:            
            generatedList.append(x)

    for index in range(0,len(list2duplicate)): #looks in list2
        x=list2duplicate[index]
        if x not in list1duplicate and x not in generatedList:            
            generatedList.append(x)            

    print(f"Task4 ({len(generatedList)} elements) = ",generatedList)

def task5():
    """Create the third list containing only the smallest and the largest values of each list."""

    generatedList=[]
    min=list1duplicate[0]
    max=list1duplicate[0]
    for index in range(0,len(list1duplicate)): #looks in list1
        x=list1duplicate[index]
        if x<min:
            min=x
        if x>max:
            max=x
    generatedList.append(min)
    generatedList.append(max)

    min=list2duplicate[0]
    max=list2duplicate[0]
    for index in range(0,len(list2duplicate)): #looks in list2
        x=list2duplicate[index]
        if x<min:
            min=x
        if x>max:
            max=x
    generatedList.append(min)
    generatedList.append(max)            

    print(f"Task5 ({len(generatedList)} elements) = ",generatedList)

task1()
task2()
task3()
task4()
task5()