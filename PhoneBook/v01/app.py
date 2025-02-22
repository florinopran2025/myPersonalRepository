import os


# ----------------------------------------------------
# ------ CONSTANTS and variable INITIALIZATION -------
fileMenu=open("C:\\_FILES\\Programare\\Python\\Curs\\apps\\2025_01_phonebook\\file.menu","r")
englishDict={}
romanianDict={}
for row in fileMenu:
    if row.startswith("englishDict") or row.startswith("romanianDict"):
        row=row.strip()
        (language,no,opt)=row.split("=",maxsplit=2)
        if language=="englishDict":
            englishDict[int(no)]=opt 
        else:
            romanianDict[int(no)]=opt   
fileMenu.close()
MENU ={
    "english": englishDict,
    "romanian": romanianDict
}

names=[]
phones=[]
emails=[]
gameon=True
lang="english"
opt=0     

# ----------------------------------------------------
# ---------------- GENERAL METHODS -------------------
# USED BY THE MAIN METHODS 
def switchContacts(i,j):
    #names
    aux=names[i]
    names[i]=names[j]
    names[j]=aux
    #phones
    aux=phones[i]
    phones[i]=phones[j]
    phones[j]=aux
    #emails
    aux=emails[i]
    emails[i]=emails[j]
    emails[j]=aux

def continueGame():
    input("Press ENTER to continue...")


def searchByContactName(nameSearched):
    foundIt=False
    for i in range (0,len(names)):
        if nameSearched==names[i]:
            print(f"{names[i]} has the number: {phones[i]}")
            foundIt=True
    if foundIt==False:
        print(f"You dont' have {nameSearched}\'s number.")

# ----------------------------------------------------
# --------------------- MENU -------------------------
def displayMenu(lang):
    os.system('cls')
    print("--- --- MENU --- ---")
    for key, value in MENU[lang].items():
        print (f"{value}".ljust(2),"      (type",key,")".ljust(20))
    print()


# ----------------------------------------------------
# --------------------- MENU OPTIONS -----------------

# 1 = DISPLAY CONTACTS
def optDisplayContacts():    
    print("Total number of contacts:",len(names))
    for i in range (0,len(names)):
        print (f"{i+1}.  {names[i]}\'s phone is {phones[i]}. \nYou can reach him/her at {emails[i]}.")
    

# 2 = SEARCH CONTACT (BY NAME)
def optSearchContact():
    nameSearched=input("Name of contact?")
    searchByContactName(nameSearched)

# 3 = SORT CONTACTS
def optSortContacts():
    optLoadContacts()    
    length=len(names)
    for i in range (0,length-1):
        for j in range (i+1,length):
            if names[i]>names[j]:
                switchContacts(i,j)
    optSaveContacts()
    print ("The list was successfully sorted. Here it is:")
    optDisplayContacts()


# 4 = ADD CONTACT
def optAddContact():
    contactName=input("Name:")
    contactPhone=input("Phone:")
    names.append(contactName)
    phones.append(contactPhone)
    print(f"You've successfully added {contactName} in your phone book.")

# 5 = SAVE CONTACTS
def optSaveContacts():
    file=open("C:\\_FILES\\Programare\\Python\\Curs\\apps\\2025_01_phonebook\\phonebook_v01.csv",'w')
    for i in range (0,len(names)):        
        file.write(f"{names[i]},{phones[i]},{emails[i]}")
        file.write("\n")
    print(names)
    print(phones)
    print(emails)
    file.close()

# 6 = LOAD CONTACTS
def optLoadContacts():
    global names,phones,emails
    names=[]
    phones=[]
    emails=[]
    file=open("C:\\_FILES\\Programare\\Python\\Curs\\apps\\2025_01_phonebook\\phonebook_v01.csv",'r')
    numberOfContacts=0
    for line in file:
        numberOfContacts+=1
        line=line.strip()
        nameOnEachLine,phoneOnEachLine,emailOnEachLine=line.split(",")
        names.append(nameOnEachLine)
        phones.append(phoneOnEachLine)
        emails.append(emailOnEachLine)
    print ("You've successfully loaded",numberOfContacts,"contacts.")    
    file.close()

# 7 = SWITCH LANGUATE
def optSwitchLanguage(lang):
    if lang=="english":
        return "romanian"
    else:
        return "english"

# WRONG COMMAND
def optStrange():
    print ("Nu such option in the menu.😒")




# names=["Andreea", "Marius", "Valeriu"]
# phones=["0751.100.666","0751.200.666","0751.300.666"]
# emails=["andreea@yahoo.com","marius@gmail.com","valeriu@hotmail.com"]


while gameon:    
    displayMenu(lang)
    opt=int(input("What do you want?"))
    if opt==1: # display contacts
        optDisplayContacts()        
    elif opt==2: # search contact
        optSearchContact()
    elif opt==3: # sort contacts
        optSortContacts()
    elif opt==4: # add contact
        optAddContact()
    elif opt==5: # save contacts
        optSaveContacts()
    elif opt==6: # load contacts
        optLoadContacts()
    elif opt==7: # switch language
        lang=optSwitchLanguage(lang)
    elif opt==0: # exit
        gameon=False    
    else: # unrecognised option
        optStrange()
    continueGame()
    
