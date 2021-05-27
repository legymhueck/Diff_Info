import random


def benutzereingabe():
    laenge = (int(input("Passwortlänge: ")))
    while laenge < 8 or laenge > 20:
        laenge = (int(input("Bitte geben Sie eine gültige Passwortlänge zwischen 8 und 20 an: ")))
    return laenge


def zufallsindex():
    laenge = len(passwortzeichen())  # Zufallszahl muss innerhalb der Länge der Liste möglicher Zeichen liegen
    index = random.randint(0, laenge - 1)  # Ende Zufallszahl ist inklusiv, Index muss aber 1 kleiner sein
    return index


def passwortzeichen():
    liste = ["#", "!", "?", "%", "$"]  # Eine Liste mit den Sonderzeichen erzeugen. Die Zahlen kommen hinzu.
    for i in range(0, 10):
        liste.append(str(i))  # Die Zahlen 0-9 werden zur Liste hinzugefügt.
    return liste


def passwort():
    benutzer_passwort = ""  # Zu Beginn ist das Passwort noch leer.
    passwort_laenge = benutzereingabe()  # Die Passwortlänge wird benötigt für die Abbruchbedingung der for-Schleife.
    for i in range(0, passwort_laenge):
        # Das Passwort wird Zeichen für Zeichen vergrößert, indem ein zufälliger Index aus der Liste gewählt wird.
        # zufallsindex() wird aufgerufen, weil immer wieder ein neuer zufälliger Index erzeugt werden muss.
        benutzer_passwort += passwortzeichen()[zufallsindex()]  # Der String wird erweitert und ein zufälliges Zeichen.
    return benutzer_passwort


print(passwort())
