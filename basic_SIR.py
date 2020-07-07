"""
Fun fact man kann auch mit Emojis programmieren (oder griechischen Buchstaben) 😉
"""

class SIR:
    def __init__(self, start_infected_percent: float, recovered_percent: float = 0.0, β: float = 0.5, 𝚫: float = 0.1):
        self.s = 1 - start_infected_percent - recovered_percent
        self.i = start_infected_percent
        self.r = recovered_percent
        self.β = β
        self.𝚫 = 𝚫
        self.t = 0

    def step(self) -> tuple:
        self.s = self.s - self.β * self.s * self.i
        self.i = self.i + self.β * self.s * self.i - self.𝚫 * self.i
        self.r = self.r + self.𝚫 * self.i
        self.t += 1
        return self.s, self.i, self.r

    def steps(self, count: int) -> tuple:
        susceptible = []
        infected = []
        recovered = []
        for i in range(count):
            output = self.step()
            susceptible.append(output[0])
            infected.append(output[1])
            recovered.append(output[2])
        return susceptible, infected, recovered