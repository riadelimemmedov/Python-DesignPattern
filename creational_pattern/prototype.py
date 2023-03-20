import copy
from abc import ABC,abstractmethod

#!Shape => Abstract class
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    

#!Square
class Square(Shape):
    def __init__(self,size):
        self.size = size
    
    def draw(self):
        print(f"Drawing a square of size {self.size}")
        

#!Circle
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def draw(self):
        print(f"Drawing a circle of radius {self.radius}")
        

#!AbstractArt
class AbstractArt:
    def __init__(self,bg_color,shapes):
        self.bg_color = bg_color
        self.shapes = shapes
        
    def draw(self):
        print(f"Background color is {self.bg_color}")
        [x.draw() for x in self.shapes]

if __name__ == '__main__':
    shapes = [Square(5),Square(12),Circle(8)]
    art1 = AbstractArt("red",shapes)
    
    #After create instance AbstractArt class,for example I am need two or more number of same value AbstractArt class,what I have do,I am receareate same instance again to again?,not copy earlier created object usuing python copy method
    art2 = copy.copy(art1)
    
    #call original and copued object
    art1.draw()
    art2.draw()
