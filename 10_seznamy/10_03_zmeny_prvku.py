# Změna prvku v seznamu:
zviratka = ['pes', 'kočka', 'králík']
zviratka[1] = 'koťátko'
print(zviratka)

# Přiřazovat se dá i do podseznamu:
zviratka = ['pes', 'kočka', 'králík', 'had', 'andulka']
print(zviratka[1:-2])
zviratka[1:-2] = ['koťátko', 'králíček']
print(zviratka)
print(40 * "-")


# POZOR seznam se dá zcela změnit (smazat prvky) i přiřazením do podseznamu:
zviratka = ['pes', 'kočka', 'králík']
zviratka[1:-1] = ['had', 'ještěrka', 'drak']
print(zviratka)
zviratka[1:-1] = []
print(zviratka)