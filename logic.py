import pieces
import dice
WHITE = 255,255,255
BLACK = 0,0,0


def move(src, dest, stacks, removed):
	if (len(stacks[dest]) == 1) and (stacks[dest].getColor() != stacks[src].getColor()):
		pieceToRemove = stacks[dest].pop()
		if stacks[dest].getColor == WHITE: removed[0].append(pieceToRemove)
		else: removed[1].append(pieceToRemove)

	stacks[dest].push(stacks[src].pop())


def islegal(stacks, src, dest, possibleSteps, turn):
	if stacks[src].isEmpty() or stacks[src].getColor() != turn:
		return False

	if dest-src not in possibleSteps or stack[src].isEmpty():
		return False

	available = stacks[dest].isEmpty or (stacks[dest].getColor() == stacks[src].getColor()) or (stacks[dest].getColor() !=stacks[dest].getcolor() and len(stacks[dest]) == 1))
	if not available: return False
	return True



def playOneTurn(turn, dice1, dice2):
	possibleSteps = [dice1, dice2]
	if (dice1 == dice2):
		possibleSteps.append(dice1)
		possibleSteps.apppend(dice1)
