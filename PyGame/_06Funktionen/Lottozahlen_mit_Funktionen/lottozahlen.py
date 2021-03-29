import random


# Definition der Methoden
def benutzereingabe():
    # Benutzereingabe: 6 Lottozahlen
    fertig_getippt = False
    while not fertig_getippt:
        zahl = int(input("Geben Sie 6 Zahlen zwischen 1 und 49 ein: "))
        if zahl not in getippte_zahlen and 0 < zahl < 50:
            getippte_zahlen.append(zahl)
        else:
            print("Ihre Zahl ist nicht im erlaubten Bereich oder doppelt.")
        if len(getippte_zahlen) == 6:
            fertig_getippt = True
    print("Getippt:\t\t", getippte_zahlen)


def zufallszahlen_erzeugen():
    # Zufallszahlen erzeugen
    fertig_zufallszahlen_erzeugen = False
    while not fertig_zufallszahlen_erzeugen:
        zufallszahl = random.randint(1, 49)
        if zufallszahl not in zufallszahlen:
            zufallszahlen.append(zufallszahl)
        if len(zufallszahlen) == 6:
            fertig_zufallszahlen_erzeugen = True
    # print("Zufallszahlen: " + str(zufallszahlen))
    print("Zufallszahlen:\t", zufallszahlen)


def anzahl_richtige_testen():
    # Anzahl richtiger Tipps testen.
    # Richtige Tipps in eine neue Liste schreiben.
    counter = 0
    while counter < 6:
        if getippte_zahlen[counter] in zufallszahlen:
            richtige.append(getippte_zahlen[counter])
        counter += 1
    if len(richtige) > 0:
        # print("Sie haben " + str(len(richtige)) + " Richtige.")
        # print("Sie haben folgende Zahl(en) richtig geraten: " + str(richtige))
        print("Sie haben", len(richtige), "Richtige.")
        print("Sie haben folgende Zahl(en) richtig geraten:", richtige)
    else:
        print("Sie haben leider keine Zahl richtig geraten.")


# Deklaration der globalen Variablen
zufallszahlen = []
getippte_zahlen = []
richtige = []

# Aufruf der Methoden
benutzereingabe()
zufallszahlen_erzeugen()
anzahl_richtige_testen()
