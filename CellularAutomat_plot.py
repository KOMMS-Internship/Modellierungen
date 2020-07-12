import CellularAutomat
from matplotlib import pyplot as plt

steps = 300
persons = 100
houses = 30
contact_restrictions = 0  # If no restriction planned set to 0
infected_start = 1
naughty_start = 2
recovered_start = 0
immunity_time = True  # Never expires
disinfection_prob = 1-0.1
infection_prob = 1-0.9
vaccine_per_tick = 2
naughty_plus = 2

health_system_border = 10

CA = CellularAutomat.Simulation(persons, houses, contact_restrictions, infected_start, naughty_start, recovered_start,
                                immunity_time, disinfection_prob, infection_prob, vaccine_per_tick, naughty_plus)

susceptible, infected, recovered, naughty = CA.steps(steps)
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
