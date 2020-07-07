from matplotlib import pyplot as plt
ZEITSCHRITTE = 10

I_START = .1
R_START = 0

BETA = .5
DELTA = .1

s = 1 - I_START - R_START
i = I_START
r = R_START


print(str(s) +"; "+ str(i) +"; "+ str(r) +" gesamt: "+str(s+i+r))
xaxis = []
susceptible = []
infected = []
recovered = []
for index in range(100):
    xaxis.append(index)
    sNeu = s - BETA * s * i
    iNeu = i + BETA * s * i - DELTA * i
    rNeu = r + DELTA * i
    s = sNeu
    i = iNeu
    r = rNeu
    susceptible.append(s)
    infected.append(i)
    recovered.append(r)
    plt.plot(xaxis, susceptible, "k")
    plt.plot(xaxis, infected, "b")
    plt.plot(xaxis, recovered, "r")

plt.show()
