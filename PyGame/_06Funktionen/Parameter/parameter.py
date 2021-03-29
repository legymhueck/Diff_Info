# Definition der Methoden
def drucken(platzhalter):  # Wird die Funktion im Hauptteil aufgerufen, fügt man den wirklichen Wert ein
    print("Das Doppelte ist:", platzhalter + platzhalter)  # Hier wird mit der parameter-Variablen gearbeitet.


def zahl_eingeben():
    return int(input("\nIhre Zahl: "))


# Hauptprogramm
drucken(5)  # Hier setzt man für den Parameter 'platzhalter' den wirklichen Wert ein.

drucken(zahl_eingeben())  # Der wirkliche Wert kann auch aus der Benutzereingabe kommen.


# Man kann auch erst die Funktion aufrufen (rechts vom Zuweisungsoperator) und den Wert dann in die Variable schreiben.
wert_des_benutzers = zahl_eingeben()
drucken(wert_des_benutzers)  # Dann wird die Funktion mit dem Wert der Variablen aufgerufen.
