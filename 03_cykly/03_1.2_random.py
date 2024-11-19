
import random
print()
print(f"random.randint(1,4) - generuje náhodné číslo od 1 do 4 (včetně 4): {random.randint(1,4)}")     # generuje náhodné číslo od 1 do 4 (včetně 4)
print()
print(f"random.randrange(1,4) - generuje náhodné číslo od 1 do 4 (vylučuje 4): {random.randrange(1,4)}")   # generuje náhodné číslo od 1 do 4 (vylučuje 4)
print()
print(f"random.randrage(1,10,2) - generuje náhodné číslo od 1 do 9, ale jen s krokem 2 (tedy 1, 3, 5, 7, 9): {random.randrange(1, 10, 2)}")   # generuje náhodné číslo od 1 do 9, ale jen s krokem 2 (tedy 1, 3, 5, 7, 9)
print()
print(f"random.uniform - generuje náhodné reálné číslo (float): {random.uniform(1,10)}")
print()


from random import randrange

cislo = randrange(0, 3)  # číslo je 0, 1, nebo 2
if cislo == 0:
    print('Kolečko')
elif cislo == 1:
    print('Čtvereček')
else:  # tady musí být číslo 2
    print('Trojúhelníček')
    