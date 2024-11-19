
# 
jmeno = input("Jméno: ")
prijmeni = input("Příjmení: ")

# Když chceš celý výpis uložit do proměnné jako jeden řetězec,
# čárka tu fungovat nebude. Ta odděluje argumenty ve volání funkce.
inicialy = jmeno[0] + "." + prijmeni[0] + "."   # s čárkou by byl výpis brán jako tupl a protože tupl není string,
print(f"Iniciály: {inicialy.upper()}")          # nelze nad ním volat metodu pro stringy (tedy například .upper)
