import pygame


class BoardController:
    should_run = True

    def __init__(self, board_model):
        self.board_model = board_model

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                self.board_model.move_piece(0, 2)
