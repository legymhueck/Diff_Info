import random


# Definition der Funktionen
def benutzereingabe():
    begriff = input(str(liste) + "?")
    return begriff


def computereingabe():
    return liste[random.randint(0, 2)]


def gewinner_einer_runde(benutzer, computer):
    benutzeridx = liste.index(benutzer)
    computeridx = liste.index(computer)

    if benutzeridx == computeridx:
        print("Unentschieden!")
        return 0, 0
    elif (computeridx + 1) % 3 == benutzeridx:
        print("Gewinner: Benutzer")
        return 1, 0
    else:
        print("Gewinner: Computer")
        return 0, 1


def gewinner_einer_runde2(benutzer, computer):
    gewinner = 0
    if benutzer == "Schere" and computer == "Papier" \
            or benutzer == "Stein" and computer == "Schere" \
            or benutzer == "Papier" and computer == "Stein":
        print("Gewinner: Benutzer")
        gewinner = 1
    elif benutzer == "Schere" and computer == "Stein" \
            or benutzer == "Stein" and computer == "Papier" \
            or benutzer == "Papier" and computer == "Schere":
        print("Gewinner: Computer")
        gewinner = -1
    else:
        print("Unentschieden!")
    return gewinner


def runde():
    benutzer = benutzereingabe()
    computer = computereingabe()
    return gewinner_einer_runde(benutzer, computer)


def auswertung(punkte1, punkte2):
    print("\nEndauswertung:")
    print("\tBenutzerpunkte:", punkte1)
    print("\tComputerpunkte:", punkte2)


# Hauptteil
liste = ["Schere", "Stein", "Papier"]
benutzerpunkte = 0
computerpunkte = 0
for x in range(3):
    p1, p2 = runde()
    benutzerpunkte += p1
    computerpunkte += p2
auswertung(benutzerpunkte, computerpunkte)
