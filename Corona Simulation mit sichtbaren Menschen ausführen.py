# abstand = sqrt( Δx ** 2 + Δy ** 2 )



import VideoCorona

breite = 100
personen = 3
zeit_infiziert = 100
infiziert = 2
inf_distanz = 10
inf_wahrscheinlichkeit = 0.3
max_kontakte = 0
abstandsregelung = 8
interval = 1
zeige_graph = True



VideoCorona.simulation(breite, personen, zeit_infiziert,
    infiziert, inf_distanz,
    inf_wahrscheinlichkeit, max_kontakte,
    abstandsregelung, interval, zeige_graph)
