import pygame as pg



class Piece:
	BLACK = 0,0,0
	WHITE = 255,255,255
    
	def __init__(self, color):
		self.type = color

	def getColor(self):
		return self.type


class Stack:
	def __init__(self, x, y):
		self.items = []
		self.x = x
		self.y = y

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def getColor(self):
		return self.pop().getColor()



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


