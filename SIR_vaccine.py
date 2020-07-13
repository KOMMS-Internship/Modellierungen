# -*- coding: utf8 -*-
"""
Fun fact man kann auch mit Emojis programmieren (oder griechischen Buchstaben) 😉
"""


class SIR:
    def __init__(self, start_infected_percent: float, recovered_percent: float = 0.0, β: float = 0.5, 𝚫: float = 0.1,
                 vaccine_percent: float = 0.0):
        """
        :param start_infected_percent: How many percent of the people are infected at the beginning of the simulation
        :param recovered_percent: how many percent of the people are immune at the beginning of the simulation
        :param β: Infection rate
        :param 𝚫: #Todo andresmatthias
        :param vaccine_percent: How many percent of the people get there vaccine per tick (might be very small)
        """
        self.s = 1 - start_infected_percent - recovered_percent
        self.i = start_infected_percent
        self.r = recovered_percent
        self.β = β
        self.𝚫 = 𝚫
        self.v = vaccine_percent
        self.t = 0

    def step(self) -> tuple:
        self.s = self.s - self.β * self.s * self.i * (1 - self.v)
        self.i = self.i + self.β * self.s * self.i * (1 - self.v) - self.𝚫 * self.i
        self.r = self.r + self.𝚫 * self.i
        self.t += 1
        return self.s, self.i, self.r

    def steps(self, count: int) -> tuple:
        susceptible = []
        infected = []
        recovered = []
        for _ in range(count):
            output = self.step()
            susceptible.append(output[0])
            infected.append(output[1])
            recovered.append(output[2])
        return susceptible, infected, recovered
