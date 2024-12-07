
# tupl nelze měnit pomocí tupl[index]
# lze je ale pomocí tupl[index] číst:
osoby = 'máma', 'teta', 'babička'
for osoba in osoby:
    print(osoba)

prvni = osoby[0]
print(f'První je {prvni}')