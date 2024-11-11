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
        return prvni_cislo / druhe_cislo
    else:
        return "Nespravny operator"

vysledek = spocitej_to()

print(f"Vysledek je {vysledek}.")

