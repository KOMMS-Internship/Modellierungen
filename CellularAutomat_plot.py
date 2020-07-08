import CellularAutomat
import sys
from matplotlib import pyplot as plt

steps = 100
persons = 100
houses = 30
contact_restrictions = 0
infected_start = 1
naughty_start = 1
recovered_start = 0
immunity_time = sys.maxsize
disinfection_prob = 5
infection_prob = 0.9

CA = CellularAutomat.Simulation(persons, houses, contact_restrictions, infected_start, naughty_start, recovered_start, immunity_time, disinfection_prob, infection_prob)

susceptible, infected, recovered = CA.steps(steps)
xaxis = list(range(steps))

plt.plot(xaxis, susceptible, "k", label="susceptible")
plt.plot(xaxis, infected, "b", label="infected")
plt.plot(xaxis, recovered, "r", label="recovered")
plt.legend()
plt.title("COVID-19 Simulation")
plt.show()
