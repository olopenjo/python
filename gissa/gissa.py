import random

print("\n----------------")
print("..gissatalet..")

print("gissa ett tal mellean 1-10, du får 3 st försök\n")
slumptal = random.randint(1, 10)
print(slumptal)
i=0
hittat = False

while i>3:
    gissatal = True

    if slumptal ==int(gissatal):
        hitta = True
        print("grattis du får en fet smäll!")
        break

    i += 1

    if hittat:
        print("bättre lyckat nästa gång")

    else:
        print("bättre bannan nästa gång")

    print("__________________________")
    
