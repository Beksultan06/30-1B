


# class Dog:
#     def __init__(self, name, breed, color):
#         self.name = name 
#         self.breed = breed
#         self.color = color
    
#     def bark(self):
#         print(f"{self.name} лает!")

# dog1 = Dog("Bob", "Овчарка", "Dark")
# print(dog1.name)
# print(dog1.color)
# dog1.bark()


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand 
#         self.model = model 

#     def info(self):
#         print(f"Бранд : {self.brand}, модель {self.model} едит в город!")

# car = Car("Toyota", "Supra MK4")
# car.info()


# class Animal:
#     def __init__(self, name):
#         self.name = name 

#     def speak(self):
#         print(f"{self.name} издает звук")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} лает!")

# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} мяукает!")

# dog = Dog("Bob")
# cat = Cat("Alice")
# dog.speak()
# cat.speak()

# Привет! Меня зовут Алия, мне 18 лет.


class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def hello(self):
        print(f"HEllo My name is {self.name}, {self.age}")

person1 = Person("Bob", 19)
person2 = Person("Alice", 20)

person1.hello()
person2.hello()