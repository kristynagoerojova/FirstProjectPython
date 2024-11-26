import csv
import pickle
import json

poznamky = []

def pridat_poznamku(poznamky):
    while True:
        poznamka = input("Vlozte poznamku (nebo Enter pro ukonceni zadavani): ")
        if poznamka == "":
            print("Konec zadavani.")
            break
        poznamky.append(poznamka)
        print(f"Poznamka byla zadana.")


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
    else:
        vypis_poznamky(poznamky)
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
    else:
        vypis_poznamky(poznamky)
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
    print(f"Soubor byl ulozen jako '{nazev_souboru}'.")


def nacist_z_csv():
    nazev_souboru = input("Zadej nazev souboru, ktery chcete otevrit: ")
    try:
        with open(nazev_souboru, encoding="utf-8") as existujici_soubor:
            reader = csv.reader(existujici_soubor)
            for row in reader:
                print(row)

    except FileNotFoundError:
        print(f"Soubor '{nazev_souboru}' nebyl nalezen.")


def ulozit_do_pkl(poznamky):
    if not poznamky:
        print("Seznam poznámek je prázdný.")
        return

    nazev_souboru = input("Zadej nazev noveho souboru: ")

    with open(nazev_souboru, 'wb') as novy_soubor:
        pickle.dump(poznamky, novy_soubor)
    print(f"Soubor byl ulozen jako '{nazev_souboru}'.")


def nacist_z_pickle():
    nazev_souboru = input("Zadejte název souboru, ktery chcete otevrit: ")
    try:
        with open(nazev_souboru, 'rb') as existujici_soubor:
            data = pickle.load(existujici_soubor)
        print(data)
    except FileNotFoundError:
        print(f"Soubor '{nazev_souboru}' nebyl nalezen.")


def ulozit_do_json(poznamky):
    if not poznamky:
        print("Seznam poznámek je prázdný.")
        return

    nazev_souboru = input("Zadej nazev noveho souboru: ")

    with open(nazev_souboru, 'w') as novy_soubor:
        json.dump(poznamky, novy_soubor)
    print(f"Soubor byl ulozen jako '{nazev_souboru}'.")

def nacist_z_json():
    nazev_souboru = input("Zadejte název souboru, ktery chcete otevrit: ")
    try:
        with open(nazev_souboru, 'r') as existujici_soubor:
            data = json.load(existujici_soubor)
        print(data)
    except FileNotFoundError:
        print(f"Soubor '{nazev_souboru}' nebyl nalezen.")


#program

def poznamkovy_blok():
    print("Vitej v tvem poznámkovém bloku! \n")

    while True:
        print("Vyber z nasledujicich akci: \n")
        print("1. Pridat poznamku \n"
              "2. Vypsat poznamku \n"
              "3. Smazat poznamku \n"
              "4. Upravit poznamku \n"
              "5. Ulozit poznamky do souboru .csv \n"
              "6. Nacist poznamky ze souboru .csv \n"
              "7. Ulozit poznamky do souboru pickle \n"
              "8. Nacist poznamky ze soubrou pickle \n"
              "9. Ulozit poznamky do souboru .json \n"
              "10. Nacist poznamky ze souboru .json \n")

        try:
            user_input = int(input("Vyber cislo akce, kterou chces provest: \n"))

            if user_input == 1:
                pridat_poznamku(poznamky)

            elif user_input == 2:
                vypis_poznamky(poznamky)

            elif user_input == 3:
                smazat_poznamku(poznamky)

            elif user_input == 4:
                upravit_poznamku(poznamky)

            elif user_input == 5:
                ulozit_do_csv(poznamky)

            elif user_input == 6:
                nacist_z_csv()

            elif user_input == 7:
                ulozit_do_pkl(poznamky)

            elif user_input == 8:
                nacist_z_pickle(poznamky)

            elif user_input == 9:
                ulozit_do_json(poznamky)

            elif user_input == 10:
                nacist_z_json(poznamky)

            elif user_input > 10:
                print("Tato akce neexistuje, vyber znovu ze seznamu.")
        except ValueError:
            print("Zadej pouze cela cisla.")

poznamkovy_blok()


# as a class
#
class Poznamkovy_blok:

    def __init__(self):
        self.poznamky = []

    def pridat_poznamku(self):
        while True:
            poznamka = input("Vlozte poznamku (nebo Enter pro ukonceni zadavani): ")
            if poznamka == "":
                print("Konec zadavani.")
                break
            self.poznamky.append(poznamka)


    def vypis_poznamky(self):
        if not self.poznamky:
            print("Seznam poznámek je prázdný.")
        else:
            print("Vase poznamky: ")
            for index, poznamka in enumerate(self.poznamky, start=1):
                print(f"{index}. {poznamka}")

    def smazat_poznamku(self):
        if not self.poznamky:
            print("Seznam poznámek je prázdný.")
            return

        while True:
            try:
                poradi = int(input("Ktery radek chcete smazat? "))

                if poradi <= len(self.poznamky):
                    del self.poznamky[poradi - 1]
                    print(f"Poznamka byla smazana.")
                    break
                else:
                    print(f"Zadejte cislo v rozmezi 1 az {len(self.poznamky)}")
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")

    def upravit_poznamku(self):
        if not self.poznamky:
            print("Seznam poznámek je prázdný.")
            return

        while True:
            try:
                poradi = int(input("Ktery radek chcete upravit? "))

                if poradi <= len(poznamky):
                    index = poradi - 1
                    novy_text = input("Zadejte zmeneny text: ")
                    self.poznamky[index] = novy_text
                    print(f"Poznamka cislo {poradi} byla nahrazena '{novy_text}'.")
                    break
                else:
                    print(f"Zadejte cislo v rozmezi 1 az {len(self.poznamky)}")
            except ValueError:
                print("Neplatný vstup. Zadejte číslo.")

    def ulozit_do_csv(self):
        if not self.poznamky:
            print("Seznam poznámek je prázdný.")
            return

        nazev_souboru = input("Zadej nazev noveho souboru: ")

        with open(nazev_souboru, 'w', newline="", encoding="utf-8") as novy_soubor:
            writer = csv.writer(novy_soubor)

            for poznamka in self.poznamky:
                writer.writerow([poznamka])

    def nacist_z_csv(self):
        nazev_souboru = input("Zadej nazev souboru, ktery chcete otevrit: ")

        with open(nazev_souboru, encoding="utf-8") as existujici_soubor:
            reader = csv.reader(existujici_soubor)
            for row in reader:
                print(row)

    def ulozit_do_pkl(self):
        if not self.poznamky:
            print("Seznam poznámek je prázdný.")
            return

        nazev_souboru = input("Zadej nazev noveho souboru: ")

        with open(nazev_souboru, 'wb') as novy_soubor:
            pickle.dump(self.poznamky, novy_soubor)

    def ulozit_do_json(self):
        if not self.poznamky:
            print("Seznam poznámek je prázdný.")
            return

        nazev_souboru = input("Zadej nazev noveho souboru: ")

        with open(nazev_souboru, 'w') as novy_soubor:
            json.dump(self.poznamky, novy_soubor)
#
#
#
# poznamka = Poznamkovy_blok()
#
# poznamka.pridat_poznamku()
# poznamka.vypis_poznamky()
# poznamka.ulozit_do_csv()
# # poznamka.nacist_z_csv()


