def spocitej_to():
    prvni_cislo = int(input("Zadej cislo: "))

    operator = input("Zadej operator (+, -, *, /): ")

    druhe_cislo = int(input("Zadej dalsi cislo: "))

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

