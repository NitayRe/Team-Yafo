import pygame as pg
import sys


class Piece:
    def __init__(self, type):
        self.type = type

    def getType(self):
        return self.type


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


class DrawableStack(Stack):
    def __init__(self, x, y):
        super().__init__()
        self.items = []
        self.x = x
        self.y = y

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.items.__len__() < 5:
            self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def draw(self):
        x = self.x
        y = self.y
        if y == 0:
            for piece in self.items:
                if piece.getType() == WHITEPIECE:
                    pg.draw.circle(screen, white, (x + 45, y + 40), 20)
                if piece.getType() == BLACKPIECE:
                    pg.draw.circle(screen, black, (x + 45, y + 40), 20)
                y += 40
        else:
            for piece in self.items:
                if piece.getType() == WHITEPIECE:
                    pg.draw.circle(screen, white, (x + 45, y - 40), 20)
                if piece.getType() == BLACKPIECE:
                    pg.draw.circle(screen, black, (x + 45, y - 40), 20)
                y -= 40


screen = pg.display.set_mode((800, 800))
background_image = pg.image.load("background.bmp")
clock = pg.time.Clock()
black = 0, 0, 0
white = 255, 255, 255
BLACKPIECE = 0
WHITEPIECE = 1
stacks = []
stackX = 0
stackY = 0
for i in range(24):
    if i<12:
        stacks.append(DrawableStack(stackX, stackY))
        stackX += 65
    elif i == 12:
        stackX = 0
        stackY = 800
        stacks.append(DrawableStack(stackX,stackY))
        stackX += 66
    else:
        stacks.append(DrawableStack(stackX, stackY))
        stackX += 66

screen.blit(background_image, [0, 0])


def main():
    left_mouse_down = 0
    right_mouse_down = 0
    while 1:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_mouse_down = True
                if event.button == 3:
                    right_mouse_down = True

            if event.type == pg.QUIT:
                sys.exit(1)

            if left_mouse_down:
                x = pg.mouse.get_pos()[0]
                y = pg.mouse.get_pos()[1]
                index = whichStack(x, y)
                stacks[index].push(Piece(BLACKPIECE))

            if right_mouse_down:
                x = pg.mouse.get_pos()[0]
                y = pg.mouse.get_pos()[1]
                index = whichStack(x, y)
                stacks[index].push(Piece(WHITEPIECE))

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    pass

            left_mouse_down = 0
            right_mouse_down = 0
        for s in stacks:
            s.draw()
        pg.display.flip()
        clock.tick(30)

def whichStack(x,y):
    if y < 400:
        return int(x/66)
    else:
        return int(x/66)+12


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
