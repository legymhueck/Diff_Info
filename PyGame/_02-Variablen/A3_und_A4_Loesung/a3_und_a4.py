# Lösung zu Aufgabe 3

# Wir benötigen die Rechnung aus Aufgabe 2. Sie lautet: 21 * 3 + 17 * 4

# Löse die Rechnung aus Aufgabe 2 mit:
# 1 Variablen
# 2 Variablen
# 4 Variablen

# Lösung mit 1 Variablen:
print("\nLösung mit 1 Variablen:")
ergebnis = 21 * 3 + 17 * 4

print(ergebnis)
# Eine aussagekräftigere Ausgabe wäre:
rechnung_als_string = "21 * 3 + 17 * 4"
print(rechnung_als_string + " = " + str(ergebnis))

# Benutzt man nicht den Verbindungsoperator, sondern das Komma, sieht eine mögliche Anweisung so aus:
print(rechnung_als_string, "=", ergebnis)


# Lösung mit 2 Variablen
print("\nLösung mit 2 Variablen:")
produkt1 = 21 * 3
produkt2 = 17 * 4
print(produkt1 + produkt2)
print(rechnung_als_string + " = " + str(ergebnis))
print(rechnung_als_string, "=", ergebnis)

# Lösung mit 4 Variablen
print("\nLösung mit 4 Variablen:")
zahl1 = 21
zahl2 = 3
zahl3 = 17
zahl4 = 4
print(zahl1 * zahl2 + zahl3 * zahl4)
print(rechnung_als_string + " = " + str(zahl1 * zahl2 + zahl3 * zahl4))
print(rechnung_als_string, "=", zahl1 * zahl2 + zahl3 * zahl4)

# Lösung zu Aufgabe 4
# Ja, Python beachtet die Punkt-vor-Strich Regel
