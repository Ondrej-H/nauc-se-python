# slicing vytváří nový seznam:
zviratka = ['pes', 'kočka', 'králík', 'had', 'andulka']
zviratka_2 = zviratka[1:-2]

print(zviratka)
print(zviratka_2)

# metody pouze upravují seznam původní:
zviratka_3 = zviratka.append("gorila")
print(zviratka)
print(zviratka_3)   # metody (kromě pop()) vrací None, jen upravují původní seznam