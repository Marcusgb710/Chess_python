import pygame



class board_square:
    def __init__(self, x, y, color=None, pic=None):
        self.x = x
        self.y = y
        self.w = 100
        self.h = 100
        if color != None:
            self.color = color
        if pic != None:
            self.pic = pic

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))


def draw_board():
    square_list = []
    x = 0
    y = 0
    h = 1
    bh = 1
    for i in range(64):
        if x == 800:
            x = 0
            y += 100
        if bh == 1 and i % 8 == 0:
            if h ==1:
                square_list.append(board_square(x, y, color = (0, 0, 0)))
                h -=1
            else:
                square_list.append(board_square(x, y, color=(255, 255, 255)))
                h += 1
            bh -= 111
        else:
            if h ==1:
                square_list.append(board_square(x, y, color = (255, 255, 255)))
                h -=1
            else:
                square_list.append(board_square(x, y, color=(0,0,0)))
                h += 1
            bh += 1
        x += 100

    return square_list

