from abc import ABC,abstractmethod

"""
    The Command design pattern is a behavioral pattern in software design that is used to encapsulate a request as an object. This object can then be passed around and used to invoke different methods at different times,
    allowing for flexibility and decoupling of the calling code from the code that performs the requested action.
"""


#!Command
class Command(ABC):
    def __init__(self,command_id:int):
        self.command_id = command_id
    
    @abstractmethod
    def execute(self):
        pass
    


#*OrderFoodCommand
class OrderFoodCommand(Command):
    def execute(self):
        print(f"Adding order with id {self.command_id}")
        

#*PayOrderedFoodCommand
class PayOrderedFoodCommand(Command):
    def execute(self):
        print(f"Paying for order with id {self.command_id}")


#*CommandProcessor
class CommandProcessor:
    queue = []
    
    def add_to_queue(self,command:Command):
        self.queue.append(command)
        
    
    def process_commands(self):
        [item.execute() for item in self.queue]
        self.queue = []


#__name__ == __main__
if __name__ == '__main__':
    processor = CommandProcessor()
    
    processor.add_to_queue(OrderFoodCommand(1))
    processor.add_to_queue(OrderFoodCommand(2))
    processor.add_to_queue(PayOrderedFoodCommand(1))
    processor.add_to_queue(OrderFoodCommand(3))
    processor.add_to_queue(PayOrderedFoodCommand(2))
    processor.add_to_queue(PayOrderedFoodCommand(3))
    
    processor.process_commands()
    