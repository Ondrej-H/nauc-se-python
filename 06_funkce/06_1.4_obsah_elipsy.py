
from math import pi

def vypocti_obsah_elipsy(a,b):
    """Vypočítá obsah elipsy s poloosami daných délek ('a','b')."""
    # Pouhý výpočet:
    obsah = pi * a * b
    return obsah


# funkce print a input jsou "venku" z funkce vypocti_obsah_elipsy():
x = float(input("Zadejte délku poloosy 1: "))
y = float(input("Zadejte délku poloosy 2: "))
print(f"Obsah elipsy o poloosách {x} a {y} je {vypocti_obsah_elipsy(x,y)}")
