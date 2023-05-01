from __future__ import annotations
import random
from abc import ABC, abstractmethod


"""
    Example. The State pattern allows an object to change its behavior when its internal state changes.
    An object changes its behaviour based on an internal state
    The State design pattern is a behavioral design pattern that allows an object to change its behavior based on changes to its internal state. 
    The pattern is useful when you have an object that needs to behave differently depending on its current state, and when there are multiple states that the object can be in.
"""


# *Game
class Game:
    def __init__(self):
        self.state = WelcomeScreenState(self)

    def change_state(self, state):
        self.state = state


# ?State
class State(ABC):
    def __init__(self, game):
        self.game = game
        print(f"Currently in {self} state")

    @abstractmethod
    def on_welcome_screen(self):
        pass

    @abstractmethod
    def on_playing(self):
        pass

    @abstractmethod
    def on_break(self):
        pass

    @abstractmethod
    def on_end_game(self):
        pass


#!WelcomeScreenState
class WelcomeScreenState(State):
    def on_welcome_screen(self):
        print("Currently on welcome screen")

    def on_playing(self):
        self.game.change_state(PlayingState(self.game))

    def on_break(self):
        print("From welcome to break not allowed")

    def on_end_game(self):
        print("From welcome to end game not allowed")


#!PlayingState
class PlayingState(State):
    def on_welcome_screen(self):
        print("From playing to welcome not allowed")

    def on_playing(self):
        print("Currently playing")

    def on_break(self):
        self.game.change_state(BreakState(self.game))

    def on_end_game(self):
        self.game.change_state(EndGameState(self.game))


#!BreakState
class BreakState(State):
    def on_welcome_screen(self):
        print("From break to welcome not allowed")

    def on_playing(self):
        self.game.change_state(PlayingState(self.game))

    def on_break(self):
        print("Currently on break")

    def on_end_game(self):
        print("From break to end game not allowed")


#!EndGameState
class EndGameState(State):
    def on_welcome_screen(self):
        self.game.change_state(WelcomeScreenState(self.game))

    def on_playing(self):
        print("From end game to playing not allowed")

    def on_break(self):
        print("From end game to break not allowed")

    def on_end_game(self):
        print("Currently on end game")


# _name_ == _main_
if __name__ == "__main__":
    game = Game()
    for i in range(10):
        state = random.randrange(4)
        if state == 0:
            print("Move to welcome")
            game.state.on_welcome_screen()
        elif state == 1:
            print("Move to playing")
            game.state.on_playing()
        elif state == 2:
            print("Move to break")
            game.state.on_break()
        else:
            print("Move to end game")
            game.state.on_end_game()
