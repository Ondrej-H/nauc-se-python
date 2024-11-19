
def nacti_cislo():
    """Získá od uživatele celé číslo a vrátí ho. V případě VallueError vypíše hlášku a opakuje akci."""
    while True:
        odpoved = input("Napiš číslo: ")
        try:
            vysledek = int(odpoved)
            return vysledek
        except ValueError:
            try:    # bylo by lepší zde nechat vyvstat chybu, toto je jen pokus o zanoření dalšího try, except
                index_tecky = odpoved.find(".")
                odpoved = odpoved[:index_tecky]
                vysledek = int(odpoved)
                return vysledek
            except ValueError:
                print("To není celé číslo! Zkus to znovu.")


print(nacti_cislo())
