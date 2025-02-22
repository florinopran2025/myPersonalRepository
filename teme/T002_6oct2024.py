# VARIANTA 1
# no1=int(input("First number: "))
# no2=int(input("Second number: "))
# no3=int(input("Third number: "))
# sum=no1+no2+no3
# print(no1,"+",no2,"+",no3,"=",sum)



# VARIANTA 2
# print("\n-----------\n Adding numbers.",
#       "When you're ready for the grand total,",
#        "just type \'=\'")

# no=0
# sum=0

# while no!="=":    
#     no=input ("Add number (type = for the result)> ")
#     if no!="=":
#         sum+=int(no)
#     print ("Intermediate Sum is...",sum,". Type \'=\' for the final result.")
    
# print("Final result is...",sum)    

# VARIANTA 3
# def addGame(a):
#     splitted=a.split("+")
#     total=sum(int(element) for element in splitted)
#     return total
# commandFromUser=input("Type your command: ")
# print(commandFromUser, "is", addGame(commandFromUser))


# VARIANTA 4
# math order: / , *, +, -


def customSplit(initial, operator):
    result=[]
    for i in range(len(initial)):        
        element=initial[i]
        if element=="/" or element=="*" or element=="+" or element=="-":
            result.append(element)
        splitList=initial[i].split(operator)    
        for a in range (len(splitList)):          
            result.append(splitList[a])  
            if a<len(splitList)-1:                
                result.append(operator)      
     
    if operator=="/":
        switchOp="*"
    elif operator=="*":
        switchOp="+"
    elif operator=="+":
        switchOp="-"
    elif operator=="-":
        switchOp="stop"

    if switchOp!="stop":
        result=customSplit(result,switchOp)
    else:
        result=cleanList(result)

    return result

def cleanList(result):
    i=0
    while i<len(result)-1:
        # print("i=",i,"-",result[i])
        element=result[i]        
        if element in ("/","*","+","-") and element==result[i+1]:
            del result[i]
            cleanList(result)
        i+=1
    return result

    
def divide(a,b):
    a=float(a)
    b=float(b)
    return a/b

def multiply(a,b):
    a=float(a)
    b=float(b)
    return a*b

def add(a,b):
    a=float(a)
    b=float(b)
    return a+b

def substract(a,b):
    a=float(a)
    b=float(b)
    return a-b

def calcul(result):
    if len(result)<3:
        print ("exit",len(result), result[0])
        return result[0]
    
    i=0
    while i<len(result)-2:                  
        if result[i+1]=="/":
            result[i]=divide(result[i],result[i+2])
            del result[i+2]
            del result[i+1]
            print(result)
            calcul(result)
        i+=1
    i=0
    while i<len(result)-2:
        if result[i+1]=="*":
            result[i]=multiply(result[i],result[i+2])
            del result[i+2]
            del result[i+1]
            print(result)
            calcul(result)
        i+=1
    i=0
    while i<len(result)-2: 
        if result[i+1]=="-":
            result[i]=substract(result[i],result[i+2])
            del result[i+2]
            del result[i+1]
            print(result)
            calcul(result)
        i+=1
    i=0
    while i<len(result)-2:
    
        print (i)
        if result[i+1]=="+":
            result[i]=add(result[i],result[i+2])
            del result[i+2]
            del result[i+1]
            print(result)
            calcul(result)
        i+=1

    return result[0]

comanda=input("Calculate (only / * + -):  ")
result=customSplit([comanda],"/")
print(result)
finalResult=calcul(result)
print("Rezultatul final este... ",finalResult)


