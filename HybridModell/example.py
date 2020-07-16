from hybrid_main import *

# Anzahl an Simulationsschritten
SIMULATIONS_DAUER = 100

# Anzahl an Personen insgesamt
personen = 1000
# Anzahl an Personen, die sich an die Kontaktbeschränkungen halten
befolgend = 500
# Anzahl an Personen, die zu Beginn infiziert sind
infiziert = 20
# Anzahl an Personen, die zu Beginn bereits genesen sind
genesen = 0
# maximale Gruppengröße, die erlaubt ist
erlaubteGruppen = 2
# Rate, mit der infizierte Personen gesunde infizieren
infektionsRate = 0.3
# Rate, mit der infizierte genesen
genesungsRate = 0.1
# Raten für den zweiten SIR Durchlauf. Kann auf 0 gesetzt werden, um diesen wirkungslos zu machen
beta2 = 0.05
gamma2 = 0

# Welche Kurven sollen gezeigt werden
zeige_gesamt = True
zeige_befolgend = True
zeige_nichtbefolgend = True

simuliere(personen, befolgend, infiziert, genesen, erlaubteGruppen, infektionsRate, genesungsRate, beta2, gamma2, SIMULATIONS_DAUER,
          zeige_gesamt, zeige_befolgend, zeige_nichtbefolgend)
