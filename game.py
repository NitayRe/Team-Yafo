import pygame as pg
import pieces

screen = pg.display.set_mode((800, 800))
background_image = pg.image.load("background.bmp")
clock = pg.time.Clock()

stacks = []
stackX = 0
stackY = 0
for i in range(24):
	if i<12:
		stacks.append(pieces.Stack(stackX, stackY))
		stackX += 65
	elif i == 12:
		stackX = 0
		stackY = 800
		stacks.append(pieces.Stack(stackX,stackY))
		stackX += 65
	else:
		stacks.append(pieces.Stack(stackX, stackY))
		stackX += 65





def main():
	left_mouse_down = False
	right_mouse_down = False
	middle_mouse_down = False
	while True:
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
				stacks[index].push(pieces.Piece(pieces.Piece.BLACK))

			if right_mouse_down:
				stacks[index].push(pieces.Piece(pieces.Piece.WHITE))

			if middle_mouse_down and not stacks[index].isEmpty():
				stacks[index].pop()

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					pass

			left_mouse_down = False
			right_mouse_down = False
			middle_mouse_down = False
		
		screen.blit(background_image, [0, 0])
		for s in stacks:
			s.draw(screen)
		pg.display.flip()
		clock.tick(30)

def whichStack(x,y):
	if y < 400:
		return x//66
	else:
		return x//66 + 12


if __name__ == '__main__':
	pg.init()
	main()
	pg.quit()
