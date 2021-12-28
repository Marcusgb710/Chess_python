import pygame
from Chess.board import draw_board

WIDTH =800
HEIGHT =800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def redraw():
    WIN.fill((0,0,0))
    for s in draw_board():
        s.draw(WIN )
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redraw()


main()