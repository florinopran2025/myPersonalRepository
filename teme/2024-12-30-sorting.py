# Task 1
# Sort the first two-thirds of the list in ascending order 
# if the arithmetic mean of all elements is greater than 0; 
# otherwise, sort only the first third. 
# The rest of the list is not sorted but arranged in reverse order.

# def sortList(numbers):
#     length=len(numbers)
#     print (length)
#     for i in range (0,length-1):
#         for j in range (i+1,length):
#             if numbers[i]>numbers[j]:
#                 # switch numbers
#                 x=numbers[i]
#                 numbers[i]=numbers[j]
#                 numbers[j]=x
#     return numbers

# def reverseOrder(numbers):
#     length=len(numbers)
#     for i in range (0,int(length/2)):
#         #switch numbers
#         # print (numbers[i],"<>",numbers[length-1-i])
#         x=numbers[i]
#         numbers[i]=numbers[length-1-i]
#         numbers[length-1-i]=x
#     return numbers

# def constructList(numberOfElements):
#     list=[0]*numberOfElements
#     for i in range(0,numberOfElements):
#         list[i]=int(input(f"No. {i} is: "))
#     return list


# list0=constructList(int(input("No of elements in your list: ")))
# print(list0)
# length=len(list0)

# # arithemetic mean
# mean=0
# for i in list0:
#     mean+=i
# mean=mean/(length-1)

# if mean>0:
#     splitPoint=(length/3)*2 # two thirds
# else:
#     splitPoint=length/3 #one third


# list1=[]
# list2=[]
# for i in range (0,length):
#     if i<splitPoint:
#         list1.append(list0[i])            
#     else:
#         list2.append(list0[i])
# list1=sortList(list1)
# list2=reverseOrder(list2)
# print(list1)
# print(list2)
# finalList=list1+list2
# print(f"Final result is:\n",finalList)

# ------------------------------------------------
# ------------- END OF TASK 1 --------------------
# ------------------------------------------------



# Task 2
# Create an app Progress. 
# The user inputs 10 grades that the student has got. 
# Grades range from 1 to 12. Implement a user menu:

# Output grades (output list contents);
# Retake exam (the user inputs an element number in the list and a new grade);
# Whether the student will get a scholarship (students receive a scholarship 
# if their average grade is at least 10.7);
# Output a sorted list of grades: in ascending or descending order.

