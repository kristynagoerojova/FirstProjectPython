class IteratorMocnin:
    def __init__(self, umocnena_cisla):
        self.umocnena_cisla = umocnena_cisla
        self.cislo = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cislo >= self.umocnena_cisla:
            raise StopIteration
        self.cislo += 1
        return self.cislo ** 2


mocniny = IteratorMocnin(10)

for mocnina in mocniny:
    print(mocnina)

