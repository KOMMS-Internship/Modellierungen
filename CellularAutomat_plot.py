import CellularAutomat
from matplotlib import pyplot as plt

steps = 100
CA = CellularAutomat.Simulation(100)

susceptible, infected, recovered = CA.steps(steps)
xaxis = list(range(steps))

plt.plot(xaxis, susceptible, "k", label="susceptible")
plt.plot(xaxis, infected, "b", label="infected")
plt.plot(xaxis, recovered, "r", label="recovered")
plt.legend()
plt.title("COVID-19 Simulation")
plt.show()
