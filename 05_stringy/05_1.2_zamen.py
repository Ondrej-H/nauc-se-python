
# načte vstupy od uživatele
slovo = input("Jaké slovo chceš upravit? ")
pozice = int(input("Kolikáté písmeno chceš zaměnit (první písmeno je 0, druhé je 1, třetí 2 atd.)? "))
novy_znak = input("Jakým písmenem nebo znakem chceš zvolené písmeno nahradit? ")

# rozdělí původní slovo podle zadaného indexu, přičemž zadaný index bude vynechán v obou částech slova (pozice+1)
prvni_cast_slova = slovo[:pozice]
druha_cast_slova = slovo[pozice+1:]

# vytvoří nový string
nove_slovo = prvni_cast_slova + novy_znak + druha_cast_slova

print(nove_slovo)
