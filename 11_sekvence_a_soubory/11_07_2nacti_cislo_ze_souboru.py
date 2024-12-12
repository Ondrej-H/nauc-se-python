
def nacti_cele_cislo(jmeno_souboru):
    with open(jmeno_souboru, encoding='utf-8') as soubor:
        return int(soubor.read())
        # I když "return" vyskočí z funkce (nebo int() zbůsobí ValueError),
        # soubor se zavře.


# Pro vyzkoušení napiš do souboru 'cislo.txt' nějaké číslo.
print(nacti_cele_cislo('cislo.txt') * 11)