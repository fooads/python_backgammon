import pygame

class PiecesController:
    should_run = True
    pieces = []

    def __init__(self, pieces_view):
        for i in pieces_view.pieces:
            self.pieces.append(i)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_run = False


            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()

                for i in range(len(self.pieces)):
                    if self.pieces[i].check_clicked():

                        self.pieces[i].send_to_model(position[0], position[1])
                        self.pieces[i].set_unclicked()

                    else:
                        if self.pieces[i].return_rect().collidepoint(position):
                            self.pieces[i].set_clicked()

