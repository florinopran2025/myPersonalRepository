# Notes:
# Task 1, task 2 and task 3 are similar.
# for task 1: i provided a simple solution
# for task 2: i use 2 classes: class Books stores in a list (titles) all the books initialised with Book class.
# (the Book class is similar with Car class from task 1)
# for task 3: similar to task 1 solution. only marginal changes.


# Module: Object-Oriented Programming
# Topic: Classes. Objects. Part 1

# Task 1
# Implement a class Car. Class fields should store the following: 
# model, year of release, manufacturer, engine capacity, color, price. 
# Implement class methods for data input and output, 
# provide access to individual fields through class methods.

# class Car:
#     def __init__(self, model, releaseYear, manufacturer, engineCapacity, color, price):
#         self.model=model
#         self.releaseYear=releaseYear
#         self.manufacturer=manufacturer
#         self.engineCapacity=engineCapacity
#         self.color=color
#         self.price=price
#     def change(self,fieldName,fieldValue):
#         setattr(self,fieldName,fieldValue)
#     def displayField(self,fieldName):        
#         fieldValue=getattr(self,fieldName)
#         print(f"{fieldName}={fieldValue}")
#     def __str__(self):
#         return ("model="+str(self.model)+", releaseYear="+str(self.releaseYear)+
#         " manufacturer="+str(self.manufacturer)+", engineCapacity="+str(self.engineCapacity)+
#         " color="+str(self.color)+", price="+str(self.price)+" euro")

# car1=Car("Dacia Spring", "2024", "Dacia", 45, "White",22000)
# print(car1)
# newPrice=int(input(f"Set the new price for {car1.model}  {car1.manufacturer}?"))
# car1.change("price",newPrice)
# print(car1)
# car1.displayField("price")

# Task 2
# Implement a class Book. 
# Class fields should store the following: 
# title, year of release, publisher, genre, author, price. 
# Implement class methods for data input and output, 
# provide access to individual fields through class methods.

# class Book:
#     def __init__(self, title, releaseYear, publisher, genre, author, price):
#         self.title=title
#         self.releaseYear=releaseYear
#         self.publisher=publisher
#         self.genre=genre
#         self.author=author
#         self.price=price

#     def change(self,fieldName,fieldValue):
#         setattr(self,fieldName,fieldValue)

#     def fieldValue(self,fieldName):        
#         theFieldValue=getattr(self,fieldName)
#         return theFieldValue

#     def __str__(self):
#         return ("Title="+str(self.title)+", releaseYear="+str(self.releaseYear)+
#         " publisher="+str(self.publisher)+", genre="+str(self.genre)+
#         " author="+str(self.author)+", price="+str(self.price)+" lei")

# class Books:
#     def __init__(self):
#         self.titles=[]
#     def addTitle(self,book1):
#         self.titles.append(book1)

# book1=Book("Think and grow rich", 1937, "Editura 1", 
#            "self help", "Napoleon Hill",23)

# book2=Book("Project Hail Mary", 2021, "Editura 2", 
#            "science fiction", "Andy Weir",34)

# library=Books()
# library.addTitle(book1)
# library.addTitle(book2)
# print(library.titles[0])
# print(library.titles[1])
# library.titles[1].change("price",37)
# print(library.titles[1])
# print(f"The new price of {library.titles[1].fieldValue("title")} is:",library.titles[1].fieldValue("price"))

# Task 3
# Implement a class Stadium. 
# Class fields shout store the following: 
# stadium's name, date of opening, country, city, seating capacity. 
# Implement class methods for data input and output, 
# provide access to individual fields through class methods.


class Stadium:
    def __init__(self, name, openingDate, country, city, seatingCapacity):
        self.name=name
        self.openingDate=openingDate
        self.country=country
        self.city=city
        self.seatingCapacity=seatingCapacity
    def changeField(self,fieldName,fieldValue):
        setattr(self,fieldName,fieldValue)
    def seeField(self,fieldName):
        return getattr(self,fieldName)
    def __str__(self):
        return self.name+" "+str(self.openingDate)+" "+self.country+" "+self.city+" "+str(self.seatingCapacity)

ghencea=Stadium("Ghencea",2018,"Romania","Bucharest", 30000)
print(ghencea)
ghencea.changeField("seatingCapacity",32000)
print(ghencea)
fieldNameInput=input("What do you want to know about this stadium?")
response=ghencea.seeField(fieldNameInput.lower())
print(f"{fieldNameInput}={response}")



