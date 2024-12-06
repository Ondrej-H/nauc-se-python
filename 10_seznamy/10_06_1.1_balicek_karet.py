# TAKHLE NE!!! (zbytečně dlouhé, opakovaný for)
balicek = []
ciselne_hodnoty = list(range(2, 11))
ciselne_hodnoty_str = []
for hodnota in ciselne_hodnoty:
    ciselne_hodnoty_str.append(str(hodnota))
pismenne_hodnoty = ["J", "Q", "K", "A"]
hodnoty = ciselne_hodnoty_str + pismenne_hodnoty
for barva in '♠', '♥', '♦', '♣':
    for hodnota in hodnoty:
        balicek.append(barva + hodnota)

print(balicek)
