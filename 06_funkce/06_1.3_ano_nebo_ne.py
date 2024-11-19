
# return plní zároveň funkci (jakoby)break:
def ano_nebo_ne(otazka):
    """Vrátí True nebo False podle odpovědi uživatele.
    Parameter 'otazka' se objeví jako otázka při zadávání vstupu uživatele."""
    while True:
        odpoved = input(otazka + " ")
        if odpoved.lower() == "ano":
            return True
        elif odpoved.lower() == "ne":
            return False
        # zde není třeba dávat else blok, protože return zde funguje podobně jako break
        # proto se následující kód (print()) provede pouze pokud nebyla splněna žádná z podmínek výše:
        print("Nerozumím. Napiš 'ano' nebo 'ne'")


if ano_nebo_ne("Chceš si zahrát hru?"):
    print("Ok! Nejdřív si ji ale musíš naprogramovat.")
else:
    print("Škoda.")
