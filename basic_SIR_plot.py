from matplotlib import pyplot as plt
import basic_SIR

steps = 100
SIR = basic_SIR.SIR(0.1)

susceptible, infected, recovered = SIR.steps(steps)
xaxis = list(range(steps))

plt.plot(xaxis, susceptible, "k", label="susceptible")
plt.plot(xaxis, infected, "b", label="infected")
plt.plot(xaxis, recovered, "r", label="recovered")
plt.legend()
plt.title("COVID-19 simulation")
plt.xlabel("time")
plt.ylabel("percentage")
plt.show()