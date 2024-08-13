import pygame
from view import BallView, PiecesView
from controller import PiecesController
from model import Ball
from winsetup import setup_window

from init_board import Board

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()



pieces = []
board = Board()
for i in range(15):
    pieces.append(Ball(400, 40*i))

pieces_view = PiecesView(pieces, SCREEN)

pieces_controller = PiecesController(pieces_view)

loop_running = True
while loop_running:
    clock.tick(60)  # 60 fps
    setup_window(SCREEN)
# ----------------------------------------------------



    pieces_controller.handle_events()


    pieces_view.draw()

    loop_running = pieces_controller.should_run

    pygame.display.update()

#----------------------------------------------------

pygame.quit()