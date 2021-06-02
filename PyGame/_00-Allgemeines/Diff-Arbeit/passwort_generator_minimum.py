# Anforderungen:
# - 2 Funktionen
# - Benutzereingabe der Passwortlänge, Wiederholung bei Falscheingabe
# - Liste mit möglichen Passwortzeichen
# - Ausgabe auf Konsole

import random


def benutzereingabe():
    anzeigetext = "Passwortlänge (min. 8, max. 20): "
    laenge = int(input(anzeigetext))
    while laenge < 8 or laenge > 20:
        laenge = int(input(anzeigetext))
    return laenge


def passwort_generieren():
    liste = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "#", "!", "?", "%", "$"]
    benutzer_passwort = ""

    for i in range(benutzereingabe()):
        zufalls_index = random.randint(0, len(liste) - 1)
        benutzer_passwort += liste[zufalls_index]
    return benutzer_passwort


print(passwort_generieren())
