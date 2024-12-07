
balicek = []

for barva in '♠', '♥', '♦', '♣':
    for hodnota in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
        balicek.append(barva + hodnota)

print(balicek)
