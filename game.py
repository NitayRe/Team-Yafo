import pygame as pg
from pieces import Stack, Piece, OutStack
from dice import Dice
import logic

WIDTH = 800
HEIGHT = 600
DIFF_X=65

screen = pg.display.set_mode((WIDTH, HEIGHT))
background_image = pg.image.load("background.bmp")
clock = pg.time.Clock()

stacks = []
stackX = 0
stackY = 0
for _ in range(12):
        stacks.append(Stack(stackX, stackY))
        stackX += DIFF_X
stackX -= DIFF_X
stackY = HEIGHT
for _ in range(12):
        stacks.append(Stack(stackX, stackY))
        stackX -= DIFF_X

removedPieces = []
stackY = HEIGHT // 2 - 38
for _ in range(12):
    removedPieces.append(OutStack(WIDTH // 2 - 2*DIFF_X, stackY))
    stackY += DIFF_X
stacks += removedPieces


def regularStart():
    for i in range(2):
        stacks[0].push(Piece(Piece.WHITE))
    for i in range(5):
        stacks[5].push(Piece(Piece.BLACK))
    for i in range(3):
        stacks[7].push(Piece(Piece.BLACK))
    for i in range(5):
        stacks[11].push(Piece(Piece.WHITE))
    for i in range(5):
        stacks[12].push(Piece(Piece.BLACK))
    for i in range(3):
        stacks[16].push(Piece(Piece.WHITE))
    for i in range(5):
        stacks[18].push(Piece(Piece.WHITE))
    for i in range(2):
        stacks[23].push(Piece(Piece.BLACK))


def chooseStartGamePlaces():
    left_mouse_down = False
    right_mouse_down = False
    middle_mouse_down = False
    finished = False
    while not finished:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_mouse_down = True
                if event.button == 2:
                    middle_mouse_down = True
                if event.button == 3:
                    right_mouse_down = True

            if event.type == pg.QUIT:
                exit(1)

            x = pg.mouse.get_pos()[0]
            y = pg.mouse.get_pos()[1]
            index = whichStack(x, y)

            if left_mouse_down:
                if stacks[index].isEmpty() or stacks[index].getColor() == Piece.BLACK:
                    stacks[index].push(Piece(Piece.BLACK))

            if right_mouse_down:
                if stacks[index].isEmpty() or stacks[index].getColor() == Piece.WHITE:
                    stacks[index].push(Piece(Piece.WHITE))

            if middle_mouse_down and not stacks[index].isEmpty():
                stacks[index].pop()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    finished = True

            left_mouse_down = False
            right_mouse_down = False
            middle_mouse_down = False

        screen.blit(background_image, [0, 0])
        for s in stacks:
            s.draw(screen)
        pg.display.flip()
        clock.tick(30)
        print(f"white:{logic.isEndOfGame(stacks, Piece.WHITE)} -- black:{logic.isEndOfGame(stacks, Piece.BLACK)}")
 

def text_objects(text, font):
    black = (0, 0, 0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text, centerX, centerY):
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pg.font.Font('freesansbold.ttf', 35)
    text = font.render(text, True, green, blue)
    textRect = text.get_rect()
    textRect.center = (centerX, centerY)
    screen.blit(text, textRect)
    pg.display.flip()

"""    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (centerX, centerY)
    screen.blit(TextSurf, TextRect)
    pg.display.update()"""
    


def whichStack(x, y):
    if y < HEIGHT//2:
        return x // DIFF_X
    else:
        return 23 - x // DIFF_X



dices = []
dices.append(Dice(0, HEIGHT // 2 - 10))
dices.append(Dice(0, HEIGHT // 2 + 10))
def main():
    message_display('for a regular game, press 1', WIDTH//2, 200)
    message_display('to choose the start situation, press 2', WIDTH//2, 400)
    chosen = False
    while not chosen:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    regularStart()
                    chosen = True
                elif event.key == pg.K_2:
                    chooseStartGamePlaces()
                    chosen = True
                
            if event.type == pg.QUIT:
                exit(1)
            break
        clock.tick(30)
    

    turn = 0
    turns = [Piece.WHITE, Piece.BLACK]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit(1)
        
        for dice in dices:
            dice.roll()
        
        screen.blit(background_image, [0, 0])
        for s in stacks:
            s.draw(screen)
        for dice in dices:
            dice.draw(screen)
    
        pg.display.flip()
        clock.tick(30)
        
        for _ in logic.playOneTurn(stacks, dices[0].get_dice(), dices[1].get_dice(), turns[turn], removedPieces):
            print("Played")
            screen.blit(background_image, [0, 0])
            for s in stacks:
                s.draw(screen)
            for dice in dices:
                dice.draw(screen)
        
            pg.display.flip()
            clock.tick(30)
        turn = 1 - turn


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
