
# TOTO NEFUNGUJE!!!
def nacti_cislo():
    """Získá od uživatele celé číslo a vrátí ho. V případě VallueError vypíše hlášku a opakuje akci."""
    while True:
        odpoved = input("Napiš číslo: ")
        try:
            if int(odpoved) is True:
                print("int(odpoved) is True.")
                vysledek = int(odpoved)
                return vysledek
            elif odpoved.find(".") is True:
                print("odpoved.find(\".\") is True")
                index_tecky = odpoved.find(".")
                odpoved = odpoved[:index_tecky]
                vysledek = int(odpoved)
                return vysledek
        except ValueError:
            print("To není celé číslo! Zkus to znovu.")
# TOTO NEFUNGUJE!!!

# TOTO NEFUNGUJE!!!
print(nacti_cislo())
# TOTO NEFUNGUJE!!!
