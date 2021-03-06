from matplotlib import pyplot as plt
import SIR_vaccine

steps = 100
SIR = SIR_vaccine.SIR(0.1)

susceptible, infected, recovered = SIR.steps(steps)
xaxis = list(range(steps))
sum = [susceptible[i] + infected[i] + recovered[i] for i in xaxis]
plt.plot(xaxis, susceptible, "k", label="susceptible")
plt.plot(xaxis, infected, "b", label="infected")
plt.plot(xaxis, recovered, "r", label="recovered")
plt.plot(xaxis, sum, "g", label="sum")
plt.legend()
plt.title("COVID-19 simulation")
plt.xlabel("time")
plt.ylabel("percentage")
plt.show()