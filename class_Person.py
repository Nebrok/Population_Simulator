import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Graph():
    def __init__(self, res, screen):
        self.res = res
        self.screen = screen
        #if self.lisst % 2 != 0:
        #    self.lisst.pop[0]

    def draw(self, lisst):
        #line(Surface, color, start_pos, end_pos, width=1) -> Rec
        #if prev_pos[0] > res[0]:
        #    pass
            
        prev_pos = (self.res[0]/2, self.res[1])
        i = 0
        for population in lisst:
            cur_pos = (self.res[0]/2+i/8, self.res[1]-population/100)
            pygame.draw.line(self.screen, BLACK, prev_pos, cur_pos, 4)
            prev_pos = cur_pos
            i += 1
            
        

class Person():
    
    def __init__(self, size, screen, generation, age):
        self.size = size
        self.screen = screen
        self.gen = generation
        self.age = age
        self.last_birth_age = 10
        self.address = (random.randint(0, size[0])/2, random.randint(0, size[1]))
        self.children = 0

    def draw(self):
        pygame.draw.rect(self.screen, BLACK, (self.address[0], self.address[1], 1, 1))

    def reproduce(self, pop):
        if self.age >= 20 and self.age <= 45 and self.children <= 3:
            if self.last_birth_age > 4:
                new_gen = self.gen + 1
                baby = Person(self.size, self.screen, new_gen, 0)
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
            
            
