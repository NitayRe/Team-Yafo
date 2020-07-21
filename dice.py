import pygame
import random as rnd


class Dice:
    def __init__(self, x, y):
        self.value = -1
        self.x = x
        self.y = y

    def roll(self):
        self.value = rnd.randint(1, 6)

    def get_dice(self):
        return self.value

    def draw(self):
        if self.value == 1:
            dice = pygame.image.load("one").convert_alpha
        
        elif self.value == 2:
            dice = pygame.image.load("two")
       
        elif self.value == 3:
            dice = pygame.image.load("three")
         
        elif self.value == 4:
            dice = pygame.image.load("four")
           
        elif self.value == 5:
            dice = pygame.image.load("five")
           
        elif self.value == 6:
            dice = pygame.image.load("six")
        
		dice_rect = dice.get_rect()
        dice_rect.x = self.x
        dice_rect.y = self.y

