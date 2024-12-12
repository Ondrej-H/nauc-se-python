
with open('druha-basnicka.txt', 'w', encoding='utf-8') as f:
    print('Naše staré hodiny', file=f)
    print('Bijí', 2+2, 'hodiny', file=f)

# verze z naucse-python:
with open('druha-basnicka.txt', mode='w', encoding='utf-8') as soubor:
    print('Naše staré hodiny', file=soubor)
    print('Bijí', 2+2, 'hodiny', file=soubor)