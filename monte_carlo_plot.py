import CellularAutomat
from matplotlib import pyplot as plt

monte_carlo = 100
steps = 100
persons = 100
houses = 30
contact_restrictions = 0  # If no restriction planned set to 0
infected_start = 1
naughty_start = 2
recovered_start = 0
immunity_time = True  # Never expires
disinfection_prob = 1-0.1
infection_prob = 1-0.9
vaccine_per_tick = 0
naughty_plus = 2
naughty_plus_percent = 0.01

health_system_border = 10

susceptible = [0 for _ in range(steps)]
infected = [0 for _ in range(steps)]
recovered = [0 for _ in range(steps)]
naughty = [0 for _ in range(steps)]

for simulation in range(monte_carlo):
    CA = CellularAutomat.Simulation(persons, houses, contact_restrictions, infected_start, naughty_start, recovered_start,
                                    immunity_time, disinfection_prob, infection_prob, vaccine_per_tick, naughty_plus,
                                    naughty_plus_percent)

    states = CA.steps(steps)
    susceptible = [susceptible[i] + states[0][i] for i in range(steps)]
    infected = [infected[i] + states[1][i] for i in range(steps)]
    recovered = [recovered[i] + states[2][i] for i in range(steps)]
    naughty = [naughty[i] + states[3][i] for i in range(steps)]

susceptible = [i/monte_carlo for i in susceptible]
infected = [i/monte_carlo for i in infected]
recovered = [i/monte_carlo for i in recovered]
naughty = [i/monte_carlo for i in naughty]

xaxis = list(range(steps))
health_system = [health_system_border for _ in range(steps)]

plt.plot(xaxis, health_system, "o", label="health system border")
plt.plot(xaxis, susceptible, "k", label="susceptible")
plt.plot(xaxis, infected, "b", label="infected")
plt.plot(xaxis, recovered, "g", label="recovered")
plt.plot(xaxis, naughty, "r", label="naughty")
plt.legend()
plt.title("COVID-19 simulation")
plt.xlabel("time")
plt.ylabel("people")
plt.show()
