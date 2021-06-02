import random


def benutzereingabe():
    anzeigetext = "Ihre Ratezahl zwischen 0 und 100: "
    rate_zahl = int(input(anzeigetext))
    while rate_zahl < 0 or rate_zahl > 100:
        rate_zahl = int(input(anzeigetext))
    return rate_zahl


def ratespiel():
    geratene_zahlen = []
    zufalls_zahl = random.randint(0, 101)
    raten = True
    while raten:
        benutzer_zahl = benutzereingabe()
        geratene_zahlen.append(benutzer_zahl)
        if benutzer_zahl == zufalls_zahl:
            print("Sie haben", len(geratene_zahlen), "Versuche gebraucht.")
            print("Sie haben folgende Zahlen geraten:", geratene_zahlen)
            raten = False
        elif benutzer_zahl > zufalls_zahl:
            print("Ihre Zahl ist zu groß.")
        elif benutzer_zahl < zufalls_zahl:
            print("Ihre Zahl ist zu klein.")


ratespiel()
