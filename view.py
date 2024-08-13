import pygame


class BoardView:

    def __init__(self, board, screen):
        self.board = board
        self.screen = screen

    _rank_x_coordinates = (556, 515, 473, 430, 390, 347, 250, 209, 167, 124, 84, 41)
    _colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0)
    }

    def draw(self):
        for i in range(len(self.board.positions)):
            for j in range(len(self.board.positions[i])):
                if i < 12:
                    piece = pygame.Rect((self._rank_x_coordinates[i], 35 + 20 * j, 15, 15))
                    pygame.draw.rect(self.screen, self._colors[self.board.positions[i][j].color], piece)
                else:
                    piece = pygame.Rect((self._rank_x_coordinates[-(i-11)], 505 - 20 * j, 15, 15))
                    pygame.draw.rect(self.screen, self._colors[self.board.positions[i][j].color], piece)

