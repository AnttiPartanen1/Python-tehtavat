# kerrat = int(input("Montako kertaa tervehditään: "))
# tehdyt = 0
# while tehdyt < kerrat:
#     print("Hyvää huomenta")
#     tehdyt = tehdyt + 1

# komento = input("Anna komento: ")
# while komento != "lopeta":
#     print("Suoritan toiminnon: " + komento)
#     komento = input("Anna komento: ")
# print("Toiminnot lopetettu.")


import random
noppa1 = noppa2 = heitot = 0
while (noppa1 != 6 or noppa2 != 6):
    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    heitot = heitot + 1
print(f"Tarvittiin {heitot:d} heittoa.")

luku = 0 + 1
while luku < 5:
    print(luku)