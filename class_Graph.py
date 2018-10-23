import pygame
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Graph():
    def __init__(self, res, screen):
        self.res = res
        self.screen = screen

    def draw(self, lisst):
        prev_pos = (self.res[0]/2, self.res[1])
        i = 0
        for population in lisst:
            cur_pos = (self.res[0]/2+i/8, self.res[1]-population/100)
            pygame.draw.line(self.screen, BLACK, prev_pos, cur_pos, 2)
            prev_pos = cur_pos
            i += 1

            
        
