import csv
import pickle

poznamky = []

def pridat_poznamku():
    while True:
        poznamka = input("Vlozte poznamku (nebo Enter pro ukonceni zadavani): ")
        if poznamka == "":
            print("Konec zadavani.")
            break
        poznamky.append(poznamka)


def vypis_poznamky(poznamky):
    if not poznamky:
        print("Seznam poznámek je prázdný.")
    else:
        print("Vase poznamky: ")
        for index, poznamka in enumerate(poznamky, start=1):
            print(f"{index}. {poznamka}")


def smazat_poznamku(poznamky):
    if not poznamky:
        print("Seznam poznámek je prázdný.")
        return

    while True:
        try:
            poradi = int(input("Ktery radek chcete smazat? "))

            if poradi <= len(poznamky):
                del poznamky[poradi - 1]
                print(f"Poznamka byla smazana.")
                break
            else:
                print(f"Zadejte cislo v rozmezi 1 az {len(poznamky)}")
        except ValueError:
            print("Neplatný vstup. Zadejte číslo.")


def upravit_poznamku(poznamky):
    if not poznamky:
        print("Seznam poznámek je prázdný.")
        return

    while True:
        try:
            poradi = int(input("Ktery radek chcete upravit? "))

            if poradi <= len(poznamky):
                index = poradi - 1
                novy_text = input("Zadejte zmeneny text: ")
                poznamky[index] = novy_text
                print(f"Poznamka cislo {poradi} byla nahrazena '{novy_text}'.")
                break
            else:
                print(f"Zadejte cislo v rozmezi 1 az {len(poznamky)}")
        except ValueError:
            print("Neplatný vstup. Zadejte číslo.")


def ulozit_do_csv(poznamky):
    if not poznamky:
        print("Seznam poznámek je prázdný.")
        return

    nazev_souboru = input("Zadej nazev noveho souboru: ")

    with open(nazev_souboru, 'w', newline="", encoding="utf-8") as novy_soubor:
        writer = csv.writer(novy_soubor)

        for poznamka in poznamky:
            writer.writerow([poznamka])


def nacist_z_csv():
    nazev_souboru = input("Zadej nazev souboru, ktery chcete otevrit: ")

    with open(nazev_souboru, encoding="utf-8") as existujici_soubor:
        reader = csv.reader(existujici_soubor)
        for row in reader:
            print(row)




pridat_poznamku()
vypis_poznamky(poznamky)
smazat_poznamku(poznamky)
# upravit_poznamku(poznamky)
#
# ulozit_do_csv(poznamky)
# nacist_z_csv()
