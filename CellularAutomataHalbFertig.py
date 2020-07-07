import numpy
import random

PERSONENZAHL = 100
HAUSZAHL = 20
ZEITRAUM = 25
INFEKTIONSWAHSCHEINLICHKEIT = 0.9
INFEKTIONSZEITRAUM = 5
RAUMLIMIT = 5


class Person:
    def __init__(self, krankheitsStatus, befolgtRegel):
        self.krankheitsStatus = krankheitsStatus
    def __str__(self):
        return self.krankheitsStatus
    def move(self, häuser):
        random.choice(häuser).personenListe.append(self)
        
class Haus:
    def __init__(self, personenListe):
        self.personenListe = personenListe
       
   


personen = []
häuser = []
     
def einTag():
    for haus in häuser:
        haus.personenListe = []
        
    for person in personen:
        person.move(häuser)
    
    for haus in häuser:
        infizierte = 0
        for person in haus.personenListe:
            if(person.krankheitsStatus == "infiziert"):
                infizierte ++;
        for person in haus.personenListe:
            if(random.random() > (1 - INFEKTIONSWAHSCHEINLICHKEIT) ** infizierte):
                person.krankheitsStatus = "infiziert"
        

        
for i in range(HAUSZAHL):
    häuser
       
for i in range(PERSONENZAHL):
    p = Person("gesund", True)
    r = random.random()
    if(r)
    personen.append(p)
    





for i in range(PERSONENZAHL):
    print(str(personen[i]))
