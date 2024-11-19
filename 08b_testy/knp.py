import random

def urci_vyteze(tah_hrace, tah_pocitace):
    """Vyhodnotí, kdo vyhrál hru kámen nůžky papír."""
    if tah_hrace == tah_pocitace:
        return "Remíza!"
    elif (tah_hrace, tah_pocitace) == ("kámen", "nůžky") or \
        (tah_hrace, tah_pocitace) == ("nůžky", "papír") or \
        (tah_hrace, tah_pocitace) == ("papír", "kámen"):
        return "Vyhrál hráč!"
    #elif (tah_hrace, tah_pocitace) == ("kámen", "papír") or \
    #    (tah_hrace, tah_pocitace) == ("nůžky", "kámen") or \
    #    (tah_hrace, tah_pocitace) == ("papír", "nůžky"):
    #    return "Vyhrál počítač!"
    else:
        return "Vyhrál počítač!"


def hraj_knp():
    volby = ["kámen", "nůžky", "papír"]
    tah_hrace = input("Hráč: ")
    while tah_hrace not in volby:
        tah_hrace = input("Vyber kámen, nůžky nebo papír: ")
    tah_pocitace = random.choice(volby)
    print(f"Počítač: {tah_pocitace}")

    vysledek = urci_vyteze(tah_hrace, tah_pocitace)
    print(vysledek)


# kámen > nůžky
# nužky > papír
# papír > kámen