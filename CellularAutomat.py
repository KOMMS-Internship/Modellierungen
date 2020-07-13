"""
Die Fuzziness ist präsentiert durch naughty die Zahl dieser Leute sollte langsam aber je mehr es sind immer schneller
wachsen besonders beschleunigt wird die Zahl durch Lockerungen
"""

import random


class HumanBeing:
    def __init__(self, simu, contact_restriction: int, infected: bool = False, naughty: bool = False,
                 immune: int = 0):
        self.naughty = naughty  # If someone if naughty he does not care about rules like contact restriction
        self.infected = infected
        self.contact_restriction = contact_restriction
        self.immunity = immune
        self.simu = simu
        self.step()

    def step(self):
        home = random.choice(self.simu.city)
        while not self.naughty:
            if len(home) < self.contact_restriction:
                break
            home = random.choice(self.simu.city)
        home.append(self)

        if self.immunity and self.immunity is not True:
            self.immunity -= 1  # There is the possibility to get susceptible again

        if self.infected and random.randint(0, int(self.simu.disinfection*100)) == 0:
            self.infected = False  # Getting recovered is probability driven
            self.immunity = self.simu.immunity_time


class Simulation:
    def __init__(self, persons: int, houses: int = 30, contact_restrictions: int = 0, infected_start: int = 1,
                 naughty_start: int = 1, recovered_start: int = 0, immunity_time: int = True,
                 disinfection_prob: float = 0.1, infection_prob: float = 0.9, vaccine_per_tick: int = 0,
                 naughty_plus: int = 2):
        """
        :param persons: Population which will be simulated
        :param houses: different places to go will get more complicated. Can also be seen as 2 meter square areas
        :param contact_restrictions: how many people are allowed to meet will be ignored by the naughty people
        :param infected_start: how much people are infected at the beginning
        :param naughty_start: how much people do not care about the rules at the beginning
        :param recovered_start: how much people are already immune
        :param immunity_time: how long are the people immune. Does the immunity even stop
        :param disinfection_prob: how high probability to recover and get immune
        :param infection_prob: how high is the probability to get infected by a person in one tick (1-)
        :param vaccine_per_tick: how many vaccines are available per tick
        :param naughty_plus: How many people get suddenly naughty if there is a positive change for them
        """
        if not contact_restrictions:
            contact_restrictions = persons
        if recovered_start + infected_start >= persons:
            raise Exception
        self.disinfection = disinfection_prob
        self.infection_prob = infection_prob
        self.immunity_time = immunity_time
        self.vaccine_per_tick = vaccine_per_tick
        self.naughty_plus = naughty_plus
        self.naughty = naughty_start
        self.houses = houses
        self.city = [[] for _ in range(self.houses)]  # Could also be interpreted as many 5 meter zones
        self.human_beings = [HumanBeing(self, contact_restrictions) for _ in range(persons)]
        for human in random.sample(self.human_beings, infected_start):
            # choosing people with special roles for the beginning
            human.infected = True
        for _ in range(naughty_start):
            human = random.choice(self.human_beings)
            timer = 0
            while human.naughty and timer != 2 * len(self.human_beings):
                human = random.choice(self.human_beings)
                timer += 1
            human.naughty = True
        for _ in range(recovered_start):
            human = random.choice(self.human_beings)
            while human.infected:
                human = random.choice(self.human_beings)
            human.immunity = immunity_time

        self.s = persons - infected_start - recovered_start
        self.i = infected_start
        self.r = recovered_start

    def step(self, change: bool = False) -> tuple:
        self.city = [[] for _ in range(self.houses)]

        if change:
            for _ in range(self.naughty_plus):
                human = random.choice(self.human_beings)
                timer = 0
                while human.naughty and timer != 2 * len(self.human_beings):
                    human = random.choice(self.human_beings)
                    timer += 1
                human.naughty = True

        for _ in range(self.naughty):
            human = random.choice(self.human_beings)
            timer = 0
            while human.naughty and timer != 2 * len(self.human_beings):
                human = random.choice(self.human_beings)
                timer += 1
            human.naughty = True

        for i in self.human_beings:
            i.step()

        for _ in range(self.vaccine_per_tick):
            human = random.choice(self.human_beings)
            while human.infected and human.immunity:
                human = random.choice(self.human_beings)
            human.immunity = self.immunity_time

        for house in self.city:
            states = [i.infected for i in house]
            if True in states:
                for i in house:
                    if random.randint(0, int(self.infection_prob * 100)) == 0 and not i.immunity:
                        i.infected = True

        self.s, self.i, self.r = 0, 0, 0  # Will be recalculated every step
        for index in self.human_beings:
            if index.infected:
                self.i += 1

        for index in self.human_beings:
            if index.immunity:
                self.r += 1
        self.s = (len(self.human_beings) - self.i) - self.r

        self.naughty = len([i.naughty for i in self.human_beings if i.naughty])

        return self.s, self.i, self.r, self.naughty

    def steps(self, steps):  # For plots mainly
        susceptible = []
        infected = []
        recovered = []
        naughty = []

        for i in range(steps):
            states = self.step()

            susceptible.append(states[0])
            infected.append(states[1])
            recovered.append(states[2])
            naughty.append(states[3])

        return susceptible, infected, recovered, naughty
