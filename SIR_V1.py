ZEITSCHRITTE = 10

I_START = .1
R_START = 0

BETA = .5
DELTA = .1

s = 1 - I_START - R_START
i = I_START
r = R_START


print(str(s) +"; "+ str(i) +"; "+ str(r) +" gesamt: "+str(s+i+r))
for index in range(10):
    sNeu = s - BETA * s * i
    iNeu = i + BETA * s * i - DELTA * i
    rNeu = r + DELTA * i
    s = sNeu
    i = iNeu
    r = rNeu
    print(str(s) +"; "+ str(i) +"; "+ str(r) +" gesamt: "+str(s+i+r))