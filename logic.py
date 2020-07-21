import pieces
import dice
import pygame as pg
from game import message_display, whichStack
import time

WHITE = pieces.Piece.WHITE
BLACK = pieces.Piece.BLACK

clock = pg.time.Clock()
homeBlack = {x for x in range(6)}
homeWhite = {x for x in range(23, 23-6, -1)}
# assume islegal function was called before, and the move found as legal.
def move(src, dest, stacks, removed):
    if (len(stacks[dest]) == 1) and (stacks[dest].getColor() != stacks[src].getColor()):
        pieceToRemove = stacks[dest].pop()
        if pieceToRemove.getColor() == WHITE: removed[0].push(pieceToRemove)
        else: removed[1].push(pieceToRemove)

    stacks[dest].push(stacks[src].pop())


def islegal(stacks, src, dest, possibleSteps, turn, removed):
    if hasOut(removed, turn): return False
    
    if stacks[src].isEmpty() or stacks[src].getColor() != turn:
        return False
    sign = 1
    if turn == pieces.Piece.BLACK: sign = -1
    if sign*(dest-src) not in possibleSteps or stacks[src].isEmpty():
        return False

    emptyColomn = stacks[dest].isEmpty()
    if emptyColomn:
        return True
        
    sameColor = stacks[dest].getColor() == stacks[src].getColor()
    eatable = (not sameColor) and len(stacks[dest]) == 1
    available = sameColor or eatable
    if not available:
        return False
    
    return True


def isEndOfGame(stacks, color):
    home = homeWhite
    if color == BLACK: home = homeBlack
    for i in range(24):
        if i in home: continue
        if stacks[i].isEmpty(): continue
        if (stacks[i].getColor() == color):
            return False
    return True

def hasOut(removed, color):
    if color == WHITE:
        return not removed[0].isEmpty()
    return not removed[1].isEmpty()


def trySpecialMove(stacks, possibleSteps, removed, turn, index):
    removeIndex = 0
    if turn == BLACK: removeIndex = 1
    if hasOut(removed, turn):
        oppHome = homeBlack
        if turn == BLACK:
            oppHome = homeWhite
        step = min(index + 1, 24 - index)
        if index not in oppHome:
            return False
        if step in possibleSteps:
        
            if stacks[index].isEmpty() or stacks[index].getColor() == turn:
                stacks[index].push(removed[removeIndex].pop())
                possibleSteps.remove(step)
                return True
            
            if len(stacks[index]) == 1:
                removed[1-removeIndex].push(stacks[index].pop())
                stacks[index].push(removed[removeIndex].pop())
                possibleSteps.remove(step)
                return True

        return False


    
    if isEndOfGame(stacks, turn) and (not stacks[index].isEmpty()) and stacks[index].getColor() == turn:
        step = min(index, 23 - index)
        for x in possibleSteps:
            if x >= step:
                stacks[index].pop()
                possibleSteps.remove(x)
                return True
    
    return False

def getCoordinate():
    while True:
        mousePressed = False
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousePressed = True
            if event.type == pg.QUIT:
                exit(1)
            x = pg.mouse.get_pos()[0]
            y = pg.mouse.get_pos()[1]
            index = whichStack(x, y)
            if mousePressed:
                clock.tick(300)
                return index
            mousePressed = False
            clock.tick(30)
            
def playOneTurn(stacks, dice1, dice2, turn, removed):
    possibleSteps = [dice1, dice2]
    if dice1 == dice2:
        possibleSteps *= 2

    possibleSteps.sort()

    while len(possibleSteps) != 0:
        if not moveExists(stacks, turn, removed, possibleSteps):
            message_display("No valid Moves", 400,60)
            time.sleep(1)
            return
        print(possibleSteps)
        src = getCoordinate()
        played = trySpecialMove(stacks, possibleSteps, removed, turn, src)
        
        if played:
            yield 1
            continue
        
        dest = getCoordinate()
        if islegal(stacks, src, dest, possibleSteps, turn, removed):
            move(src, dest,stacks, removed)
            possibleSteps.remove(abs(dest-src))
            yield 1

def isAvailable(stacks, turn, index):
    return stacks[index].isEmpty() or stacks[index].getColor() == turn or len(stacks[index]) == 1

def moveExists(stacks, turn, removed, possibleSteps):

    if hasOut(removed, turn):
        for i in possibleSteps:
            if turn == WHITE:
                if isAvailable(stacks, turn, i-1):
                    return True
            if turn == BLACK:
                if isAvailable(stacks, turn, 24-i):
                    return True
        return False
    
    srcs = {i for i in range(24) if (not stacks[i].isEmpty()) and stacks[i].getColor() == turn}
    if len(srcs) == 0: return False
    
    if isEndOfGame(stacks, turn):
        maxDie = max(possibleSteps)
        if turn == WHITE:
            if max(srcs) + maxDie > 23:
                return True
        if turn == BLACK:
            if min(srcs) - maxDie < 0:
                return True
    for src in srcs:
        for dest in range(24):
            if islegal(stacks, src, dest,possibleSteps, turn, removed):
                return True
    return False






def hasLeft(stacks, color):
    for stack in stacks:
        if (not stack.isEmpty()) and stack.getColor() == color: return True
    return False
