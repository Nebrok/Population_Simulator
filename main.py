import pygame
import math
import random
import class_Person
import class_Graph
import class_Predator

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    size = (1200,600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Population Simulator")


    done = False
    clock = pygame.time.Clock()
    screen.fill(WHITE)

    population = []
    pred_pop = []
    tick = 1
    year = 1
    total_tick = 0

    hit_list = 0
    pred_deaths = 0
    pred_kills = 0

    population_over_years = []

    gragh = class_Graph.Graph(size, screen)
    
    for i in range(10):
        random_address = (random.randint(0, size[0])/2, random.randint(0, size[1]))
        newPerson = class_Person.Person(size, screen, 1, 30, random_address)
        population.append(newPerson)

    for i in range(10):
        random_address = (random.randint(0, size[0])/2, random.randint(0, size[1]))
        newPred = class_Predator.Predator(size, screen, 1, 30, random_address)
        pred_pop.append(newPred)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print("A nasty plague has spread across the population")
                i = 0
                for person in population:
                    if i > 50:
                        del population[i]
                        hit_list += 1
                        i -= 1
                    i += 1
        
    
        for num in range(5):
            if tick == 10:
                for i in range(len(population)):
                    population[i].grow(1)

                for i in range(len(pred_pop)):
                    pred_pop[i].grow(1)

                for i in range(0, len(population), 2):
                    population[i].reproduce(population)

                for i in range(len(pred_pop)):
                    pred_pop[i].reproduce(pred_pop)

                pop_length = len(population)
                for i in range(pop_length-1, 0, -1): 
                    hit_list += population[i].die(population, i)

                pred_pop_length = len(pred_pop)
                for i in range(pred_pop_length-1, 0, -1):
                    pred_deaths += pred_pop[i].die(pred_pop, i)

                for i in range(len(pred_pop)):
                    pred_pop[i].kill(population)


                year += 1
                tick = 0
            tick += 1
            total_tick += 1
            if total_tick % 50 == 0:
                print("YEAR:", str(year))
                print("POPULATION: " + str(len(population)))
                print("HIT LIST:", hit_list)
                print("PREDATOR POPULATION: " + str(len(pred_pop)))
                print("PREDATOR DEATHS:", pred_deaths)
                #print("PREDATOR KILLS:", pred_kills)
            population_over_years.append(len(population))

        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, (600, 600), (600, 0), 2)
        gragh.draw(population_over_years)
        for person in population:
            person.draw()
        for pred in pred_pop:
            pred.draw()
        pygame.display.flip()
              

        #End of Loop
        clock.tick(30)


    pygame.quit()

main()
