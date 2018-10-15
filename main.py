import pygame
import math
import random
import class_Person

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    size = (600,600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Population Simulator")


    done = False
    clock = pygame.time.Clock()
    screen.fill(BLACK)

    population = []
    tick = 1
    year = 1
    total_tick = 0
    
    for i in range(2):
        newPerson = class_Person.Person(1, 30)
        population.append(newPerson)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

        while year < 225:
            if tick == 30:
                for i in range(len(population)):
                    population[i].grow(1)
                for i in range(0, len(population), 2):
                    population[i].reproduce(population)
                pop_length = len(population)
                for i in range(pop_length-1, 0, -1): 
                    population[i].die(population, i)
                year += 1
                tick = 0
                total_tick += 1
            tick = tick + 1
            total_tick += 1
            
            
        done = True




        #End of Loop
        pygame.display.flip()
        clock.tick(15)

    print(len(population))
    print(total_tick)


    pygame.quit()

main()



qoot = False
while not qoot:
    input("Press q to quit: ")
    if x == q:
        qoot = True
