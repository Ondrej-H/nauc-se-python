
# Někdy se stane, že jednu šablonu potřebuješ použít vícekrát.
# V takovém případě můžeš šablonu napsat do normálního řetězce (bez f na začátku)
# a použít metodu format:

sablona = 'Ahoj {jmeno}! Tvoje číslo je {cislo}.'
print(sablona.format(cislo=7, jmeno='Hynku'))
print(sablona.format(cislo=42, jmeno='Viléme'))
print(sablona.format(cislo=3, jmeno='Jarmilo'))