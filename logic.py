import pieces
import dice
import pygame as pg

WHITE = 255,255,255
BLACK = 0,0,0

clock = pg.time.Clock()

def move(src, dest, stacks, removed):
	if (len(stacks[dest]) == 1) and (stacks[dest].getColor() != stacks[src].getColor()):
		pieceToRemove = stacks[dest].pop()
		if stacks[dest].getColor == WHITE: removed[0].append(pieceToRemove)
		else: removed[1].append(pieceToRemove)

	stacks[dest].push(stacks[src].pop())


def islegal(stacks, src, dest, possibleSteps, turn):
	if stacks[src].isEmpty() or stacks[src].getColor() != turn:
		return False
	if dest-src not in possibleSteps or stacks[src].isEmpty():
		return False
	emptyColomn = stacks[dest].isEmpty()
	sameColor = stacks[dest].getColor() == stacks[src].getColor()
	eatable = (stacks[dest].getColor() != stacks[dest].getcolor()) and len(stacks[dest]) == 1)
	available = emptyColomn or sameColor or eatable
	if not available:
		return False
	return True



def playOneTurn(stacks, dice1, dice2, turn, removed):

	possibleSteps = [dice1, dice2]
	if (dice1 == dice2):
		possibleSteps *= 2


	while len(possibleSteps) != 0:
		coord=[]
		while len(coord)<=2:
			mousePressed = False
			while True:
				for event in pg.event.get():
					if event.type == pg.MOUSEBUTTONDOWN:
						if event.button == 1:
							mousePressed = True
					if event.type == pg.QUIT:
						exit(1)
					x = pg.mouse.get_pos()[0]
					y = pg.mouse.get_pos()[1]
					index = game.whichStack(x, y)
					if mousePressed:
						coord.append(index)
						clock.tick(300)
					mousePressed = False
					clock.tick(30)

		src = coord[0]
		dest = coord[1]
		if islegal(stacks, src, dest, possibleSteps, turn):
			move(src, dest,stacks, removed)
		possibleSteps.remove(abs(dest-src))
