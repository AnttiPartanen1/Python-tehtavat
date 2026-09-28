
# g = 1

# while g <= 20:
#     print(g)
#     g += 1



# i = 1

# while i <= 1000:
#     if i % 3 == 0:
#         print (i)
#     i += 1


tuuma = float(input("Anna tuuma määrä minkä haluat muuttaa senteiksi: "))

while tuuma >= 0:
    sentti = tuuma * 2.54
    print("Antamasi tuuma määrä sentteinä: ", sentti)
    tuuma = float(input("Anna tuuma määrä minkä haluat muuttaa senteiksi: "))

print("negatiivinen luku")


# tuumaa = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))

# # while tuumaa >= 0:
#     senttimetria = tuumaa * 2.54
#     print(f"{tuumaa} tuumaa on {senttimetria:.2f} senttimetriä")
#     tuumaa = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))

# print("Ohjelma lopetettu.")