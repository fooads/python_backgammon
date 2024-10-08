import pygame
from view import BoardView
from controller import BoardController
from model import Board
from winsetup import setup_window

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Backgammon')
clock = pygame.time.Clock()

board = Board()
board_view = BoardView(board, SCREEN)
board_controller = BoardController(board)

loop_running = True
while loop_running:
    clock.tick(60)  # 60 fps
    setup_window(SCREEN)
# ----------------------------------------------------

    board_view.draw()
    board_controller.handle_events()

    loop_running = board_controller.should_run
    pygame.display.update()
#----------------------------------------------------

pygame.quit()