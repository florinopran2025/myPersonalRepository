# CONCEPT:
# LOAD/SAVE CONTACTS TO/FROM FILE
# When you add a contact, you only have it in your local memory


import os

thePath=os.path.abspath(__file__)
theDir =os.path.dirname(thePath)+"\\"

# ----------------------------------------------------
# ------ CONSTANTS and variable INITIALIZATION -------

fileMenu=open(theDir+"file.menu","r")
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
WARNING_MESSAGE=("Important: Contacts are available only in the current session.\n"
                    "Don't forge to save your contacts to cloud.")   

# ----------------------------------------------------
# ---------------- GENERAL METHODS -------------------
# USED BY THE MAIN METHODS 
def switchContacts(i,j):
    """Switch two contacts method."""
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
    """Search by name method."""
    foundIt=False
    for i in range (0,len(names)):
        if nameSearched.lower()==names[i].lower():
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
        print (f"{key}. {value}")
    print()


# ----------------------------------------------------
# --------------------- MENU OPTIONS -----------------

# 1 = DISPLAY CONTACTS
def optDisplayContacts():    
    print("Total number of contacts:",len(names))
    for i in range (0,len(names)):
        print (f"{i+1}.  {names[i]}\'s phone is {phones[i]}. \n"
               f"You can reach him/her at {emails[i]}.")
# 2 = SEARCH CONTACT (BY NAME)
def optSearchContact():
    nameSearched=input("Name of contact?")
    searchByContactName(nameSearched)
# 3 = SORT CONTACTS
def optSortContacts():
    # optLoadContacts()    
    length=len(names)
    for i in range (0,length-1):
        for j in range (i+1,length):
            if names[i]>names[j]:
                switchContacts(i,j)    
    print ("The list was successfully sorted. Here it is:")
    optDisplayContacts()
# 4 = ADD CONTACT
def optAddContact():
    contactName=input("Name:")
    contactPhone=input("Phone:")
    contactEmail=input("Email:")
    names.append(contactName)
    phones.append(contactPhone)
    emails.append(contactEmail)
    print(f"You've successfully added {contactName} in your phone book.")    
    print (WARNING_MESSAGE)
# 5 = SAVE CONTACTS
def optSaveContacts():
    file=open(theDir+"phonebook_v01.csv",'w')
    for i in range (0,len(names)):        
        file.write(f"{names[i]},{phones[i]},{emails[i]}")
        file.write("\n")
    file.close()
# 6 = LOAD CONTACTS
def optLoadContacts():
    global names,phones,emails
    names=[]
    phones=[]
    emails=[]
    file=open(theDir+"phonebook_v01.csv",'r')
    numberOfContacts=0
    for line in file:
        numberOfContacts+=1
        line=line.strip()
        print(line)
        nameOnEachLine,phoneOnEachLine,emailOnEachLine=line.split(",")
        names.append(nameOnEachLine)
        phones.append(phoneOnEachLine)
        emails.append(emailOnEachLine)
    print ("You've successfully loaded",numberOfContacts,"contacts.")    
    file.close()
# 7 = SWITCH LANGUAGE
def optSwitchLanguage(lang):
    if lang=="english":
        return "romanian"
    else:
        return "english"
# WRONG COMMAND
def optUnknown():
    print ("Nu such option in the menu.😒")

while gameon:    
    displayMenu(lang)
    opt=int(input("What do you want?"))
    if opt==1: # display contacts
        optDisplayContacts()  
        continueGame()      
    elif opt==2: # search contact
        optSearchContact()
        continueGame()
    elif opt==3: # sort contacts
        optSortContacts()
        continueGame()
    elif opt==4: # add contact
        optAddContact()
        continueGame()
    elif opt==5: # save contacts
        optSaveContacts()
        continueGame()
    elif opt==6: # load contacts
        optLoadContacts()
        continueGame()
    elif opt==7: # switch language
        lang=optSwitchLanguage(lang)
    elif opt==0: # exit
        gameon=False    
    else: # unrecognised option
        optUnknown()
    
    
