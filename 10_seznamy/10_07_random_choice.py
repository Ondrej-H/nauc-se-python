import random

# definuje funkci hraj
def hraj(tah_hrace, tah_pocitace):
    if tah_hrace == tah_pocitace:
        print("Remíza!")
    elif (tah_hrace, tah_pocitace) == ("kámen", "nůžky") or \
        (tah_hrace, tah_pocitace) == ("nůžky", "papír") or \
        (tah_hrace, tah_pocitace) == ("papír", "kámen"):
        print("Vyhrál hráč!")
    else:
        print("Vyhrál počítač!")


mozne_tahy = ['kámen', 'nůžky', 'papír']
# načte vstup (tah) od uživatele a vyhodnotí tah počítače
tah_hrace = input("Hráč 1: ")
tah_pocitace = random.choice(mozne_tahy)
print(f"Počítač: {tah_pocitace}")

# zavolá funkci
hraj(tah_hrace, tah_pocitace)

# kámen > nůžky
# nužky > papír
# papír > kámen
