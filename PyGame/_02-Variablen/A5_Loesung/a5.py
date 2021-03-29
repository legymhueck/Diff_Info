# Lösung zu Aufgabe 5

# Benutze nochmal Variablen und Zuweisungen für folgende Berechnung.
# 8736 / 3 + 9286
zahl1 = 8736
zahl2 = 3
zahl3 = "9286"

ergebnis = zahl1 / zahl2 + int(zahl3)
rechnung_als_string = "8736 / 3 + 9286"
print(rechnung_als_string + " = " + (str(ergebnis)))

# Erläutere, welchen Datentyp deine Variablen haben!

# Die Variable zahl1 hat den Datentyp "Integer".
# Die Variable zahl2 hat ebenfalls den Datentyp "Integer"
# Die Variable zahl3 hat den Datentyp "String"
# Das Ergebnis hat den Datentyp "Float", da hier eine Division erfolgt.

# Nachweis:
print("\nNachweis der Datentypen:")
print("Die Variable 'zahl1' (" + str(zahl1) + ") ist vom Datentyp: " + str(type(zahl1)))
print("Die Variable 'zahl2' (" + str(zahl2) + ") ist vom Datentyp: " + str(type(zahl2)))
print("Die Variable 'zahl3' (" + str(zahl3) + ") ist vom Datentyp: " + str(type(zahl3)))
print("Die Variable 'ergebnis' (" + str(ergebnis) + ") ist vom Datentyp: " + str(type(ergebnis)))
