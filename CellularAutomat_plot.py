import CellularAutomat
from matplotlib import pyplot as plt

steps = 100
CA = CellularAutomat.Simulation(100)

susceptible, infected, recovered = CA.steps(steps)
xaxis = list(range(steps))

plt.plot(xaxis, susceptible, "k")
plt.plot(xaxis, infected, "b")
plt.plot(xaxis, recovered, "r")
plt.show()
