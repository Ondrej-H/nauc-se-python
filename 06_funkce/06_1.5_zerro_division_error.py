
def podel(delenec, delitel):
    """Podělí čísla mezi sebou a vrátí výsledek."""
    return delenec / delitel        # řádek 3


def podel_nulou(cislo):
    """Vydělí dané číslo nulou a vrátí výsledek."""
    return podel(cislo, 0)          # řádek 8


def ukaz_priklad():
    """Spočítá ukázkový příklad a výsledek vypíše (nevrátí!)"""
    vysledek = podel_nulou(3)       # řádek 13
    print(vysledek)

ukaz_priklad()                      # řádek 16