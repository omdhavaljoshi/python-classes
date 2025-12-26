class Animal:
    def __init__(self):
        pass
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def __init__(self):
        super().__init__()
    def bark(self):
        print("Dog is barking!")

class Cat(Animal):
    def __init__(self):
        super().__init__()
    def meow(self):
        print("Cat says meow!")

dog = Dog()
cat = Cat()
dog.eat()
cat.eat()
dog.bark()
cat.meow()