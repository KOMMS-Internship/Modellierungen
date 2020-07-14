import random


class HumanBeing:
    def __init__(self, simulation, contact_restriction: int, infected: bool = False, naughty: bool = False,
                 immune: int = 0):
        self.naughty = naughty  # If someone if naughty he does not care about rules like contact restriction
        self.infected = infected
        self.contact_restriction = contact_restriction
        self.immunity = immune
        self.simulation = simulation
        self.step()

    def step(self):
        random.choice([home for home in self.simulation.city if len(home) < self.contact_restriction]).append(self)

        if self.immunity and self.immunity is not True:
            self.immunity -= 1  # There is the possibility to get susceptible again

        if self.infected and random.randint(0, int(self.simulation.disinfection * 100)) == 0:
            self.infected = False  # Getting recovered is probability driven
            self.immunity = self.simulation.immunity_time


class Simulation:
    def __init__(self, persons: int, houses: int = 30, contact_restrictions: int = 0, infected_start: int = 1,
                 naughty_start: int = 1, recovered_start: int = 0, immunity_time: int = True,
                 disinfection_prob: float = 0.1, infection_prob: float = 0.9, vaccine_per_tick: int = 0,
                 naughty_plus: int = 2, naughty_plus_percent: float = 0.5):
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
        :param naughty_plus_percent: Calculates how many people are naughty in the next step
        """
        if not contact_restrictions:
            contact_restrictions = persons
        if recovered_start + infected_start > persons:
            raise OverflowError("More immune and infected people than the sum of all people")
        self.disinfection = disinfection_prob
        self.infection_prob = infection_prob
        self.immunity_time = immunity_time
        self.vaccine_per_tick = vaccine_per_tick
        self.naughty_plus = naughty_plus
        self.naughty = naughty_start
        self.naughty_plus_percent = naughty_plus_percent
        self.houses = houses
        self.city = [[] for _ in range(self.houses)]  # Could also be interpreted as many 5 meter zones
        self.human_beings = [HumanBeing(self, contact_restrictions) for _ in range(persons)]
        for human in random.sample(self.human_beings, infected_start):
            # choosing people with special roles for the beginning
            human.infected = True
        for human in random.sample(self.human_beings, naughty_start):
            human.naughty = True
        for human in random.sample([human for human in self.human_beings if not human.infected], recovered_start):
            human.immunity = immunity_time
        """for _ in range(recovered_start):
            human = random.choice(self.human_beings)
            while human.infected:
                human = random.choice(self.human_beings)
            human.immunity = immunity_time"""

        self.s = persons - infected_start - recovered_start
        self.i = infected_start
        self.r = recovered_start

    def step(self, change: bool = False) -> tuple:
        for i in self.human_beings:
            i.step()

        if change:
            try:
                for human in random.sample([human for human in self.human_beings if not human.naughty],
                                           self.naughty_plus):
                    human.naughty = True
            except ValueError:
                pass

        naughty_plus = self.naughty * self.naughty_plus_percent
        if naughty_plus < 1:
            naughty_plus = 1
        if naughty_plus + self.naughty >= 0.9 * len(self.human_beings):
            naughty_plus = 0
        try:
            for human in random.sample([human for human in self.human_beings if not human.naughty], naughty_plus):
                human.naughty = True
        except ValueError:
            pass

        try:
            for human in random.sample([human for human in self.human_beings
                                        if not human.immunity and not human.infected], self.vaccine_per_tick):
                human.immunity = self.immunity_time
        except ValueError:
            pass

        for house in self.city:
            states = [i.infected for i in house]
            if True in states:
                for i in house:
                    if random.randint(0, int(self.infection_prob * 100)) == 0 and not i.immunity:
                        i.infected = True

        self.s, self.i, self.r = 0, 0, 0  # Will be recalculated every step

        self.i = len([infected for infected in self.human_beings if infected.infected])
        self.r = len([recovered for recovered in self.human_beings if recovered.immunity])
        self.s = (len(self.human_beings) - self.i) - self.r

        self.naughty = len([naughty for naughty in self.human_beings if naughty.naughty])

        self.city = [[] for _ in range(self.houses)]

        return self.s, self.i, self.r, self.naughty

    def steps(self, steps):  # For plots mainly
        susceptible, infected, recovered, naughty = [], [], [], []

        for _ in range(steps):
            states = self.step()

            susceptible.append(states[0])
            infected.append(states[1])
            recovered.append(states[2])
            naughty.append(states[3])

        return susceptible, infected, recovered, naughty
