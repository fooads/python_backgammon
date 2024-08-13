import pygame


def setup_window(screen):
    bg = pygame.image.load("backgammon/src/board.jpg")
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
