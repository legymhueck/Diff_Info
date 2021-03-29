import random


# Definition der Methoden
def benutzereingabe():
    # Benutzereingabe: 6 Lottozahlen
    tipp = []
    while len(tipp) < 6:
        zahl = int(input("Geben Sie 6 Zahlen zwischen 1 und 49 ein: "))
        if zahl not in tipp and 0 < zahl < 50:
            tipp.append(zahl)
        else:
            print("Ihre Zahl ist nicht im erlaubten Bereich oder doppelt.")
    print("Getippt:\t\t", tipp)
    return tipp


def zufallszahlen_erzeugen():
    # Zufallszahlen erzeugen
    zufallszahlen = []
    while len(zufallszahlen) < 6:
        zufallszahl = random.randint(1, 49)
        if zufallszahl not in zufallszahlen:
            zufallszahlen.append(zufallszahl)

    # print("Zufallszahlen: " + str(tipp))
    print("Zufallszahlen:\t", zufallszahlen)
    return zufallszahlen


def anzahl_richtige_testen(tipp, zufallszahlen):
    # Anzahl richtiger Tipps testen.
    # Richtige Tipps in eine neue Liste schreiben.
    richtige = []
    counter = 0
    while counter < 6:
        if tipp[counter] in zufallszahlen:
            richtige.append(tipp[counter])
        counter += 1
    if len(richtige) > 0:
        # print("Sie haben " + str(len(richtige)) + " Richtige.")
        # print("Sie haben folgende Zahl(en) richtig geraten: " + str(richtige))
        print("Sie haben", len(richtige), "Richtige.")
        print("Sie haben folgende Zahl(en) richtig geraten:", richtige)
    else:
        print("Sie haben leider keine Zahl richtig geraten.")


# Hauptteil
getippte_zahlen = benutzereingabe()
lottozahlen = zufallszahlen_erzeugen()

anzahl_richtige_testen(getippte_zahlen, lottozahlen)
