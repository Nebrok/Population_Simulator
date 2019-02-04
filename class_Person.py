import pygame
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)       

class Person():
    
    def __init__(self, size, screen, generation, age, address):
        self.size = size
        self.screen = screen
        self.gen = generation
        self.age = age
        self.last_birth_age = 10
        self.address = address
        self.x = address[0]
        self.y = address[1]
        self.children = 0

        self.nhood = 50

    def draw(self):
        pygame.draw.rect(self.screen, BLACK, (self.address[0], self.address[1], 1, 1))

    def reproduce(self, pop):
        if self.age >= 20 and self.age <= 45 and self.children <= 3:
            if self.last_birth_age > 4:
                new_gen = self.gen + 1

                r = random.randint(1, self.nhood)
                x = random.randint(-r, r)
                y = r - x ** 2

                y = math.sqrt(abs(y))
                baby_address = [self.address[0]+x*self.pos_neg(), self.address[1]+y*self.pos_neg()]

                x_pos = baby_address[0]
                y_pos = baby_address[1]

                if (x_pos < 0):
                    baby_address[0] = 600 - abs(baby_address[0])

                if (x_pos > 600):
                    baby_address[0] = abs(baby_address[0]-600)

                if (y_pos < 0):
                    baby_address[1] = 600 - abs(baby_address[1])

                if (y_pos > 600):
                    baby_address[1] = abs(baby_address[1]-600)
                        

                baby = Person(self.size, self.screen, new_gen, 0, baby_address)
                               
                pop.append(baby)
                self.children += 1
            

                self.last_birth_age = 0

            self.last_birth_age += 1

    def grow(self, growth):
        self.age = self.age + growth

    def die(self, lisst, index):
        will_die = random.random()
        if self.age > 75:
            del(lisst[index])
            return 1
        elif will_die < 0.025:
            del(lisst[index])  
            return 1
        else:
            return 0

    def pos_neg(self):
        n = random.randint(0, 1)
        if n == 0:
            return -1
        else:
            return 1 
            
