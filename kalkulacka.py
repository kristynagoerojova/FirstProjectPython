def spocitej_to():
    try:
        prvni_cislo = int(input("Zadej cislo: "))
    except ValueError:
        print("Muzes zadat pouze cislo.")

    operator = input("Zadej operator (+, -, *, /): ")
    if operator not in ["+", "-", "*", "/"]:
        raise ValueError("Spatne zadane znamenko")

    try:
        druhe_cislo = int(input("Zadej dalsi cislo: "))
    except ValueError:
        print("Muzes zadat pouze cislo.")

    if operator == "+":
        return prvni_cislo + druhe_cislo
    elif operator == "-":
        return prvni_cislo - druhe_cislo
    elif operator == "*":
        return prvni_cislo * druhe_cislo
    elif operator == "/":
        try:
            return prvni_cislo / druhe_cislo
        except ZeroDivisionError:
            print("Nelze delit nulou.")
    else:
        return "Zadal si nespravny operator"

vysledek = spocitej_to()

print(f"Vysledek: {vysledek}.")

