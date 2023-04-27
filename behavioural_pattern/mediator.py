from __future__ import annotations

"""
    The mediator class provides a central point of control for the communication between the objects. 
    When one object needs to communicate with another object, it sends a message to the mediator object, 
    which in turn forwards the message to the appropriate object.
"""


#!ChatUser
class ChatUser:
    mediator = None

    def __init__(self, name: str):
        self.name = name

    def set_mediator(self, med: Mediator):
        self.mediator = med

    def getMediator(self):
        return 'Not found mediator' if self.mediator==None else self.mediator
    
    def send(self, msg: str):
        print(f"{self.name}: Sending message {msg}")
        self.mediator.send_message(msg, self)

    def receive(self, msg: str):
        print(f"{self.name}: Receiving message {msg}")
        
        


#!Mediator
class Mediator:

    users = []

    def add_users(self, user: ChatUser):
        self.users.append(user)
        user.set_mediator(self)

    def send_message(self, msg: str, user: ChatUser):
        for i in self.users:
            if i != user:
                i.receive(msg)


#__name__ == __main__
if __name__ == '__main__':
    mediator = Mediator()

    alice = ChatUser('Alice')
    bob = ChatUser('Bob')
    carol = ChatUser('Carol')

    mediator.add_users(alice)
    mediator.add_users(bob)
    mediator.add_users(carol)

    carol.send('Hello Guys!')
