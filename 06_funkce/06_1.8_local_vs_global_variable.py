from math import pi
print(f"pí je: {pi}")
obsah = 0
a = 30

def obsah_elipsy(a, b):
    print(f"Parametr 'a', tedy lokální proměnná 'a' je: {a}")
    obsah = pi * a * b  # Přiřazení do `obsah`
    a = a + 3  # Přiřazení do `a`
    print(f"Lokální proměnná 'a' po +=3 je: {a} a ve funkci se nijak nevyužívá (neslouží pro výpočet)!")
    return obsah


print(f"Obsah elipsy při poloosách a = 30 a b = 20 je: {obsah_elipsy(a, 20)}")
print(f"Globální proměnná 'obsah' je: {obsah}")
print(f"Globální proměnná 'a' je: {a}")
