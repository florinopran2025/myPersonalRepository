SEPARATOR_MENIU = " -> "

class MenuItem:
    def __init__(self, id, label):
        self.id = id
        self.label = label

    def __str__(self):
        return self.id + " " + self.label
    
class Menu:
    #variabilele din clase se numesc membri
    items = []

    #daca nu facem noi constructorul cu parametri
    #in POO limbajul creaza un constructor fara parametri
    #numit constructorul implicit

    def addMenuItem(self, menuItem):
        self.items.append(menuItem)
    
    #functiile din clase se numesc metode
    def display(self):
        print('*********************')
        print("* AGENDA TELEFONICA *")
        print('*********************')
        print()
        for i in range(0,len(self.items)):
            print ("here it is ----",self.items[i].label)
            self.displayMenuItem(self.items[i]) 
        print()

    def displayMenuItem(self,item):
        print(item.id , SEPARATOR_MENIU , item.label)

#GangOfFour GOF -> design patterns
# MenuFactory

#constructorul ajuta la construirea unui obiect al clasei
menuItem1 = MenuItem(1, "Read")

menu = Menu()
menu.addMenuItem(menuItem1)

menu.display()