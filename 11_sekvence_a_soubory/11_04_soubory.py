
# nutno spustit přímo z příkazové řádky,
# protože workspace UCENI_PYTHON, má nastavenou jinou výchozí adresu
# (následující dva zakomentované řádky vypíšou jakou adresu)
#import os
#print(os.getcwd())

# takto lze nahlédnou do souboru ...:
soubor = open('basnicka.txt', encoding='utf-8')
obsah = soubor.read()
soubor.close()

print(obsah)

# ... správné přistupování k souborům ale vypadá takto:
with open('basnicka.txt', encoding='utf-8') as soubor:
    obsah = soubor.read()

print(obsah)