

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#         else:
#             print("Недостаточно средств")

#     def get_balance(self):
#         return self.__balance

# account = BankAccount("Bob", 1000)
# account.deposit(500)
# account.withdraw(300)

# print(account.get_balance())
# print(account.owner)
# print(account.__balance)



# Задание: Класс Rectangle
# 📦 Что нужно сделать:
# Создай класс Rectangle, у которого есть:
# Приватные переменные:
# __width
# __height
# Геттеры и сеттеры через @property:
# для width и height
# сеттеры должны не позволять отрицательные значения
# Метод area, который возвращает площадь прямоугольника


# class Rectangle:
#     def __init__(self, width, heigth):
#         self.__widht = width
#         self.__heigth = heigth

#     @property
#     def width(self):
#         return self.__widht

#     @width.setter
#     def width(self, value):
#         if value >= 0:
#             self.__widht = value
#         else:
#             print("Ширина не может быть отрицательным")
    
#     @property
#     def heigth(self):
#         return self.__heigth

#     @heigth.setter
#     def heigth(self, value):
#         if value >= 0:
#             self.__heigth = value
#         else:
#             print("Высота не может быть отрицательным")

#     def area(self):
#         return self.__widht * self.__heigth


# r = Rectangle(10, 5)

# print("Ширина", r.width)
# print("Высота", r.heigth)
# print("Площадь", r.area())

# r.width = -3
# r.heigth = 20

# print("Новая площадь", r.area())


class Animal:
    def speak(self):
        print("Животное издает звук")

class Dog(Animal):
    def speak(slef):
        print("Gav Gav")

class Cat(Animal):
    def speak(self):
        print("Mya Mya")

class Python(Animal):
    def speak(self):
        print("Python")

animals = [Dog(), Cat(), Animal(), Python()]

for animal in animals:
    animal.speak()