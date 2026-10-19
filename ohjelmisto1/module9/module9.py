


# class auto:
#     pass

# class koulu:
#     pass

# class opiskelija:
#     pass


# opiskelija1 = opiskelija()

# opiskelija1.nimi = "jaakko"
# opiskelija1.syntymävuosi = "2006"
# opiskelija1.keskiarvo = 1

# print(f"{opiskelija1.nimi} on syntynyt vuonna {opiskelija1.syntymävuosi}")



# def kahdenluvunsumma(luku1, luku2):
#     summa = luku1 + luku2
#     return summa

# yhteenlaskettusumma = kahdenluvunsumma(1, 2)

# print(f"summa: {yhteenlaskettusumma}")



class hero:

    sankarien_määrä = 0

    def __init__(self, nimi, tyyppi, voima, aseaani, huudahdus="Hei!"):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.voima = voima
        self.huudahdus = huudahdus
        self.aseaani = aseaani
        hero.sankarien_määrä = hero.sankarien_määrä + 1

    def huuda(self, kerrat=1):
        for i in range(kerrat):
            print(f"{self.huudahdus}")

    def ase(self):
        print(self.aseaani)

hero1 = hero("Roadhog", "Tankki", "Sarjatuli", "RÄTÄTÄTÄTÄTÄTÄ", "(epämääräistä örinää)")
hero2 = hero("Mercy", "Support", "en muista se mistä kaikki revivaantuu", "piu piu")
hero3 = hero("Junkrat", "enmuista", "Räjähtävä rengas", "Poks Poks")

print(f"{hero1.nimi} on {hero1.tyyppi} ja hänen ultimate on {hero1.voima}, hän sanoo {hero1.huudahdus}")
print(f"{hero2.nimi} on {hero2.tyyppi} ja hänen ultimate on {hero2.voima}, hän sanoo {hero2.huudahdus}")
print(f"{hero3.nimi} on {hero3.tyyppi} ja hänen ultimate on {hero3.voima}, hän sanoo {hero3.huudahdus}")

hero1.huuda()
hero1.ase()

hero2.huuda(2)
hero2.ase()

hero2.huuda(2)
hero2.ase()

print(f"Sankarien määrä joukkueessa: {hero.sankarien_määrä}")