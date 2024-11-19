from random import randint

pocet_bodu = 0 

while True:
    print(f"Máš {pocet_bodu} bodů.")
    if pocet_bodu == 21:
        print("Oko bere!!! Vyhrál/a jsi s 21 body!")
        break
    elif pocet_bodu > 21:
        print("Přesáhl jsi 21 bodů! Prohrál/a jsi.")
        break
    if pocet_bodu >= 19:
        print("To je slušný počet bodů!")
    pokracovat = input("Chceš pokračovat? Pokud ne, napiš 'n' a stisni enter, jinak pouze stiskni enter: ")
    if pokracovat == "n":
        print(f"Tuto hru končíš s {pocet_bodu} body.")
        if pocet_bodu >= 19:
            print("Dobré skóre!")
        break
    else:
        hodnota_karty = randint(2,10)
        pocet_bodu += hodnota_karty
        print(f"Hodnota nové otočené karty je: {hodnota_karty}")
