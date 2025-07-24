


# class Person:
#     def __init__(self, name):
#         self.name = name
# 
#     def __str__(self):
#         return f"Person: {self.name}"
# 
#     def info(self):
#         print(f"Person: {self.name}")
# 
# p = Person("Bob")
# print(p)
# # print(p.info())
# 
# class Vector:
#     def __init__(self, x, y):
#         self.x = x 
#         self.y = y
# 
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
# 
#     def __str__(self):
#         return f"({self.x}, {self.y})"
# 
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# print(v1 + v2)


# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b

# print(Math.add(2, 5))


# class TemperatureConverter:
#     @staticmethod
#     def celsius(c):
#         return (c * 9/5) + 32

# print(TemperatureConverter.celsius(0))


# class Person:
#     def __init__(self, name):
#         self.name = name
# 
#     @classmethod
#     def from_dict(cls, data):
#         return cls(data['name'])
# 
# p = Person.from_dict({"name" : "Bob"})
# print(p.name)
# print(Person.__mro__)


# class A:
#     def show(self):
#         print("A")
# 
# class B(A):
#     def show(self):
#         print("B")
# 
# class C(A):
#     def show(self):
#         print("C")
# 
# class D(B, C):
#     pass 
# 
# 
# d = D()
# d.show()
# print(D.__mro__)


class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Shape: {self.name}"

    @classmethod 
    def default_shape(cls):
        return cls("Default Shape", "Black")

    @staticmethod
    def area_formula():
        print("Area = base * heigth")

class Colored:
    def __init__(self, color):
        self.color = color
    
    def show_color(self):
        print(f"Color: {self.color}")

class ColoredShape(Shape, Colored):
    def __init__(self, name, color):
        Shape.__init__(self, name)
        Colored.__init__(self, color)

    def __str__(self):
        return f"{self.name} with color {self.color}"


obj = ColoredShape("Rectange", "Blue")
print(obj)
obj.show_color()
obj.area_formula()

default_obj = ColoredShape.default_shape()
print(default_obj)