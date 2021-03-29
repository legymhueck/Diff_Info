# Lösung zu Aufgabe 7

# Du hast 1357 Sekunden für den 5 km Lauf im Sportunterricht benötigt.
# Du möchtest die Zeit aber in Minuten und Sekunden wissen.
# Berechne die Minuten und Sekunden mit arithmetischen Operatoren!

# Lösung:
print("\nLösung mit Modulo:")
zeit_in_sekunden = 1357
zeit_in_minuten = zeit_in_sekunden / 60  # Ergebnis: 22.61666666
restliche_sekunden = zeit_in_sekunden % 60  # Ergebnis: 37
print(zeit_in_minuten)  # Wir wollen aber eine Ganzzahl, d.h. keine Kommastellen.
print(int(zeit_in_minuten))  # Wir schneiden die Zahlen hinter dem Komma ab, indem wir Float in Int konvertieren.
print(restliche_sekunden)

# Hier eine schöne Ausgabe ...
print(str(zeit_in_sekunden) + " Sekunden sind " + str(int(zeit_in_minuten)) + " Minuten und "
      + str(restliche_sekunden) + " Sekunden.")


# Kompliziertere Rechnung:
print("\nKomplizierte Lösung:")
ausgabe_der_minuten = int(1357 / 60)
sekunden_als_dezimalzahl = 1357 / 60 - ausgabe_der_minuten
wirkliche_sekunden = sekunden_als_dezimalzahl * 60
# print(ausgabe_der_minuten)
# print(sekunden_als_dezimalzahl)
# print(wirkliche_sekunden)
print(str(zeit_in_sekunden) + " Sekunden sind " + str(ausgabe_der_minuten) + " Minuten und "
      + str(int(wirkliche_sekunden)) + " Sekunden.")


# Wie kommt man auf die 37 Sekunden Rest?
# 22 Minuten sind 1320 Sekunden. (22 * 60 = 1320)
# Die restlichen Sekunden ergeben sich also aus: 1357 - 1320. Das sind 37 Sekunden.

# Da mit dem Modulo-Operator NUR der Rest einer Division ausgegeben wird, ergibt 1357 % 60 die Zahl 37.

# Ein weiteres Beispiel:
# Ein Kuchen hat 21 Stücke.
# Wenn du nun ganze Stücke auf 4 Kinder verteilen möchtest, wie viele Stücke bleiben dann als Rest übrig?
# Bei einer Division OHNE Rest, bekommt jedes Kind 4 Stücke: 21 / 4 = 5.

# Wie ermitteln, wie viele Stücke verteilt wurden, also: 5 * 4 = 20
# Wie viele Stücke bleiben übrig? 21 Stücke insgesamt minus 20 verteilte Stücke ergibt 1 Stück.
# Es bleibt also 1 Stück übrig.
# Bei einer Modulo-Operation interessiert uns NUR der Rest! Also ergibt 21 % 5 den Rest 1:
print("\n\nDer Rest aus der Division von 21 und 4 ergibt:", 21 % 4)

