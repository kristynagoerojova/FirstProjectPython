#Task 13 - zároveň sčítáme a násobíme

#cílem bude paralerně počítat:
# součet čísel 1,2,3,4,...1000000
# násobení čísel 1, 2, 3,4, .... 100


#Vložit třídu ThreadWithReturnValue

# definovat funkce pro sčítání a násobení

# inicializovat třídu ThreadWithReturnValue pro každou úlohu

# pustit  .start()

# počkat na výsledek .join()

import threading


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target):
        self.target = target
        super().__init__()

    def run(self):
        self.result = self.target()

    def join(self, timeout=None):
        super().join(timeout)
        return self.result

def scitani():
    soucet = 0
    for cislo in range(1000000):  # Loop from 0 to 999999
        soucet += cislo
    return soucet

def nasobeni():
    nasobek = 1
    for cislo in range(1, 100):
        nasobek *= cislo
    return nasobek

if __name__ == "__main__":
    vysledek_scitani = ThreadWithReturnValue(target=scitani)
    vysledek_nasobeni = ThreadWithReturnValue(target=nasobeni)

    vysledek_scitani.start()
    vysledek_nasobeni.start()

    print("Vysledek scitani: ", vysledek_scitani.join())
    print("Vysledek nasobeni: ", vysledek_nasobeni.join())

