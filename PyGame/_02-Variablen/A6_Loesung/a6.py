# Lösung zu Aufgabe 6:

# Nehmen wir an, folgende Zuweisungen sind gegeben:
x = 10
y = 5
z = 15

# Versuche nun, folgende Anweisung im Detail zu erklären!
# print(str(z) + " = " + str(x) + " + " + str(y))

# Bei dieser Anweisung werden mit der Funktion str() die Variablen x, y und z als Strings ausgegeben.
# Ursprünglich waren x, y, und z bei der Zuweisung Integer.

# Da bei der print-Anweisung Strings miteinander verbunden werden, ist das Plus-Zeichen ein Verbindungsoperator und kein
# arithmetischer Operator.
# Da die arithmetischen Operatoren zwischen Anführungszeichen stehen, also " = " und " + ", sind diese Strings.

# Nachweis:
print("\nNachweis, dass die Variablen bei der Zuweisung Integer sind:")
print(type(x))
print(type(y))
print(type(z))

print("\nNachweis, dass die Variablen in der Anweisung Strings sind:")
print(type(str(x)))
print(type(str(y)))
print(type(str(z)))

print("\nNachweis, dass die arithmetischen Operatoren in der Anweisung ebenfalls Strings sind:")
print(type(" = "))
print(type(" + "))



