import CellularAutomat
from matplotlib import pyplot as plt

steps = 100
persons = 100
houses = 30
contact_restrictions = 4  # If no restriction planned set to 0
infected_start = 1
naughty_start = 1
recovered_start = 0
immunity_time = True  # Never expires
disinfection_prob = 1-0.1
infection_prob = 0.09

CA = CellularAutomat.Simulation(persons, houses, contact_restrictions, infected_start, naughty_start, recovered_start, immunity_time, disinfection_prob, infection_prob)

susceptible, infected, recovered = CA.steps(steps)
xaxis = list(range(steps))

plt.plot(xaxis, susceptible, "k", label="susceptible")
plt.plot(xaxis, infected, "b", label="infected")
plt.plot(xaxis, recovered, "r", label="recovered")
plt.legend()
plt.title("COVID-19 simulation")
plt.xlabel("time")
plt.ylabel("people")
plt.show()
