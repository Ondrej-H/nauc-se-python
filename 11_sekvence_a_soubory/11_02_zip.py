
veci = ['tráva', 'slunce', 'mrkev', 'list']
barvy = ['zelená', 'žluté', 'oranžová', 'zelený']
mista = ['na zemi', 'nahoře', 'na talíři', 'na stromě']
cisla = range(1,5)

print (30 * "-")
print(zip(veci, barvy))
print (30 * "-")
print(list(zip(veci, barvy)))
print (30 * "-")

for vec, barva, misto, cislo in zip(veci, barvy, mista, cisla):
    print(f"{cislo}. {barva} {vec} je {misto}.")
