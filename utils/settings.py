import pygame
pygame.init()
pygame.font.init()

#Constants

#colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 255, 0)
COLOR_GREEN = (0, 0, 255)
COLOR_GRAY = (217, 217, 217)
COLOR_YELLOW = (255, 255, 0)
COLOR_ORANGE = (255, 125, 0)

FPS = 240

#Size
WIDTH, HEIGHT = 600, 700
ROWS = COLS = 100

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BACKGROUND_COLOR = COLOR_WHITE

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("comicsans", size)
