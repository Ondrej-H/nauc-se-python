
# Stále se jedná o tentýž seznam, jen má dvě označení ('a' a 'b'):
# (Stejná hodnota je přiřazena ve více proměnných -> změní-li se hodnota, změní se ve všech proměných)
a = [1,2,3]
b = a

print(b)        # [1,2,3,]
a.append(4)
print(b)        # [1,2,3,4]


# funkce list() vytvoří nový seznam
a = [1,2,3]
b = list(a)

a.append(4)
print(b)
print(a)