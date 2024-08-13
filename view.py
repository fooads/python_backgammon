import pygame
# from main import SCREEN


class PiecesView:
    pieces = []

    def __init__(self, models, screen):
        self.screen = screen
        for i in models:
            self.pieces.append(BallView(i, self.screen))

    def draw(self):
        for i in range(len(self.pieces)):
            pygame.draw.rect(self.screen, (255, 0, 0), self.pieces[i].return_rect())
    #
    # def check_clicked(self, piece_number):
    #     return self.pieces[piece_number].clicked


class BallView:

    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def return_rect(self):
        return pygame.Rect((self.model.x, self.model.y, 25, 25))

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.return_rect())

    def send_to_model(self, x, y):
        self.model.move((x, y))

    def check_clicked(self):
        return self.model.clicked

    def set_clicked(self):
        self.model.clicked = True

    def set_unclicked(self):
        self.model.clicked = False
