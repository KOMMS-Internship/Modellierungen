import numpy as np
from matplotlib import pyplot as plt
import random
from matplotlib.animation import FuncAnimation

breite = 100
personen = 100
zeit = 150
zeit_infiziert = 50
infiziert = 2
inf_distanz = 7
inf_wahrscheinlichkeit = 0.3
max_kontakte = 50
abstandsregelung = 0


startx = 0
starty = 0
feld = np.zeros((breite, breite))
feld = feld.astype(int)
gesunde = [personen - infiziert]
infizierte = [infiziert]
genesene = [0]


class Person:
    def __init__(self, x, y, zustand, infcounter, regeln, bewegt, grenze):
        self.x = x
        self.y = y
        self.zustand = zustand
        self.infcounter = infcounter
        self.regeln = regeln
        self.bewegt = bewegt
        self.grenze = grenze

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


def grenze_berührt():
    b = breite / 2
    for i in range(personen):
        if liste[i].x >= b or liste[i].x <= -b or liste[i].y >= b or liste[i].y <= -b:
            liste[i].grenze = 1
            if liste[i].x >= b:
                liste[i].x -= 1
            elif liste[i].x <= -b:
                liste[i].x += 1
            elif liste[i].y >= b:
                liste[i].y -= 1
            elif liste[i].y <= b:
                liste[i].y += 1
        else:
            liste[i].grenze = 0
    

def anfangspos():
    fig, ax = plt.subplots()
    anz_personen = len(liste)
    
    bild_matrix = np.NaN * np.ones((anz_personen, anz_personen))
    cmap = plt.get_cmap('jet')
    bild = ax.imshow(bild_matrix, vmin=0, vmax = 2, cmap=cmap)
    fig.colorbar(bild, ax=ax)
    
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
#                    plt.plot(c2, a2, "rs")
                    bild_matrix[a, c] = 1
                elif liste[i].zustand == 0:
#                    plt.plot(c2, a2, "ys")
                    bild_matrix[a, c] = 0
            else:
                pass
    
    bild.set_array(bild_matrix)
            
    return fig, ax, bild, b


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
        #print(liste[i].bewegt, "bewegt", liste[i].grenze, "grenze")
        if liste[i].bewegt == 0 and liste[i].grenze == 0:
            liste[i].bewegen()
        else:
            liste[i].grenze = 0
            liste[i].bewegt = 0


def kontaktbeschraenkung():
    for i in range(personen):
        if liste[i].grenze == 0:
            zaehler = 0
            for k in range(personen):
                if liste[i].x - liste[k].x <= abstandsregelung and liste[i].x - liste[k].x >= -abstandsregelung and liste[i].y - liste[k].y <= abstandsregelung and liste[i].y - liste[k].y >= -abstandsregelung:
                    zaehler += 1
                    #Ab hier sind Fehler drinnen. Wenn man max_kontakte ganz hoch stellt, wird das nicht ausgeführt und das Programm läuft normal.
                    if zaehler >= max_kontakte:
                        liste[k].bewegt = 1
                        if abs(liste[i].x - liste[k].x) < abs(liste[i].y - liste[k].y):
                            if liste[i].y - liste[k].y < 0:
                                liste[k].y += 1
                            elif liste[i].y - liste[k].y > 0:
                                liste[k].y -= 1
                        elif abs(liste[i].x - liste[k].x) > abs(liste[i].y - liste[k].y):
                            if liste[i].x - liste[k].x < 0:
                                liste[k].x += 1
                            elif liste[i].x - liste[k].x > 0:
                                liste[k].x -= 1
                        elif abs(liste[i].x - liste[k].x) == abs(liste[i].y - liste[k].y):
                            a = random.random()
                            if a < 0.5:
                                if liste[i].y - liste[k].y < 0:
                                    liste[k].y += 1
                                elif liste[i].y - liste[k].y > 0:
                                    liste[k].y -= 1
                            else:
                                if liste[i].x - liste[k].x < 0:
                                    liste[k].x += 1
                                elif liste[i].x - liste[k].x > 0:
                                    liste[k].x -= 1
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
                            
                        

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
    liste.append(Person(startx,starty, 0, 0, 0, 0, 0))


anf_infizieren()
fig, ax, bild, b = anfangspos()
plt.show
#for i in range(zeit):
    #erzeuge_rand()
    #grenze_berührt()
    #kontaktbeschraenkung()
    #schritt()
    #infizieren()
    #infzeit()
    #genesen()
    #plot()
    #graph()

#    
#plt.clf()
#plt.plot(gesunde)
#plt.plot(infizierte)
#plt.plot(genesene)
#plt.show()
#
#
## Figure initialisieren
#fig, ax = plt.subplots()
#ax.set(xlim=(0,1), ylim=(0,1))
#
#N = 20
#x = np.zeros(N)
#y = np.zeros(N)
#line = ax.plot(x, y, 'bo')[0]
## man könnte auch scatter verwenden
#
#anf_infizieren()
#anfangspos()
#plt.show
#

def animate(i):
    """Diese Funktion wird in der Schleife ausgefuehrt."""
    
#    erzeuge_rand()
    grenze_berührt()
    kontaktbeschraenkung()
    schritt()
    infizieren()
    infzeit()
    genesen()
#    plot()
#    graph()
    
    bild_matrix = np.NaN * np.ones((int(2 * b)+1, int(2 * b)+1))
    
    for i in range(len(liste)):
        bild_matrix[int(liste[i].y + b), int(liste[i].x + b)] = liste[i].zustand
    
    bild.set_array(bild_matrix)
    print(np.max(bild.get_array()))
#
#
#    
anim = FuncAnimation(fig, animate, interval=200)  #interval: ms between two frames 
plt.draw()
plt.show()
