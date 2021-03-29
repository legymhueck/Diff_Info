# ------ Anfang Definition der Funktionen ------

def eingabe_kaufpreis():
    eingegebener_kaufpreis = (int(input("Geben Sie den Kaufpreis ein: ")))
    return eingegebener_kaufpreis


def eingabe_mehrwertsteuersatz():
    eingegebener_steuersatz = (int(input("Geben Sie den Mehrwertsteuersatz ein: (7/19)")))
    return eingegebener_steuersatz


def berechnung_steuer(param_bruttobetrag, param_steuersatz):
    enthaltene_steuer = float((param_bruttobetrag / (100 + param_steuersatz) * param_steuersatz))
    return enthaltene_steuer


def runden(zahl):
    return (int(zahl * 100)) / 100


# ------ Ende Definition der Funktionen ------


# ------ Angang Hauptteil ------
mehrwertsteuersatz = berechnung_steuer(eingabe_kaufpreis(), eingabe_mehrwertsteuersatz())
print("Im Bruttobetrag enthaltener Mehrwertsteuersatz:", runden(mehrwertsteuersatz), "%")

# ------ Ende Hauptteil ------
