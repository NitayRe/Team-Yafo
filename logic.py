WHITE = 0
BLACK = 1


def move(src, dest, stacks):
    stacks[dest].push(stacks[src].pop())


def legal(stacks, src, dest, dice1, dice2, turn):
    if turn == WHITE:
        if src + dice1 != dest and src + dice2 != dest:
            return False
        available = stacks[dest].isEmpty or (stacks[dest].getColor == BLACK and stacks[dest].size == 1)
        if src + dice1 == dest and available:
            return True
        elif src + dice2 == dest and available:
            return True