# import os
# class Grades():
#     def __init__(self):
#         self.GRADES_ORDER=["Prima nota", "A doua nota:", "A treia nota", 
#                     "A patra nota", "A cincea nota", "A șasea nota",
#                     "A saptea nota", "A opta nota", "A noua nota",
#                     "Ultima nota"]
#         self.gradesList=[]
#     def basicMenu(self):   
#         os.system("cls")            
#         print("(tasta 1) Introdu notele. ")
#         print("(tasta 2) Printeaza notele. ")
#         print("(tasta 3) Repeta un examen. ")
#         print("(tasta 4) Verifica promovare")
#         print("(tasta 0) Parasire aplicatie")
#         raspuns=int(input("Optiunea ta:"))
#         if raspuns==1:
#             self.typeGrades()    
#         elif raspuns==2:
#             self.printGrades(4)
#         elif raspuns==3:
#             self.repeatExam() 
#         elif raspuns==4:
#             self.graduation()
#         else:
#             print("Ai parasit aplicatia. Succes!")   
#             exit()
#     def graduation(self):
#         medie=0
#         for i in range (0,10):            
#             medie+=self.gradesList[i]
#         medie=medie/10
#         if medie>=10.7:
#             print (f"Media ta este {medie}. Felicitari! Ai trecut.")        
#         else: 
#             print(f"Media ta este {medie}.")
#             raspuns=input("Vrei sa repeti un examen? (da/nu)")
#             if raspuns =="da":
#                 self.repeatExam()
#             else:
#                 self.printGrades(4)
#     def typeGrades(self):
#         os.system("cls")
#         for i in range(0,10):
#             grade="invalid"
#             while grade=="invalid":
#                 grade=int(input(f"{self.GRADES_ORDER[i]} a fost: "))
#                 if 1<=grade<=12:    
#                     self.gradesList.append(grade)                    
#                 else:
#                     print("Nota trebuie sa fie in intervalul 1-12.",end=" ")
#                     grade="invalid"
#         print("Notele au fost actualizate")
#         input("(click enter to continue)")
#         self.basicMenu()        
#     def repeatExam(self):
#         os.system("cls")        
#         raspuns=int(input("Ce examen vrei sa repeti? (0=exit to menu)"))
#         if raspuns==0:
#             self.basicMenu()
#         else:
#             grade="invalid"
#             while grade=="invalid":
#                 grade=int(input(f"{self.GRADES_ORDER[raspuns-1]} a fost: "))
#                 if 1<=grade<=12:    
#                     self.gradesList[raspuns-1]=grade
#                     self.basicMenu()
#                 else:
#                     print("Nota trebuie sa fie in intervalul 1-12.",end=" ")
#                     grade="invalid"
#         input("(click enter to continue)")
#         self.basicMenu()
#     def sortListAscending(self,grades):
#         length=len(grades)
#         print (length)
#         for i in range (0,length-1):
#             for j in range (i+1,length):
#                 if grades[i]>grades[j]:
#                     # switch numbers
#                     x=grades[i]
#                     grades[i]=grades[j]
#                     grades[j]=x
#         for i in range (0,10):
#             print(self.GRADES_ORDER[i], "a fost:", grades[i],".")
#     def sortListDescending(self,grades):
#         length=len(grades)
#         print (length)
#         for i in range (0,length-1):
#             for j in range (i+1,length):
#                 if grades[i]<grades[j]:
#                     # switch numbers
#                     x=grades[i]
#                     grades[i]=grades[j]
#                     grades[j]=x
#         for i in range (0,10):
#             print(self.GRADES_ORDER[i], "a fost:", grades[i],".")
#     def printGrades(self,option): 
#         os.system("cls")
#         if option==4: #standard
#             print("Meniu pentru afisarea notelor din Catalog:"
#                   "\nTasteaza 1 pentru afisarea in ordinea materiilor."
#                   "\nTasteaza 2 pentru afisarea in ordinea crescatoare a notelor."
#                   "\nTasteaza 3 pentru afisarea in ordinea descrescatoare a notelor."
#                   "\nTasteaza 0 pentru intoarcearea la meniul principal.")  
#             option=int(input("Optiunea ta este...")) 
#             self.printGrades(option)
#         elif option==0:
#             self.basicMenu()
#         elif option==1:    
#             print("C A T A L O G:") 
#             for i in range (0,10):
#                 print(self.GRADES_ORDER[i], "a fost:", self.gradesList[i],".")                
#             self.graduation()
#             input("(click enter to continue)")
#             self.printGrades(4)
#         elif option==2:
#             self.sortListAscending(self.gradesList)
#             self.graduation()
#             input("(click enter to continue)")
#             self.printGrades(4)
#         elif option==3:
#             self.sortListDescending(self.gradesList)
#             self.graduation()
#             input("(click enter to continue)")
#             self.printGrades(4)

# aplicatie=Grades()
# aplicatie.basicMenu()



# ------------------------------------------------
# ------------- END OF TASK 2 --------------------
# ------------------------------------------------


# Task 3
# Create an app that sorts a list using the advanced bubble sort. 
# The improvement is to analyze the number of swaps at each step; 
# if this number is equal to 0, there is no point in continuing sorting — 
# the list has been sorted.

# theList=[222, 111, 99, 88, 77, 66, 55, 44, 33, 22, 11, 7]
# length=len(theList)

# def swap(a,b):
#     global theList
#     temp =theList[a]
#     theList[a]=theList[b]
#     theList[b]=temp

# swaps=1
# while swaps!=0:
#     swaps=0
#     for i in range(0,length-1):
#         if theList[i]>theList[i+1]:
#             swap(i,i+1)
#             swaps+=1
#     print(f"No of swaps={swaps}")
# print(theList)

# ------------------------------------------------
# ------------- END OF TASK 3 --------------------
# ------------------------------------------------

