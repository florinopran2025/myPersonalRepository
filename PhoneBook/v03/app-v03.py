import os
from contacts import Contacts




contacts=Contacts()



# names=["Andreea", "Marius", "Valeriu"]
# phones=["0751.100.666","0751.200.666","0751.300.666"]
# emails=["andreea@yahoo.com","marius@gmail.com","valeriu@hotmail.com"]


while contacts.gameon:    
    contacts.displayMenu()
    opt=int(input("What do you want?"))
    if opt==1: # display contacts
        contacts.optDisplayContacts()        
    elif opt==2: # search contact
        contacts.optSearchContact()
    elif opt==3: # sort contacts
        contacts.optSortContacts()
    elif opt==4: # add contact
        contacts.addContact()
    elif opt==5: # save contacts
        contacts.optSaveContacts()
    elif opt==6: # load contacts
        contacts.optLoadContacts()
    elif opt==7: # switch language
        contacts.optSwitchLanguage()        
    elif opt==0: # exit
        gameon=False    
    else: # unrecognised option
        contacts.unknownOption()
    contacts.continueGame()
    
