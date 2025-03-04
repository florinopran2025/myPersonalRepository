

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.width*self.length
    def perimeter(self):
        return 2*(self.width+self.length)
    def decoratePerimeter(self,sign):
        for i in range (0,self.length):
            for j in range (0,self.width):
                if i==0 or i==self.length-1 or j==0 or j==self.width-1:
                    print(sign,end="")

                else:
                    print(" ",end="")
                if j==self.width-1:
                    print()
    def __str__(self):
        return "length="+str(self.length)+" , width="+str(self.width)

r1=Rectangle(10,20)
print(r1)
print(r1.area())
print(r1.perimeter())
r1.decoratePerimeter("*")

# import math

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return math.pi*self.radius*self.radius
#     def perimeter(self):
#         return 2*math.pi*self.radius
#     def __str__(self):
#         return "radius="+str(self.radius)

# c1=Circle(10)
# print(c1)
# print("area=",c1.area())
# print("perimeter=",c1.perimeter())


