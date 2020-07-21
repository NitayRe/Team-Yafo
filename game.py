import pygame as pg



class Piece:
	BLACK = 0,0,0
	WHITE = 255,255,255
    
	def __init__(self, color):
		self.type = color

	def getColor(self):
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
		return self.items[-1]


class DrawableStack(Stack):

	
	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y

	def draw(self, screen):
		x = self.x
		y = self.y
		if y == 0:
			for piece in self.items:
				pg.draw.circle(screen, piece.getColor(), (x + 45, y + 40), 20)
				y += 40
		else:
			for piece in self.items:
				pg.draw.circle(screen, piece.getColor(), (x + 45, y - 40), 20)
				y -= 40


screen = pg.display.set_mode((800, 800))
background_image = pg.image.load("background.bmp")
clock = pg.time.Clock()

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
		stackX += 65
	else:
		stacks.append(DrawableStack(stackX, stackY))
		stackX += 65

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
				exit(1)

			if left_mouse_down:
				x = pg.mouse.get_pos()[0]
				y = pg.mouse.get_pos()[1]
				index = whichStack(x, y)
				stacks[index].push(Piece(Piece.BLACK))

			if right_mouse_down:
				x = pg.mouse.get_pos()[0]
				y = pg.mouse.get_pos()[1]
				index = whichStack(x, y)
				stacks[index].push(Piece(Piece.WHITE))

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					pass

			left_mouse_down = 0
			right_mouse_down = 0
		for s in stacks:
			s.draw(screen)
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
