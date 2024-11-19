
x = 0                                               # zde je x globální proměnná

def nastav_x(hodnota):
    x = hodnota  # Přiřazení do lokální proměnné!   # zde je x lokální proměnná
    print('Ve funkci nastav_x: x =', x)

nastav_x(40)                                        # zde je x lokální proměnná
print('Venku: x =', x)                              # zde je x globální proměnná