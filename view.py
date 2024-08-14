import pygame


class BoardView:

    def __init__(self, board, screen):
        self.board = board
        self.screen = screen

    _rank_x_coordinates = (556, 515, 473, 430, 390, 347, 250, 209, 167, 124, 84, 41)
    _colors = {
        "white": "./backgammon/src/white_piece.png",
        "black": "./backgammon/src/black_piece.png"
    }

    def draw(self):
        for i in range(len(self.board.positions)):
            for j in range(len(self.board.positions[i])):
                if i < 12:
                    piece_img = pygame.image.load(self._colors[self.board.positions[i][j].color])
                    piece_img = pygame.transform.scale(piece_img, (20, 20))
                    self.screen.blit(piece_img, (self._rank_x_coordinates[i], 35 + 22 * j))
                else:
                    piece_img = pygame.image.load(self._colors[self.board.positions[i][j].color])
                    piece_img = pygame.transform.scale(piece_img, (20, 20))
                    self.screen.blit(piece_img, (self._rank_x_coordinates[-(i-11)], 505 - 20 * j))
