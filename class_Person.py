import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Person():
    
    def __init__(self, size, screen, generation, age):
        self.size = size
        self.screen = screen
        self.gen = generation
        self.age = age
        self.last_birth_age = 10
        self.address = (random.randint(0, size[0]), random.randint(0, size[1]))

    def draw(self):
        pygame.draw.rect(self.screen, BLACK, (self.address[0], self.address[1], 1, 1))
        #print("person draw method activated")

    def reproduce(self, pop):
        if self.age >= 16:
            if self.last_birth_age > 2:
                new_gen = self.gen + 1
                baby = Person(self.size, self.screen, new_gen, 0)
                survive = random.random()

                if survive > 0.1:
                    pop.append(baby)

                self.last_birth_age = 0
            self.last_birth_age += 1

    def grow(self, growth):
        self.age = self.age + growth

    def die(self, lisst, index):
        if self.age > 75:
            del(lisst[index])
            return 1
        else:
            return 0
            
            
