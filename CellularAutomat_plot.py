import CellularAutomat

CA = CellularAutomat.Simulation(100)

for i in range(0, 100):
    print(CA.step())