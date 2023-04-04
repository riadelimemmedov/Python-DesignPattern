
"""
    Decorator Method is a Structural Design Pattern which allows you to dynamically attach 
    new behaviors to objects without changing their implementation by placing these objects inside the wrapper objects that contains the behaviors.
"""
# *https: // www.geeksforgeeks.org/decorator-method-python-design-patterns/ => this is great resource understant decorator design pattern for python developers


from abc import ABC, abstractmethod


# ?CoffeeMachine
class CoffeeMachine(ABC):
    @abstractmethod
    def make_small_coffee(self):
        pass

    @abstractmethod
    def make_large_coffee(self):
        pass


#!BasicCoffeeMachine
class BasicCoffeeMachine(CoffeeMachine):
    def make_small_coffee(self):
        print('Basic coffee machine : Making small coffee')

    def make_large_coffee(self):
        print('Basic coffee machine : Making large coffee')


#!EnhancedCoffeeMachine
class EnhancedCoffeeMachine(CoffeeMachine):
    def __init__(self, basic_machine: BasicCoffeeMachine):
        self.basic_machine = basic_machine

    def make_small_coffee(self):  # keep same functionality
        self.basic_machine.make_small_coffee()

    def make_large_coffee(self):  # change functionality
        print('Enhanced coffee machine use large coffee')

    def make_milk_coffee(self):  # add functionality
        print('Enhanced coffee machine : Making milk coffee')
        self.basic_machine.make_small_coffee()
        print('Enhanced coffee machine : adding milk')


if __name__ == '__main__':
    basic_machine = BasicCoffeeMachine()
    enhanced_machine = EnhancedCoffeeMachine(basic_machine)

    enhanced_machine.make_small_coffee()
    print()
    enhanced_machine.make_large_coffee()
    print()
    enhanced_machine.make_milk_coffee()
    print()
