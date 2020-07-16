import VideoCorona

breite = 100
personen = 3
zeit_infiziert = 10
infiziert = 2
inf_distanz = 7
inf_wahrscheinlichkeit = 0.3
max_kontakte = 0
abstandsregelung = 7
interval = 200

for i in range(15):
    abstandsregelung = i
    VideoCorona.simulation(breite, personen, zeit_infiziert,
           infiziert, inf_distanz,
           inf_wahrscheinlichkeit, max_kontakte,
           abstandsregelung, interval)
