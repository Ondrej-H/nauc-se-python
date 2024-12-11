
# Iterátor zip skončí hned, když dojdou prvky nejkratší sekvence:
veci = ['tráva', 'slunce', 'mrkev', 'list', 'myšlenka', 'spravedlnost']
barvy = ['zelená', 'žluté', 'oranžová', 'zelený']
for vec, barva in zip(veci, barvy):
    print(f"{vec} je {barva}")

print(50*"-")
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
from itertools import zip_longest
for vec, barva in zip_longest(veci, barvy, fillvalue='(nevím)'):    # defaultně fillvalue=None
    print(f"{vec} je {barva}")

print(50*"-")

for vec, barva in zip_longest(veci, barvy):
    if vec == None:
        vec = 'nějaká věc'
    if barva == None:
        barva = 'bez barvy'
    print(f"{vec} je {barva}")


