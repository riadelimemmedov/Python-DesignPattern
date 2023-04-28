from dataclasses import dataclass


"""
    A Memento Pattern says that "to restore the state of an object to its previous state". But it must do this without violating Encapsulation. Such case is useful in case of error or failure.
    The Memento pattern is also known as Token.
    Undo or backspace or ctrl+z is one of the most used operation in an editor. Memento design pattern is used to implement the undo operation. This is done by saving the current state of the object as it changes state.
"""

#!Memento
@dataclass
class Memento:  # Stores the state data
    state: str


#!Originator
class Originator:  # Creates the state
    def __init__(self, state):
        self.state = state

    def create_memento(self):
        return Memento(self.state)

    def restore_memento(self, memento: Memento):
        self.state = memento.state


#!Caretaker
class Caretaker:  # Decides to save or restore the state
    memento_list = []

    def save_state(self, state: Memento):
        self.memento_list.append(state)

    def restore(self, index: int):
        return self.memento_list[index]


#__name__ == __main__
if __name__ == '__main__':
    originator = Originator('First State')
    caretaker = Caretaker()

    caretaker.save_state(originator.create_memento())
    print(f"Current state is {originator.state}")

    originator.state = 'Second State'
    caretaker.save_state(originator.create_memento())
    print(f"Current state is {originator.state}")

    originator.state = 'Third State'
    caretaker.save_state(originator.create_memento())
    print(f"Current state is {originator.state}")

    print('########################################################################')

    originator.restore_memento(caretaker.restore(2))
    print(f"Current state is {originator.state}")

    originator.restore_memento(caretaker.restore(0))
    print(f"Current state is {originator.state}")

    originator.restore_memento(caretaker.restore(1))
    print(f"Current state is {originator.state}")
