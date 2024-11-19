
for i in range(10):  # Vnější cyklus
    print(f"Teď je i: {i}")
    for j in range(10):  # Vnitřní cyklus
        print(f"Teď je j: {j}")
        print(j * i, end=' ')
        print()
        if i <= j:
            break
    print()