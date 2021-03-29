# Lösung zu Aufgabe 2

# Benutze Variablen und Zuweisungen, um die folgende Rechnung mit Python zu machen:

# 21 * 3 + 17 * 4

zahl1 = 21
zahl2 = 3
zahl3 = 17
zahl4 = 4
ergebnis = zahl1 * zahl2 + zahl3 * zahl4

# Die Anweisung: print("21 * 3 + 17 * 4 = " + ergebnis) würde einen Fehler verursachen, da der Compiler versucht,
# mit dem Verbindungsoperator + einen String ("21 * 3 + 17 * 4 = ") mit einem Integer zu verbinden.
# Da der Verbindungsoperator nur zwei Stings miteinander verbinden kann, muss der Integer erst mit der
# Konvertierungsfunktion str() in einen Sting konvertiert werden.
print("21 * 3 + 17 * 4 = " + str(ergebnis))

# Zusatzinfo:
# Möchte man zwei Dinge hintereinander ausgeben, kann man sie durch ein Komma voneinander trennen.
print("21 * 3 + 17 * 4 =", ergebnis)


# Weitere Möglichkeit:
produkt1 = 21 * 3
produkt2 = 17 * 4
summe_der_produkte = produkt1 + produkt2
ausgabetext = "21 * 3 + 17 * 4 ="
print(ausgabetext + " " + str(summe_der_produkte))
# oder
print(ausgabetext, summe_der_produkte)
