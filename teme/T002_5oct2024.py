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


def customSplit(com, operator):
    result=[]    
    splitList=com.split(operator)    
    for i in range (len(splitList)):  
        result.append(splitList[i])                
        if operator=="/":            
            print(f"customSplit pe * from {splitList[i]}")
            splitList[i]=customSplit(splitList[i],"*")
            result[-1]=splitList[i]
            if i<len(splitList)-1:
                result.append(operator)
        elif operator=="*":            
            print(f"customSplit pe + from {splitList[i]}")
            splitList[i]=customSplit(splitList[i],"+")
            result[-1]=splitList[i]
            if i<len(splitList)-1:
                result.append(operator)
        elif operator=="+":            
            print(f"customSplit pe - from {splitList[i]}")
            splitList[i]=customSplit(splitList[i],"-")
            result[-1]=splitList[i]
            if i<len(splitList)-1:
                result.append(operator)

        if i<len(splitList)-1:
                result.append(operator)    
        
    return result

def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            # Recursively flatten the inner list
            flat_list.extend(flatten_list(item))
        else:
            # Add the element if it's not a list
            flat_list.append(item)
    return flat_list

def elimDupOpp(list):
    for i in range(len(list)):
        x=list[i]
        if list[i]==list[i-1] and (x=="/" or x=="*" or x=="+" or x=="-"):
            print(list[i],list[i-1])
            del list[i]
            elimDupOpp(list)
    return list


# def splitAll(com):
#     result=[]
#     splitDivide=com.split("/")    
#     for i in range (len(splitDivide)):
#         arrDiv=customSplit(splitDivide,*)



#         splitDivide[i]=splitDivide
#         result.append(splitDivide[i])  
#         result.append("/")
#     temp=[]
#     for e in range(len(com)):        
#         SplitMultiply=com[e].split("*")  
#         print(SplitMultiply)  
#         for i in range (len(SplitMultiply)):
#             temp.append(SplitMultiply[i])  
#             temp.append("*")
#         result.append(temp)        
#     return result



com=input("Type your command: ")

# arr=arrSplitDivide(commandFromUser)
# arr=arrSplitMultiply(arr)
# arr=arrSplitPlus(arr)
# arr=arrSplitMinus(arr)
arr=customSplit("1+2+3/4*5-6+7/8*9","/")
print(arr)
arr=flatten_list(arr)
print(arr)
arr=elimDupOpp(arr)
print(arr)

