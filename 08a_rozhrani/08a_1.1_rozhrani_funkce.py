
from tkui import input, nacti_cislo, ano_nebo_ne, print
# ROZHRANÍ FUNKCE:

if ano_nebo_ne("Chceš si zahrát hru?"):
    print("Ok! Nejdřív si ji ale musíš naprogramovat.")
else:
    print("Škoda.")

vstup = input("Co se teď asi stane? ")
print(vstup)

print(nacti_cislo("Zadej číslo: "))

# Rozhraní funkce tvoří všechno, co potřebuje kód, který funkce volá
