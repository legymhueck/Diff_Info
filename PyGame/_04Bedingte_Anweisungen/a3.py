b1 = True
b2 = False
x = 17
y = 9
txt1 = ""
txt2 = "Hallo Welt"

print("1.: True UND False ergibt: " + str(bool(b1 and b2)))  # True AND False -> False
print("2.: True ODER False ergibt: " + str(bool(b1 or b2)))  # True OR False -> True
print("3.: Nicht False ergibt: " + str(bool(not b2)))  # not False -> True
print("4.: Der Buchstabe 'a' ist in 'Hallo Welt' enthalten ergibt: " + str(bool("a" in txt2)))
print("5.: 17 ist größer als 9 ergibt: " + str(bool(x > y)))
print("6.: 17 ist ungleich 9 ergibt: " + str(bool(x != y)))
print("7.: Eine leere Zeichenkette UND 9 < 17 ergibt: " + str(bool(txt1 and y < x)))  # False AND True -> False
print("8.: Eine Zeichenkette ODER False ergibt: " + str(bool(txt2 or b2)))  # True OR False -> True
print("9.: (True ODER False) UND (eine leere Zeichenkette oder eine Zeichenkette) UND True ergeben: "
      + str((bool(b1 or b2)) and (bool(txt1 or txt2)) and True))  # True AND True AND True
