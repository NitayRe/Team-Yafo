import pygame
import random as rnd


class Dice:
    IMGS = [pygame.image.load("number1.png")
    ,pygame.image.load("number2.png")
    ,pygame.image.load("number3.png")
    ,pygame.image.load("number4.png")
    ,pygame.image.load("number5.png")
    ,pygame.image.load("number6.png")]
    
    def __init__(self, x, y):
        self.value = -1
        self.x = x
        self.y = y

    def roll(self):
        self.value = rnd.randint(1, 6)

    def get_dice(self):
        return self.value

    def draw(self, screen):
        if self.value == -1: return
        
        dice = Dice.IMGS[self.value-1]
        screen.blit(dice, [self.x, self.y])

        

