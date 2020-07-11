import numpy as np
from matplotlib import pyplot as plt
import random

startx = 0
starty = 0
breite = 100
personen = 100
zeit = 500
zeit_infiziert = 90
infiziert = 2
inf_distanz = 7
inf_wahrscheinlichkeit = 0.9


feld = np.zeros((breite, breite))
feld = feld.astype(int)
gesunde = [personen - infiziert]
infizierte = [infiziert]
genesene = [0]


class Person:
    def __init__(self, x, y, zustand, infcounter):
        self.x = x
        self.y = y
        self.zustand = zustand
        self.infcounter = infcounter

    def bewegen(self):
        richtung = random.randint(1,4)
        if richtung == 1:
            self.x += 1
        elif richtung == 2:
            self.x -= 1
        elif richtung == 3:
            self.y += 1
        elif richtung == 4:
            self.y -= 1


def erzeuge_rand():
    b = breite/2
    seite = [-b, b]
    unten = [-b, -b]
    oben = [b, b]
    plt.plot(seite, unten,"b")
    plt.plot(seite, oben,"b")
    plt.plot(unten, seite,"b")
    plt.plot(oben, seite,"b")
    plt.show()

def anfangspos():
    b = breite/2
    for i in range(len(liste)):
        verteilt = False
        while verteilt == False:
            a = random.randint(0, b * 2-1)
            c = random.randint(0, b * 2-1)
            if feld[a, c] == 0:
                feld[a, c] = 1
                verteilt = True
                a2 = a - b
                c2 = c - b
                liste[i].x = c2
                liste[i].y = a2
                #print(liste[i].x, liste[i].y)
                if liste[i].zustand == 1:
                    plt.plot(c2, a2, "rs")
                elif liste[i].zustand == 0:
                    plt.plot(c2, a2, "ys")
            else:
                pass


def anf_infizieren():
    for i in range(infiziert):
        liste[i].zustand = 1


def infizieren():
    for i in range(personen):
        for k in range(personen):
            if liste[i].zustand == 1:
                if liste[k].zustand == 0 and liste[i].x - liste[k].x <= inf_distanz and liste[i].x - liste[k].x >= -inf_distanz and liste[i].y - liste[k].y <= inf_distanz and liste[i].y - liste[k].y >= -inf_distanz:
                    a = random.random()
                    if a <= inf_wahrscheinlichkeit:
                        liste[k].zustand = 1
                    else:
                        pass
                else:
                    pass
            else:
                pass


def infzeit():
    for i in range(personen):
        if liste[i].zustand == 1:
            liste[i].infcounter += 1


def genesen():
    for i in range(personen):
        if liste[i].infcounter >= zeit_infiziert:
            liste[i].zustand = 2


def schritt():
    for i in range(personen):
        liste[i].bewegen()


def plot():
    for i in range(personen):
        if liste[i].zustand == 1:
            plt.plot(liste[i].x, liste[i].y, "rs")
        elif liste[i].zustand == 0:
            plt.plot(liste[i].x, liste[i].y, "ys")
        elif liste[i].zustand == 2:
            plt.plot(liste[i].x, liste[i].y, "bs")


def graph():
    zaehlerg = 0
    zaehleri = 0
    zaehlerr = 0
    for i in range(personen):
        if liste[i].zustand == 0:
            zaehlerg += 1
        elif liste[i].zustand == 1:
            zaehleri += 1
        elif liste[i].zustand == 2:
            zaehlerr += 1
    gesunde.append(zaehlerg)
    infizierte.append(zaehleri)
    genesene.append(zaehlerr)
        

liste = []
for i in range(personen):
    liste.append(Person(startx,starty, 0, 0))


anf_infizieren()
anfangspos()
plt.show
for i in range(zeit):
    erzeuge_rand()
    schritt()
    infizieren()
    infzeit()
    genesen()
    plot()
    graph()

    
plt.clf()
plt.plot(gesunde)
plt.plot(infizierte)
plt.plot(genesene)
plt.show()
