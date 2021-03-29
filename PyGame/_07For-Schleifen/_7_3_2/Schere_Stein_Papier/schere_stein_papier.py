import random


# Definition der Funktionen
def benutzereingabe():
    begriff = input("Schere, Stein oder Papier? ")
    return begriff


def computereingabe():
    liste = ["Schere", "Stein", "Papier"]
    return liste[random.randint(0, 2)]


def gewinner_einer_runde(benutzer, computer):
    if benutzer == "Schere" and computer == "Papier" \
            or benutzer == "Stein" and computer == "Schere" \
            or benutzer == "Papier" and computer == "Stein":
        return benutzer
    elif benutzer == "Schere" and computer == "Stein" \
            or benutzer == "Stein" and computer == "Papier" \
            or benutzer == "Papier" and computer == "Schere":
        return computer


def drei_runden():
    benutzerpunkte = 0
    computerpunkte = 0
    for x in range(3):
        benutzer = benutzereingabe()
        computer = computereingabe()
        if gewinner_einer_runde(benutzer, computer) == benutzer:
            benutzerpunkte += 1
            print("Gewinner: Benutzer")
        elif gewinner_einer_runde(benutzer, computer) == computer:
            computerpunkte += 1
            print("Gewinner: Computer")
        else:
            print("Unentschieden!")

    print("\nEndauswertung:")
    print("\tBenutzerpunkte:", benutzerpunkte)
    print("\tComputerpunkte:", computerpunkte)


# Hauptteil
drei_runden()
