from random import randint

"""
Začínáš s 0 body.
Počítač v každém kole vypíše, kolik máš bodů, a zeptá se tě, jestli chceš pokračovat.
Pokud odpovíš „ne“, hra končí.
Pokud odpovíš „ano“, počítač „otočí kartu“ (náhodně vybere číslo od 2 do 10), vypíše její hodnotu a přičte ji k bodům.
Pokud máš víc než 21 bodů, prohráváš.
Cílem hry je získat co nejvíc bodů, ideálně 21.
"""

def pokracuj(pocet_bodu):
    if pokracovat == "ano" or pokracovat == "a":
        karta = randint(2,10)
        print(f"Otočená karta má hodnotu: {karta}")
        pocet_bodu += karta


nadpis = "Hrajem OKO BERE!"
print(nadpis)
print(len(nadpis) * "*")

pocet_bodu = 0
while True:
    print(f"Máš {pocet_bodu} bodů.")
    if pocet_bodu > 21:
        print("Přesáhl jsi 21! Prohrál jsi!")
        pocet_bodu = 0
    pokracovat = input("Chceš pokračovat? (napiš ano/ne) ")
    if pokracovat == "ne" or pokracovat == "n":
        print(f"Hru uzavíráš s {pocet_bodu} body.")
        break
    elif pokracovat == "ano" or pokracovat == "a":
        karta = randint(2,10)
        print(f"Otočená karta má hodnotu: {karta}")
        pocet_bodu += karta
    else:
        while pokracovat != "ano" or pokracovat != "ne":
            pokracovat = input("Ty nemluvit čecky? Napiš \"ano\" nebo \"ne\"!")
            pokracuj(pocet_bodu)







