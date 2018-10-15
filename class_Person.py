import random

class Person():
    
    def __init__(self, generation, age):
        self.gen = generation
        self.age = age
        self.last_birth_age = 10


    def reproduce(self, pop):
        if self.age >= 16:
            if self.last_birth_age > 2:
                new_gen = self.gen + 1
                baby = Person(new_gen, 0)

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
            
