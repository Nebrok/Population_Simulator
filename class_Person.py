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
            pygame.draw.line(self.screen, BLACK, prev_pos, cur_pos, 4)
            prev_pos = cur_pos
            i += 1

            
        

class Person():
    
    def __init__(self, size, screen, generation, age, address):
        self.size = size
        self.screen = screen
        self.gen = generation
        self.age = age
        self.last_birth_age = 10
        self.address = address
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
                polarisation = 0
                y = r - x ** 2

                if y < 0:
                    y = y * -1
                else:
                    pass
                y = math.sqrt(y)
                baby_address = [self.address[0]+x*self.pos_neg(), self.address[1]+y*self.pos_neg()]

                baby = Person(self.size, self.screen, new_gen, 0, baby_address)


                x_pos = baby_address[0]
                y_pos = baby_address[1]

                if (x_pos < 0 or x_pos > 600):
                    baby_address[0] = abs(baby_address[0]-600)

                if (y_pos < 0 or y_pos > 600):
                    baby_address[1] = abs(baby_address[1]-600)

                baby.address = baby_address
                survive = random.random()

                if survive > 0.1:
                    pop.append(baby)
                    self.children += 1
                    return 0
                else:
                    return 1

                self.last_birth_age = 0

            else:
                return 0
            self.last_birth_age += 1
        else:
            return 0

    def grow(self, growth):
        self.age = self.age + growth

    def die(self, lisst, index):
        will_die = random.random()
        if self.age > 75:
            del(lisst[index])
            return 1
        elif will_die < 0.02:
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
            
