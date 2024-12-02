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
    def __init__(self, target, args=(), kwargs=None):
        if kwargs is None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result

def scitani(cisla):
    soucet = 0
    for cislo in range(cisla):  # Loop from 0 to 999999
        soucet += cislo
    return soucet

def nasobeni(cisla):
    nasobek = 1
    for cislo in range(1, cisla):
        nasobek *= cislo
    return nasobek

if __name__ == "__main__":
    vysledek_scitani = ThreadWithReturnValue(target=scitani, args=(1000000,))
    vysledek_nasobeni = ThreadWithReturnValue(target=nasobeni, args=(100,))

    vysledek_scitani.start()
    vysledek_nasobeni.start()

    print("Vysledek scitani: ", vysledek_scitani.join())
    print("Vysledek nasobeni: ", vysledek_nasobeni.join())

