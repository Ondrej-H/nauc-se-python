
# 1. varianta
dny = ['Po', 'Út', 'St', 'Čt', 'Pá', 'So', 'Ne']
for index, den in enumerate(dny):
    print(f"{index + 1}. {den}")

# lepší varianta
dny = ['Po', 'Út', 'St', 'Čt', 'Pá', 'So', 'Ne']
for index, den in enumerate(dny, start=1):          # fce enumerate bere jako klíčový argument od jakého čísla má začít (start=1)
    print(f"{index}. {den}")