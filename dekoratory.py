# def vyprintuj_a_pust(func):
#     def nova_funkce(a,b):
#         print(f"pouštíme funkci {func.__name__} s parametry {a}, {b}")
#         return func(a,b)
#     return nova_funkce
#
# @vyprintuj_a_pust
# def soucet(a,b):
#     return a+b
#
# @vyprintuj_a_pust
# def rozdil(a,b):
#     return a-b
#
# print(soucet(3,5))
# print(rozdil(3,5))


def with_password(func):
    def zadej_heslo(age, name):
        heslo = input("Zadejte heslo: ")
        print("Heslo zadano")
        return func(age, name)
    return zadej_heslo


@with_password
def sample_funkce(age: int, name: str):
    print(f"Age {age}, name {name}.")

sample_funkce(20, "Kristyna")