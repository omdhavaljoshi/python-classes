from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
      pass
    @abstractmethod
    def resize(self):
        pass
    @abstractmethod
    def changeBack(self):
        pass
class Circle(Shape):
    pass
class Rectangle(Shape):
    pass
class Hexagon(Shape):
    pass

shape = None

shape = Circle()
