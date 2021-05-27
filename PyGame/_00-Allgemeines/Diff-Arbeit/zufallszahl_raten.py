import random


def zufallszahl():
    zahl = random.randint(0, 101)  # Eine Zufallszahl zwischen 0 und 100 erzeugen...
    return zahl  # ...und diese zurückgeben


def benutzereingabe():
    rate_zahl = (int(input("Raten Sie eine Zahl zwischen 0 und 100: ")))  # Die Ratezahl vom Benutzer abfragen.
    return rate_zahl


def ratespiel():
    geratene_zahlen = []  # Eine leere Liste erzeugen, die nachher mit den geratenen Zahlen gefüllt wird.
    zufalls_zahl = zufallszahl()  # Den Computer eine Zufallszahl ziehen lassen.
    raten = True  # Boolean-Variable erzeugen. Sie ist so lange True, bis der Benutzer die richtige Zahl rät.
    while raten:  # Solange die Variable True ist...
        benutzer_zahl = benutzereingabe()  # gibt der Benutzer eine Zahl ein, die in benutzer_zahl gespeichert wird.
        geratene_zahlen.append(benutzer_zahl)  # Die geratene Zahl wird in allen Fällen in die Liste eingefügt.
        if benutzer_zahl == zufalls_zahl:  # 1. Fall: Benutzer hat richtig geraten
            print("Sie haben", len(geratene_zahlen), "Versuche gebraucht.")
            print("Sie haben folgende Zahlen geraten:", geratene_zahlen)
            raten = False  # Fall soll die while-Schleife abgebrochen werden.
        elif benutzer_zahl > zufalls_zahl:  # 2. Fall: Die Zahl des Benutzers ist zu groß.
            print("Ihre Zahl ist zu groß.")
        elif benutzer_zahl < zufalls_zahl:  # 3. Fall: Die Zahl des Benutzers ist zu klein.
            print("Ihre Zahl ist zu klein.")


ratespiel()
