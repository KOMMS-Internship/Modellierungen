"""
Die Fuzziness ist präsentiert durch naughty die Zahl dieser Leute sollte langsam aber je mehr es sind immer schneller
wachsen besonders beschleunigt wird die Zahl durch Lockerungen
"""

import random
import sys


class HumanBeing:
    def __init__(self, city: list, contact_restriction: int, infected: bool = False, naughty: bool = False,
                 immune: int = 0):
        self.naughty = naughty
        self.infected = infected
        self.city = city
        self.contact_restriction = contact_restriction
        self.immunity = immune
        self.step()

    def step(self):
        while not self.naughty:
            home = random.choice(self.city)
            if len(home) < self.contact_restriction:
                home.inhabitants.append(self)
                break

        if self.immunity:
            self.immunity -= 1

        if self.infected and random.randint(0, 5) == 0:
            self.infected = False

class Simulation:
    def __init__(self, persons: int, houses: int = 30, contact_restrictions: int = 0, infected_start: int = 1,
                 naughty_start: int = 1, recovered_start: int = 0, immunity_time:int = sys.maxsize):
        if not contact_restrictions:
            contact_restrictions = persons
        self.houses = houses
        self.city = [[] for _ in range(self.houses)]
        self.human_beings = [HumanBeing(self.city, contact_restrictions) for _ in range(persons)]
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
            if index.immune:
                self.r += 1
        self.s = len(self.human_beings) - self.i - self.r

        self.city = [[] for _ in range(self.houses)]

        for i in self.human_beings:
            i.step()