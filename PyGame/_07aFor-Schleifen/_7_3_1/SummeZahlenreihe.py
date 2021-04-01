# Definition der Funktionen
def eingabe(eingabetext):
    zahl = (int(input(eingabetext)))
    return zahl


def summe_berechnen(startwert, endwert):
    summe = 0
    for x in range(startwert, endwert + 1):
        summe = summe + x
    return summe


# Hauptprogramm
start = eingabe("Startwert:\t")
end = eingabe("Endwert:\t")
print("Summe:", summe_berechnen(start, end))
