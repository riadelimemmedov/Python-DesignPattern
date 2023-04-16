
"""
    The Flyweight design pattern is a structural pattern that aims to reduce the memory usage of an application by sharing objects between multiple contexts. 
    It is useful when there is a large number of objects in the application, and the cost of creating each object is high. By sharing objects, 
    the application can reduce memory usage and improve performance.

    In Python, the Flyweight pattern can be implemented using a combination of class methods, instance variables, and dictionaries. Here's an example implementation
"""

#* https://www.geeksforgeeks.org/flyweight-method-python-design-patterns/ => his is great resource understant flyweight design pattern for python developers


from abc import ABC,abstractmethod
import random


#*Method1
# #!Sprite
# class Sprite(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
    
#     @abstractmethod
#     def move(self,x:int,y:int):
#         pass
    


# #?FigtherRank
# class FigtherRank:
#     private = 0
#     sergeant = 1
#     major = 2


# #!Figther
# class Figther(Sprite):
#     def __init__(self,rank:FigtherRank):
#         self.rank = rank
        
#     def draw(self):
#         print(f"Drawing Figther {self}")
        
#     def move(self,x:int,y:int):
#         print(f"Moving Figther {self} to position {x}, {y}")
        

# #!FigtherFactory
# class FigtherFactory:
#     def __init__(self):
#         self.figthers = []
        
    
#     def get_figther(self,rank:FigtherRank):
#         f = self.figthers[rank]
#         if not f:
#             f = Figther(rank)
#             self.figthers[rank] = f
#             print('Rank ', rank)
#             print('Figther ', f)
#         return f
    

# #!Army
# class Army:
#     army = []
    
#     def spam_figther(self,rank:FigtherRank):
#         self.army.append(Figther(rank))
        
#     def draw_army(self):
#         for figther in self.army:
#             if figther.rank == FigtherRank.major:
#                 print('M',end='')
#             elif figther.rank == FigtherRank.sergeant:
#                 print('S',end='')
#             else:
#                 print('P',end='')

# if __name__ == '__main__':
#     army_size = 1000
#     army = Army()
    
#     for i in range(army_size):
#         r = random.randrange(3)
#         army.spam_figther(r)
        
#     army.draw_army()


#*Method2
#!Flyweight
class Flyweight:
    _shared_state = {}
    
    def __init__(self,intrinsic_state):
        self.__dict__ = self._shared_state
        self.intrinsic_state = intrinsic_state
        
    def operation(self,extrinsic_state):
        print(f"Intrinsic state : {self.intrinsic_state}\n. Extrinsic state : {extrinsic_state}")

#!FlyweightFactory
class FlyweightFactory:
    _flyweights = {}
    
    @classmethod
    def get_flyweight(cls,intrinsic_state):
        if intrinsic_state not in cls._flyweights:
            print('ins')
            cls._flyweights[intrinsic_state] = Flyweight(intrinsic_state)
        #else
        return cls._flyweights[intrinsic_state]
    
    
if __name__ =='__main__':
    factory = FlyweightFactory()
    
    flyweight1 = factory.get_flyweight('state1')
    flyweight1.operation('A')
    print('Flyweight1 ', flyweight1)
    
    
    flyweight2 = factory.get_flyweight('state2')
    flyweight2.operation('B')
    print('Flyweight2 ', flyweight2)
    
    
    flyweight3 = factory.get_flyweight('state1')
    flyweight3.operation('C')
    print('Flyweight3 ', flyweight1)