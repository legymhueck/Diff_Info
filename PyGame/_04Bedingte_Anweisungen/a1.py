waren = ["Äpfel", "Birnen", "Erdbeeren", "Kartoffeln", "Eier", "Milch"]
mengen = [4, 1, 6, 10, 2, 0]
print("Unsere Waren: " + str(waren))
ware = input("Was möchten Sie kaufen? ")
if ware in waren:
    index = waren.index(ware)
    anzahl = input("Wie viele " + waren[index] + " möchten Sie haben? ")

    if int(anzahl) > mengen[index]:
        print("Leider haben wir nur noch " + str(mengen[index]) + " " + waren[index] + ".")
        rest = (int(anzahl) - mengen[index])
        antwort = input("Sollen wir die restlichen " + str(rest) + " " + waren[index]
                        + " für morgen reservieren? (Ja/Nein) ")
        if antwort == "Ja":
            print("Sehr schön. Dann bis morgen.")
        else:
            print("Gut, dann bleibt es bei " + str(mengen[index]) + " " + waren[index] + ".")
    else:
        print("Wir haben " + anzahl + " " + waren[index] + " auf Lager. Bitteschön!")

else:
    print(ware + " haben wir leider nicht")

# Herangehensweise an die Aufgabe

# 1. Wie speichere ich die Benutzereingabe für die Warenauswahl?
# 1.1 Welchen Datentyp hat die Benutzereingabe?
# 1.2 Wie erhalte ich den Index (die Stelle), an der der Artikel der Benutzereingabe steht,
#     z. B. wenn ich Eier eingebe, ist der Index 4.
# 1.3 Welchen Datentyp hat der ermittelte Index? Wie ermittle ich einen Datentypen?

# 2. Wenn der benutzer die Anzahl eingibt, wie konvertiere ich diese in einen Integer?
# 3. Wie kontrolliere ich, dass die Benutzereingabe, z. B. "Eier", in der Liste vorhanden ist?
# 4. Wie konvertiere ich Integer in Strings? print-Anweisungen dürfen nur einen Datentyp haben, d. h.
#    beginne ich eine Print-Anweisung mit einem String, müssen die Variablen, die ich mit dem Plus-Operator
#    zusammensetze, auch vom Typ String sein.
