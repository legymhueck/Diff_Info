def auswahlmenue():
    fehlertext = "Falsche Eingabe! Wählen Sie bitte eine Zahl aus dem Menü!"
    optionen = ["1", "2", "3", "4"]  # Auswahlmöglichkeiten
    auswahl = ""  # Die Auswahl wird zu Beginn auf eine falsche Eingabe gesetzt, um eine Benutzer-Auswahl zu erzwingen.

    print("\nWillkommen! Welches Programm möchten Sie starten?\n")
    while auswahl not in optionen:
        print("1 - Textverarbeitung")
        print("2 - Tabellenkalkulation")
        print("3 - Präsentation")
        print("4 - Mail")
        auswahl = input("\nWählen Sie zum Starten eines Programms die Zahl vor den Einträgen: ")

        if auswahl not in optionen:
            print("\n" + fehlertext + "\n")

    return auswahl


def programmstarter():
    programme = ["LibreOffice Writer", "LibreOffice Calc", "LibreOffice Präsentationen", "Thunderbird"]
    starttext = " wird gestartet ..."

    auswahl = auswahlmenue()  # Wir merken uns, welchen String die Methode auswahlmenue() zurückgegeben hat.
    if auswahl == "1":  # Da die Methode auswahlmenue() einen String zurückgibt, prüft man auf einen String.
        print("\n\t" + programme[0] + starttext)
    elif auswahl == "2":
        print("\n\t" + programme[1] + starttext)
    elif auswahl == "3":
        print("\n\t" + programme[2] + starttext)
    elif auswahl == "4":
        print("\n\t" + programme[3] + starttext)
    else:
        print("\n\t Programm-Fehler! Hier darf man gar nicht hinkommen!")


# Hauptteil
programmstarter()
