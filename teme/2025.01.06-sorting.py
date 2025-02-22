# Task 1
# Write an app Reference Book. 
# Create two lists of integers. 
# One list stores identification codes, 
# the second phone numbers. 
# Implement a user menu:
# (1) Sort by id codes;
# (2) Sort by phone numbers;
# (3) Output a list of users with codes and phone numbers;
# (4) Exit.

import os
# Concept: listCodes= badge numbers (unique to each phone no =>unique identification)
listCodes=[2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
listPhones=[751146902, 751146901, 751146903, 751146904, 751146905, 
            751146906, 751146907, 751146908, 751146909, 751146910]



def mainOptions(level):    
    os.system('cls')
    if level=="0":
        print("Option 1 - Sort by ID"
            "\nOption 2 - Sort by phone"
            "\nOption 3 - Print contacts"
            "\nOption 4 - Exit")    
    if level=="12": # level 1, option 2
        print("Option 1 - Sort in ascending order of phones"
            "\nOption 2 - Sort in descending order of phones"
            "\nOption 3 - Print contacts"
            "\nOption 4 - Go back"
            "\nOption 5 - Force exit"
            )  
        
def sortList(list1,order):
    #concept: order both list at the same time
    global listCodes,listPhones #modify bost lists
    startFrom=list1
    if list1==listCodes:
        list2=listPhones
    else:
        list2=listCodes
    length=len(list1)
    if order=="ascending":
        for i in range (0,length-1):
            for j in range (i+1, length):
                if list1[i]>list1[j]:
                    #order list1
                    temp=list1[i]
                    list1[i]=list1[j]
                    list1[j]=temp
                    #order list2
                    temp=list2[i]
                    list2[i]=list2[j]
                    list2[j]=temp
    else: #descending order
        for i in range (0,length-1):
            for j in range (i+1, length):
                if list1[i]<list1[j]:
                    #order list1
                    temp=list1[i]
                    list1[i]=list1[j]
                    list1[j]=temp
                    #order list2
                    temp=list2[i]
                    list2[i]=list2[j]
                    list2[j]=temp
    if startFrom==listCodes:
        listCodes=list1
        listPhones=list2        
    else:
        listCodes=list2
        listPhones=list1


def printContacts():
    length=len(listCodes)
    print ("These are all you Contacts:")
    for i in range (0,length):
        print(f"Contact with id {listCodes[i]}: 0{listPhones[i]}")


inApp=True
menuLevel="0" # starts from mainOptions 
while inApp:     
    mainOptions(menuLevel)  
    option=input("What do you want to do?")
    if menuLevel=="0":
        if option=="1": #sort by id (ascending)
            sortList(listCodes,"ascending")
            input ("DONE!\nClick on anything to continue!")
        elif option =="2": #sort by phone
            menuLevel="12"            
        elif option=="3": #print contacts
            printContacts()
            input ("DONE!\nClick on anything to continue!")
        elif option =="4": #exit App
            inApp=False
    if menuLevel=="12": # submenu for "sort by phone"
        if option=="1": # sort by phone (ascending)
            sortList(listPhones,"ascending")
            input ("DONE!\nClick on anything to continue!")
        if option=="2": # sort by phone (descending)
           sortList(listPhones,"descending")
           input ("DONE!\nClick on anything to continue!")
        if option=="3": # print
            printContacts()
            input ("Click on anything to continue!")
        if option=="4": # go back to menu level 0
            menuLevel="0"
            input (f"DONE!\nClick on anything to continue!")
        if option=="5": # exit App
            inApp=False


# ---------------------------------------------------------------
# ------------------------ TASK 2 -------------------------------
# ---------------------------------------------------------------


# Task 2
# Write an app Book. Create two lists of data. 
# One list stores a title, 
# the second a year of release. 
# Implement a user menu:
# (1) Sort by title;
# (2) Sort by year of release;
# (3) Output a list of books with titles and years of release;
# (4) Exit.

# import os
# # Concept: two related lists: listBooks & listYears
# listBooks=[
#     "Pride and Prejudice", 
#     "1984", 
#     "Moby-Dick", 
#     "To Kill a Mockingbird", 
#     "War and Peace", 
#     "Great Expectations", 
#     "The Great Gatsby", 
#     "Crime and Punishment", 
#     "Jane Eyre", 
#     "The Catcher in the Rye"
# ] 
# listYears=[    
#     1813,  # Pride and Prejudice
#     1949,  # 1984
#     1851,  # Moby-Dick
#     1960,  # To Kill a Mockingbird
#     1869,  # War and Peace
#     1861,  # Great Expectations
#     1925,  # The Great Gatsby
#     1866,  # Crime and Punishment
#     1847,  # Jane Eyre
#     1951   # The Catcher in the Rye
#     ]

# def mainOptions(level):    
#     os.system('cls')
#     if level=="0":
#         print("Option 1 - Sort by Title"
#             "\nOption 2 - Sort by Year"
#             "\nOption 3 - Print books"
#             "\nOption 4 - Exit")    
#     if level=="12": # level 1, option 2
#         print("Option 1 - Sort in ascending order of Year"
#             "\nOption 2 - Sort in descending order of Year"
#             "\nOption 3 - Print books"
#             "\nOption 4 - Go back"
#             "\nOption 5 - Force exit"
#             )  
        
# def sortList(list1,order):
#     #concept: order both list at the same time
#     global listBooks,listYears #modify bost lists
#     start=list1
#     if list1==listBooks:
#         list2=listYears
#     else:
#         list2=listBooks
#     length=len(list1)
#     if order=="ascending":
#         for i in range (0,length-1):
#             for j in range (i+1, length):
#                 if list1[i]>list1[j]:
#                     #order list1
#                     temp=list1[i]
#                     list1[i]=list1[j]
#                     list1[j]=temp
#                     #order list2
#                     temp=list2[i]
#                     list2[i]=list2[j]
#                     list2[j]=temp
#     else: #descending order
#         for i in range (0,length-1):
#             for j in range (i+1, length):
#                 if list1[i]<list1[j]:
#                     #order list1
#                     temp=list1[i]
#                     list1[i]=list1[j]
#                     list1[j]=temp
#                     #order list2
#                     temp=list2[i]
#                     list2[i]=list2[j]
#                     list2[j]=temp
#     if start==listBooks:
#         listBooks=list1
#         listYears=list2
#     else:
#         listBooks=list2
#         listYears=list1
        


# def printTitles():
#     length=len(listBooks)
#     print ("These are all your books:")
#     for i in range (0,length):
#         print(f"{listBooks[i]} was release in {listYears[i]}.")


# inApp=True
# menuLevel="0" # starts from mainOptions 
# while inApp:     
#     mainOptions(menuLevel)  
#     option=input("What do you want to do?")
#     if menuLevel=="0":
#         if option=="1": #sort by book (ascending)
#             sortList(listBooks,"ascending")
#             input ("DONE!\nClick on anything to continue!")
#         elif option =="2": #sort by year
#             menuLevel="12"            
#         elif option=="3": #print titles
#             printTitles()
#             input ("DONE!\nClick on anything to continue!")
#         elif option =="4": #exit App
#             inApp=False
#     if menuLevel=="12": # submenu for "sort by year"
#         if option=="1": # sort by year (ascending)
#             sortList(listYears,"ascending")
#             input ("DONE!\nClick on anything to continue!")
#         if option=="2": # sort by year (descending)
#            sortList(listYears,"descending")
#            input ("DONE!\nClick on anything to continue!")
#         if option=="3": # print
#             printTitles()
#             input ("Click on anything to continue!")
#         if option=="4": # go back to menu level 0
#             menuLevel="0"
#             input (f"DONE!\nClick on anything to continue!")
#         if option=="5": # exit App
#             inApp=False
