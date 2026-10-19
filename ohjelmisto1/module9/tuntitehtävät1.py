# class pelaaja:

#     def __init__(self, nimi, elämät=3, kolikot=0, pisteet=0):
#         self.nimi = nimi
#         self.elämät = elämät
#         self.kolikot = kolikot
#         self.pisteet = pisteet


# pelaaja1 = pelaaja("Mario")

# print(f"Pelaajan 1 nimi on:{pelaaja1.nimi} Jäljellä olevat elämät:{pelaaja1.elämät} Kolikot:{pelaaja1.kolikot}, Pisteet:{pelaaja1.pisteet}")


class laiva:

    def __init__(self, nimi, tykit=12, miehistö=40, kulta=0):
        self.nimi = nimi
        self.tykit = tykit
        self.miehistö = miehistö
        self.kulta = kulta
        

    def löydä_aarre(self, maara):
        self.kulta = self.kulta + maara

    def menetä_kultaa(self, maara):
        self.kulta = self.kulta - maara >= 0


    if self.kulta < 0:
        self.kulta = 0

laiva1 = laiva("The Black Pearl")

print(f"Laivan nimi on:{laiva1.nimi}, sillä on kannellaan tykkejä {laiva1.tykit} sen miehistön vahvuus on {laiva1.miehistö} ja kultaa laivalla on {laiva1.kulta}")

