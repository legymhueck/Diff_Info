def benutzer_auswahl():
    print("Willkommen beim Temperatur-Umrechner!")
    print("Was möchten Sie umrechnen?")

    moegliche_eingaben = ["(1) Celsius nach Kelvin", "(2) Celsius nach Fahrenheit", "(3) Kelvin nach Celsius",
                          "(4) Kelvin nach Fahrenheit", "(5) Fahrenheit nach Celsius", "(6) Fahrenheit nach Kelvin"]
    print("\t", moegliche_eingaben[0])
    print("\t", moegliche_eingaben[1])
    print("\t", moegliche_eingaben[2])
    print("\t", moegliche_eingaben[3])
    print("\t", moegliche_eingaben[4])
    print("\t", moegliche_eingaben[5])

    gueltige_eingabe = int(input("\nGeben Sie Ihre Auswahl ein: "))
    b_eingabe = True
    while b_eingabe:
        if gueltige_eingabe > len(moegliche_eingaben):
            gueltige_eingabe = int(input("\nFalsche Auswahl!\nGeben Sie Ihre Auswahl ein: "))
        else:
            print("\tSie haben also", moegliche_eingaben[gueltige_eingabe - 1], "gewählt.")
            b_eingabe = False
    return gueltige_eingabe


def temperatur_eingabe():
    temperatur = int(input("Geben Sie eine Temperatur ein: "))
    return float(temperatur)


def celsius_nach_kelvin(param_celsius):
    return runden(param_celsius + 273.15)


def celsius_nach_fahrenheit(param_celsius):
    return runden(param_celsius * 1.8 + 32)


def kelvin_nach_celsius(param_kelvin):
    return runden(param_kelvin - 273.15)


def kelvin_nach_fahrenheit(param_kelvin):
    return runden((param_kelvin - 273.15) * 1.8 + 32)


def fahrenheit_nach_celsius(param_fahrenheit):
    return runden(5 / 9 * (param_fahrenheit - 32))


def fahrenheit_nach_kelvin(param_fahrenheit):
    return runden((param_fahrenheit - 32) / 1.8 + 273.15)


def runden(param_einheit):
    return (int(param_einheit * 100)) / 100


def berechnung(umrechnung, temperatur):
    if umrechnung == 1:
        print(temperatur, "Grad Celsius entsprechen", celsius_nach_kelvin(temperatur),
              "Grad Kelvin.")
    elif umrechnung == 2:
        print(temperatur, "Grad Celsius entsprechen", celsius_nach_fahrenheit(temperatur),
              "Grad Fahrenheit.")
    elif umrechnung == 3:
        print(temperatur, "Grad Kelvin entsprechen", kelvin_nach_celsius(temperatur),
              "Grad Celsius.")
    elif umrechnung == 4:
        print(temperatur, "Grad Kelvin entsprechen", kelvin_nach_fahrenheit(temperatur),
              "Grad Fahrenheit.")
    elif umrechnung == 5:
        print(temperatur, "Grad Fahrenheit entsprechen", fahrenheit_nach_celsius(temperatur),
              "Grad Celsius.")
    else:
        print(temperatur, "Grad Fahrenheit entsprechen", fahrenheit_nach_kelvin(temperatur),
              "Grad Kelvin.")


# ------ Beginn Hauptteil ------
gewaehlte_umrechnung = benutzer_auswahl()
gewaehlte_temperatur = temperatur_eingabe()
berechnung(gewaehlte_umrechnung, gewaehlte_temperatur)

