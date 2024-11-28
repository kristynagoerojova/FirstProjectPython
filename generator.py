#Task12 - Vytvoříte generátor, který bude postupně vracet
# Albert - máme koncovku "bert".
# před tu koncovku budou dávány předpony "Al", "Ro", "Hu", "Nor", "Gil"

def GeneratorJmen(pred, konc):
    for predpona in pred:
        yield predpona + konc

predpony = ["Jus", "Kris", "Valen"]
koncovka = "týna"

for jmeno in GeneratorJmen(predpony, koncovka):
    print(f"Tvé jméno je {jmeno}")