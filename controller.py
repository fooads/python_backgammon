import pygame


class BoardController:
    should_run = True

    def __init__(self, board_model):
        self.board_model = board_model

    def _match_mouse_position_to_flank(self, position):
        match position:
            case (x, y) if 542 < x < 584 and 28 < y < 282:
                return 0
            case (x, y) if 501 < x < 542 and 28 < y < 282:
                return 1
            case (x, y) if 459 < x < 501 and 28 < y < 282:
                return 2
            case (x, y) if 418 < x < 459 and 28 < y < 282:
                return 3
            case (x, y) if 375 < x < 418 and 28 < y < 282:
                return 4
            case (x, y) if 335 < x < 375 and 28 < y < 282:
                return 5
            case (x, y) if 236 < x < 279 and 28 < y < 282:
                return 6
            case (x, y) if 192 < x < 236 and 28 < y < 282:
                return 7
            case (x, y) if 156 < x < 192 and 28 < y < 282:
                return 8
            case (x, y) if 109 < x < 156 and 28 < y < 282:
                return 9
            case (x, y) if 70 < x < 109 and 28 < y < 282:
                return 10
            case (x, y) if 26 < x < 70 and 28 < y < 282:
                return 11
            case (x, y) if 26 < x < 70 and 282 < y < 525:
                return 12
            case (x, y) if 70 < x < 109 and 282 < y < 525:
                return 13
            case (x, y) if 109 < x < 156 and 282 < y < 525:
                return 14
            case (x, y) if 156 < x < 192 and 282 < y < 525:
                return 15
            case (x, y) if 192 < x < 236 and 282 < y < 525:
                return 16
            case (x, y) if 236 < x < 279 and 282 < y < 525:
                return 17
            case (x, y) if 335 < x < 375 and 282 < y < 525:
                return 18
            case (x, y) if 375 < x < 418 and 282 < y < 525:
                return 19
            case (x, y) if 418 < x < 459 and 282 < y < 525:
                return 20
            case (x, y) if 459 < x < 501 and 282 < y < 525:
                return 21
            case (x, y) if 501 < x < 542 and 282 < y < 525:
                return 22
            case (x, y) if 542 < x < 584 and 282 < y < 525:
                return 23

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                print(self._match_mouse_position_to_flank(position))
