from typing import Literal
from random import randint
import pygame



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


class Board:

    positions = []
    die1 = None
    die2 = None
    turn: Literal['white', 'black'] = 'white'

    def __init__(self):

        for i in range(23):
            a = Stack()
            self.positions.append(a)

        for i in range(15):
            self.positions[0].push(Piece('white'))
            self.positions[11].push(Piece('black'))

    def __repr__(self):
        return str(self.positions)

    def throw_dice(self):
        self.die1 = randint(1, 6)
        self.die2 = randint(1, 6)
        print(f"{self.turn} got {self.die1} and {self.die2}")

    # def move_piece(self, source, destination):
    #     self.positions[source].pop()
    #     self.positions[destination].push(Piece(self.turn))

    def check_move(self, source, destination):
        if not self.positions[source].peek():
            print("invalid move")


board = Board()



pygame.init()

width = 800
height = 600


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()



starting_position = [300, 250, 50, 50]

run = True

rec_sel = False

while run:



    player = pygame.Rect(tuple(starting_position))

    pygame.draw.rect(screen, (255, 0, 0), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()

            if not rec_sel:
                if player.collidepoint(position):
                    rec_sel = True
                    screen.fill((0, 0, 0))
            elif rec_sel:
                position = pygame.mouse.get_pos()
                starting_position = [*position, 50, 50]
                screen.fill((0, 0, 0))
                rec_sel = False



    pygame.display.update()
    clock.tick(60)  # 60 fps



pygame.quit()
