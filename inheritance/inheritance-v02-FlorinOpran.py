# figures description : chat gpt


# Quadrilateral:
# - Sides: 4
# - Angles: The sum of the angles is 360°
# - Parallel Sides: Depends on the type
# - Special Properties: Any polygon with 4 sides
class Quadrilateral: #patrulater - laturi neregulate (diferite)
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

# Rhombus:
# - Sides: 4
# - Angles: All opposite angles are equal
# - Parallel Sides: 2 pairs of parallel sides
# - Special Properties: 
#   - All sides are equal
#   - Diagonals are perpendicular and bisect each other
class Rhombus (Quadrilateral):
    def __init__(self, side):
        super().__init__(side,side,side,side)

# Trapezoid:
# - Sides: 4
# - Angles: The sum of the angles is 360°
# - Parallel Sides: 1 pair of parallel sides
# - Special Properties:
#   - Can be isosceles (with equal non-parallel sides) 
#   - Can be right (with a 90° angle)
class Trapezoid(Quadrilateral):
    def __init__(self, side1, side2, side3):
        super().__init__(side1,side2,side1,side3)



# Parallelogram:
# - Sides: 4
# - Angles: Opposite angles are equal
# - Parallel Sides: 2 pairs of parallel sides
# - Special Properties:
#   - Opposite sides are equal
#   - Diagonals bisect each other
class Parallelogram(Quadrilateral):
    def __init__(self, side1, side2):
        super().__init__(side1,side2,side1,side2)

# opposite sides are equal
class Paralelipiped(Quadrilateral):
    def __init__(self, side1, side2):
        super().__init__(side1,side2,side1,side2)

    

class Rectangle(Paralelipiped):
    def __init__(self, width, height):
        super().__init__(width, height, width, height)

    def area(self):
        return self.side1 * self.side2
    
    def __str__(self):
        return str(self.side1) + "x" + str(self.side2)
    
#  "is a" it's a type of relation

#inheritance  mostenire

# a square is a
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side, side, side)

    



#creates an object of the class Rectangle and stores the reference in the variable
# rectangle 
rectangle = Rectangle(100,200)
print("the rectangle " + str(rectangle) + " has the area " + str(rectangle.area()))
print("the rectangle with " + str(rectangle) + " has the perimeter "+ str(rectangle.perimeter()))

square = Square(50)
print("the square with " + str(square) + " has the area "+ str(square.area()))
print("the square with " + str(square) + " has the perimeter "+ str(square.perimeter()))
