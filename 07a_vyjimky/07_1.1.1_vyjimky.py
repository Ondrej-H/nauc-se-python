
#int() ->  print(int(8.5))    když dáváme funkci int() jako argument přímo desetiné číslo,
#          zaokrouhlí ho vždy dolů


def nacti_cislo():
    """Získá od uživatele celé číslo a vrátí ho. V případě VallueError vypíše hlášku a opakuje akci."""
    while True:
        odpoved = input("Napiš celé číslo: ")
        try:
            vysledek = int(odpoved)     #int() ->  zde však funkce int() neví, jaký uživatel zadá input (může to být třeba string),
            return vysledek                        # desetinou tečku tak chápe jako string a hlásí, že se nejedná o číslo
        except ValueError:
            print("To není celé číslo! Zkus to znovu.")


print(nacti_cislo())