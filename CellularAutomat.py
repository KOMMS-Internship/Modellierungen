"""
Die Fuzziness ist präsentiert durch naughty die Zahl dieser Leute sollte langsam aber je mehr es sind immer schneller
wachsen besonders beschleunigt wird die Zahl durch Lockerungen
"""

import random
import sys


class HumanBeing:
    def __init__(self, simu, contact_restriction: int, infected: bool = False, naughty: bool = False,
                 immune: int = 0):
        self.naughty = naughty
        self.infected = infected
        self.contact_restriction = contact_restriction
        self.immunity = immune
        self.simu = simu
        self.step()

    def step(self):
        home = random.choice(self.simu.city)
        while not self.naughty:
            if len(home) <= self.contact_restriction:
                break
            home = random.choice(self.simu.city)
        home.append(self)

        if self.immunity:
            self.immunity -= 1

        if self.infected and random.randint(0, self.simu.disinfection) == 0:
            self.infected = False
            self.immunity = self.simu.immunity_time


class Simulation:
    def __init__(self, persons: int, houses: int = 10, contact_restrictions: int = 0, infected_start: int = 1,
                 naughty_start: int = 1, recovered_start: int = 0, immunity_time: int = sys.maxsize,
                 disinfection_prob: int = 5, infection_prob: int = 0.9):
        if not contact_restrictions:
            contact_restrictions = persons
        self.disinfection = disinfection_prob
        self.infection_prob = infection_prob
        self.immunity_time = immunity_time
        self.houses = houses
        self.city = [[] for _ in range(self.houses)]
        self.human_beings = [HumanBeing(self, contact_restrictions) for _ in range(persons)]
        for _ in range(infected_start):
            random.choice(self.human_beings).infected = True
        for _ in range(naughty_start):
            random.choice(self.human_beings).naughty = True
        for _ in range(recovered_start):
            human = random.choice(self.human_beings)
            while human.infected:
                human = random.choice(self.human_beings)
            human.immunity = immunity_time

        self.s = persons - infected_start - recovered_start
        self.i = infected_start
        self.r = recovered_start

    def step(self) -> tuple:
        self.s, self.i, self.r = 0, 0, 0
        for index in self.human_beings:
            if index.infected:
                self.i += 1

        for index in self.human_beings:
            if index.immunity:
                self.r += 1
        self.s = (len(self.human_beings) - self.i) - self.r

        self.city = [[] for _ in range(self.houses)]

        for i in self.human_beings:
            i.step()

        for house in self.city:
            states = [i.infected for i in house]
            if True in states:
                for i in house:
                    if random.randint(0, int(self.infection_prob*10)) == 1 and not i.immunity:
                        i.infected = True

        return self.s, self.i, self.r

    def steps(self, steps):
        susceptible = []
        infected = []
        recovered = []

        for i in range(steps):
            states = self.step()

            susceptible.append(states[0])
            infected.append(states[1])
            recovered.append(states[2])

        return susceptible, infected, recovered
