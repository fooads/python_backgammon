class Ball:

    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.clicked = False

    def move(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def set_clicked(self):
        self.clicked = True

    def set_unclicked(self):
        self.clicked = False







from typing import Literal
from random import randint

class Piece:
    def __init__(self, color: Literal['white', 'black']):
        self.color = color

    def __repr__(self):
        if self.color == "white":
            return "○"
        elif self.color == "black":
            return "●"

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, element):
        self._stack.append(element)

    def pop(self):
        element = None
        if len(self._stack) > 0:
            element = self._stack.pop()
        return element

    def peek(self):
        element = None
        if len(self._stack) > 0:
            element = self._stack[-1]
        return element

    def __repr__(self):
        res = ""
        for i in self._stack:
            res = res + str(i)
        return res

    def __len__(self):
        return len(self._stack)

    def __getitem__(self, item):
        return self._stack[item]


class Board:

    positions = []
    die1 = None
    die2 = None
    turn: Literal['white', 'black'] = 'white'

    def __init__(self):

        for i in range(24):
            a = Stack()
            self.positions.append(a)

        for i in range(15):
            self.positions[0].push(Piece('white'))
            self.positions[12].push(Piece('black'))


    def __repr__(self):
        return str(self.positions)

    def throw_dice(self):
        self.die1 = randint(1, 6)
        self.die2 = randint(1, 6)
        print(f"{self.turn} got {self.die1} and {self.die2}")

    def move_piece(self, source, destination):
        self.positions[source].pop()
        self.positions[destination].push(Piece(self.turn))

    def check_move(self, source, destination):
        if not self.positions[source].peek():
            print("invalid move")

