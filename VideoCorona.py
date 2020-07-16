import numpy as np
from matplotlib import pyplot as plt
import random
from matplotlib.animation import FuncAnimation
import sys


def simulation(breite, personen, zeit_infiziert, infiziert, inf_distanz, inf_wahrscheinlichkeit, max_kontakte, abstandsregelung, interval):
    startx = 0
    starty = 0
    feld = np.zeros((breite, breite))
    feld = feld.astype(int)
    gesunde = [personen - infiziert]
    infizierte = [infiziert]
    genesene = [0]
    listex = []
    listey = []


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
        
        bild_matrix = np.NaN * np.ones((breite, breite))
        cmap = plt.get_cmap('jet')
        bild = ax.imshow(bild_matrix, vmin=0, vmax = 2, cmap=cmap)
        fig.colorbar(bild, ax=ax)
        
        b = breite/2
        #print(len(liste))
        
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
                        #print(a, c, b)
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


#Problem, wenn Person an der Grenze ist. Wenn Person an Grenze ist, kann er auch die Achse wechseln, an der er sich bewegt.
    def kontaktbeschraenkung():
        for i in range(personen):
            liste[i].bewegt = 0
            abstand = []
            abstandx = []
            abstandy = []
            zaehler = 0
            for k in range(personen):
                distanz = np.sqrt((liste[i].x - liste[k].x) ** 2 + (liste[i].y - liste[k].y) ** 2)
                if distanz <= abstandsregelung and i != k:
                    zaehler += 1
                    liste[i].bewegt = 1
                    abstandx.append(liste[i].x - liste[k].x)
                    abstandy.append(liste[i].y - liste[k].y)
                    abstand.append(distanz)
        

            if liste[i].bewegt == 1:
                mindist = min(abstand)
                argmindist = np.argmin(abstand)
                if abstandx[argmindist] < abstandy[argmindist]:
                    if liste[i].grenze == 0:
                        if abstandy[argmindist] < 0:
                            liste[i].y -= 1
                        else:
                            liste[i].y += 1
                    else:
                        if abstandx[argmindist] < 0:
                            liste[i].x -= 1
                        else:
                            liste[i].x += 1
                else:
                    if liste[i].grenze == 0:
                        if abstandx[argmindist] < 0:
                            liste[i].x -= 1
                        else:
                            liste[i].x += 1
                    else:
                        if abstandy[argmindist] < 0:
                            liste[i].y -= 1
                        else:
                            liste[i].y += 1
            








##        for i in range(personen):
##            listey = []
##            listex = []
##            listek = []
##            if liste[i].grenze == 0:
##                zaehler = 0
##                xzaehler = -1
##                yzaehler = -1
##                for k in range(personen):
##                    if i != k:
##                        if abs(liste[i].x - liste[k].x) <= abstandsregelung and abs(liste[i].y - liste[k].y) <= abstandsregelung:
##                        
##                            liste[i].bewegt = 1
##                            listex.append( abs(liste[i].x - liste[k].x) )
##                            listey.append( abs(liste[i].y - liste[k].y) )
##                            listek.append(k)
##                            
##                xmin = min(listex)
##                ymin = min(listey)
##                #print(listex, listey, i)
##                for o in listex:
##                    xzaehler += 1
##                    if o == xmin:
##                        break
##
##                for o in listey:
##                    yzaehler += 1
##                    if o == ymin:
##                        break
##
##                k1 = listek[xzaehler]
##                k2 = listek[yzaehler]
##
##
##
##
##
##                if xmin < ymin:
##                    if liste[i].y - liste[k2].y < 0:
##                        liste[i].y -= 1
##                    else:
##                        liste[i].y += 1
##                elif xmin > ymin:
##                    if liste[i].x - liste[k1].x < 0:
##                        liste[i].x -= 1
##                    else:
##                        liste[i].x += 1
##                else:
##                    c = random.random()
##                    if c < 0.5:
##                        if liste[i].y - liste[k2].y < 0:
##                            liste[i].y -= 1
##                        else:
##                            liste[i].y += 1
##                    else:
##                        if liste[i].x - liste[k1].x < 0:
##                            liste[i].x -= 1
##                        else:
##                            liste[i].x += 1








        
                                
##                        zaehler += 1
##                        #Ab hier sind Fehler drinnen. Wenn man max_kontakte ganz hoch stellt, wird das nicht ausgeführt und das Programm läuft normal.
##                        if zaehler >= max_kontakte and liste[k].bewegt == 0:
##                            liste[k].bewegt = 1
##                            if abs(liste[i].x - liste[k].x) < abs(liste[i].y - liste[k].y):
##                                if liste[i].y - liste[k].y < 0:
##                                    liste[k].y += 1
##                                elif liste[i].y - liste[k].y > 0:
##                                    liste[k].y -= 1
##                            elif abs(liste[i].x - liste[k].x) > abs(liste[i].y - liste[k].y):
##                                if liste[i].x - liste[k].x < 0:
##                                    liste[k].x += 1
##                                elif liste[i].x - liste[k].x > 0:
##                                    liste[k].x -= 1
##                            elif abs(liste[i].x - liste[k].x) == abs(liste[i].y - liste[k].y):
##                                a = random.random()
##                                if a < 0.5:
##                                    if liste[i].y - liste[k].y < 0:
##                                        liste[k].y += 1
##                                    elif liste[i].y - liste[k].y > 0:
##                                        liste[k].y -= 1
##                                else:
##                                    if liste[i].x - liste[k].x < 0:
##                                        liste[k].x += 1
##                                    elif liste[i].x - liste[k].x > 0:
##                                        liste[k].x -= 1
##                            else:
##                                pass
##                        else:
##                            pass
##                    else:
##                        pass
                                
                            

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
    l1 = []
    l2 = []
    l3 = []

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
        graph()
        
        bild_matrix = np.NaN * np.ones((int(2 * b)+2, int(2 * b)+2))
        

        l1 = []
        l2 = []
        l3 = []
        
        for i in range(len(liste)):
            #print(liste[i].y + b, liste[i].x + b)
            bild_matrix[int(liste[i].y + b), int(liste[i].x + b)] = liste[i].zustand
            if liste[i].zustand == 0:
                l1.append(i)
            elif liste[i].zustand == 1:
                l2.append(i)
            elif liste[i].zustand == 2:
                l3.append(i)
        if len(l2) == 0:
            plt.close(fig)
            return max(li)

        li.append(len(l2))
        #print(len(l1),len(l2),len(l3))
        bild.set_array(bild_matrix)
        #print(np.max(bild.get_array()))

    #
    #
    li = []

    anim = FuncAnimation(fig, animate, interval = interval, repeat = False)  #interval: ms between two frames 
    plt.draw()
    plt.show()

##    plt.clf()
##    plt.plot(gesunde)
##    plt.plot(infizierte)
##    plt.plot(genesene)
##    plt.show()
