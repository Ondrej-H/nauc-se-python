
def rekni_aaa():
    odpoved = input("Řekni \"Ááá\"! ")
    while odpoved != "Ááá":
        print("POŘÁDNĚ!!!")
        odpoved = input("Řekni: \"Ááá\"! ")
    if odpoved == "Ááá":
        print("No vidíš, ani to nebolelo!")


rekni_aaa()


while True:
    odpoved = input('Řekni Ááá! ')
    if odpoved == 'Ááá':
        print('Bééé')
        break
    print('Špatně, zkus to znovu')

print('Hotovo, ani to nebolelo.')