import pygame
import sys
from tkinter import *
from tkinter.ttk import *

root = Tk()
pygame.init()
WINDOW_HEIGHT = root.winfo_screenheight() - 60
WINDOW_WIDTH = root.winfo_screenwidth()
FPS = 20
BLACK = (0, 0, 0)
ADD_NEW_FLAME_RATE = 25
font = pygame.font.SysFont("forte", 20)

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jogo")
canvas.fill(BLACK)


def start_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # game_loop()
        pygame.display.update()


start_game()
