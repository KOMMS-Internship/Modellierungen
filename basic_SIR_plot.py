from matplotlib import pyplot as plt
import basic_SIR

steps = 100
SIR = basic_SIR.SIR(0.1)

susceptible, infected, recovered = SIR.steps(steps)
xaxis = list(range(steps))

plt.plot(xaxis, susceptible, "k")
plt.plot(xaxis, infected, "b")
plt.plot(xaxis, recovered, "r")
plt.show()