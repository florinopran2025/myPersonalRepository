import os

class Contacts:
    def __init__(self):
        self.names=[]   # names
        self.phones=[]  # phones
        self.emails=[]  # emails
        self.lang="english"
        self.opt=0
        self.gameon=True
        # LOAD AGENDA
        file=open("C:\\_FILES\\Programare\\Python\\Curs\\apps\\2025_01_phonebook\\phonebook_v01.csv",'r')
        numberOfContacts=0
        for line in file:
            numberOfContacts+=1
            line=line.strip()
            nameOnEachLine,phoneOnEachLine,emailOnEachLine=line.split(",")
            self.names.append(nameOnEachLine)   # extract names from file
            self.phones.append(phoneOnEachLine) # extract phones from file
            self.emails.append(emailOnEachLine) # extract emails from file
        file.close()
        # LOAD MENU
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
        self.MENU ={        # construct dictionary MENU (extracted from file)
            "english": englishDict,
            "romanian": romanianDict
        }

    def __str__(self):
        return self.names

    # ----------------------------------------------------
    # ---------------- GENERAL METHODS -------------------
    # USED BY THE MAIN METHODS 
    def switchContacts(self, i,j):
        #contacts.names
        aux=self.names[i]
        self.names[i]=self.names[j]
        self.names[j]=aux
        #phones
        aux=self.phones[i]
        self.phones[i]=self.phones[j]
        self.phones[j]=aux
        #emails
        aux=self.emails[i]
        self.emails[i]=self.emails[j]
        self.emails[j]=aux

    def continueGame(self):
        input("Press ENTER to continue...")


    def searchByContactName(self,nameSearched):
        self.optLoadContacts() 
        foundIt=False
        for i in range (0,len(self.names)):
            if nameSearched.lower()==self.names[i].lower():
                print(f"{self.names[i]} has the number: {self.phones[i]}")
                foundIt=True
        if foundIt==False:
            print(f"You dont' have {nameSearched}\'s number.")

    # ----------------------------------------------------
    # --------------------- DISPLAY MENU -----------------
    def displayMenu(self):
        os.system('cls')
        print("--- --- MENU --- ---")
        for key, value in self.MENU[self.lang].items():
            print (f"{value}".ljust(2),"      (type",key,")".ljust(20))
        print()

    # ----------------------------------------------------
    # --------------------- ACTIONS FROM MENU ------------
    # 1 = DISPLAY CONTACTS
    def optDisplayContacts(self):   
        self.optLoadContacts() 
        print("Total number of contacts:",len(self.names))
        for i in range (0,len(self.names)):
            print (f"{i+1}.  {self.names[i]}\'s phone is {self.phones[i]}. \n"
                   f"You can reach him/her at {self.emails[i]}.")
        

    # 2 = SEARCH CONTACT (BY NAME)
    def optSearchContact(self):
        nameSearched=input("Name of contact?")
        self.searchByContactName(nameSearched)

    # 3 = SORT CONTACTS
    def optSortContacts(self):
        self.optLoadContacts()    
        length=len(self.names)
        for i in range (0,length-1):
            for j in range (i+1,length):
                if self.names[i]>self.names[j]:
                    self.switchContacts(i,j)
        self.optSaveContacts()
        print ("The list was successfully sorted. Here it is:")
        self.optDisplayContacts()



    # 4 = ADD CONTACT
    def addContact(self):
        """Add a new contact"""
        contactName=input("Name:")
        contactPhone=input("Phone:")
        contactEmail=input("Email:")
        self.names.append(contactName)
        self.phones.append(contactPhone)
        self.emails.append(contactEmail)
        print(f"You've successfully added {contactName} in your phone book.")

    # 5 = SAVE CONTACTS
    def optSaveContacts(self):
        file=open("C:\\_FILES\\Programare\\Python\\Curs\\apps\\2025_01_phonebook\\phonebook_v01.csv",'w')
        for i in range (0,len(self.names)):        
            file.write(f"{self.names[i]},{self.phones[i]},{self.emails[i]}")
            file.write("\n")
        print(self.names)
        print(self.phones)
        print(self.emails)
        file.close()

    # 6 = LOAD CONTACTS
    def optLoadContacts(self):    
        self.names=[]
        self.phones=[]
        self.emails=[]
        file=open("C:\\_FILES\\Programare\\Python\\Curs\\apps\\2025_01_phonebook\\phonebook_v01.csv",'r')
        numberOfContacts=0
        for line in file:
            numberOfContacts+=1
            line=line.strip()
            nameOnEachLine,phoneOnEachLine,emailOnEachLine=line.split(",")
            self.names.append(nameOnEachLine)
            self.phones.append(phoneOnEachLine)
            self.emails.append(emailOnEachLine)
        print ("You've successfully loaded",numberOfContacts,"contacts.")    
        file.close()

    # 7 = SWITCH LANGUATE
    def optSwitchLanguage(self,lang):
        if self.lang=="english":
            self.lang= "romanian"
        else:
            self.lang= "english"

    # WRONG COMMAND
    def unknownOption(self):
        print ("Nu such option in the menu.😒")