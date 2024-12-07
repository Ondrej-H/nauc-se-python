# Takhle ano :-)
import random

balicek = []
ciselne_hodnoty = list(range(2,11))
pismenne_hodnoty = list("JQKA")
hodnoty = ciselne_hodnoty + pismenne_hodnoty

for barva in '♠', '♥', '♦', '♣':
    for hodnota in hodnoty:
        balicek.append(barva + str(hodnota))

print(balicek)

# random.shuffle zamíchá (randomizuje) balíček
random.shuffle(balicek)
print(balicek)

# random.choice vybere ze seznamu náhodný prvek
tah_pocitace = random.choice(balicek)
print(tah_pocitace)