class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

def main():
    auto1 = Auto("ABC-123", 142)

    print("Rekisteritunnus:", auto1.rekisteritunnus)
    print("Huippunopeus:", auto1.huippunopeus)
    print("Nopeus:", auto1.nopeus)
    print("Matka:", auto1.matka)

    auto1.kiihdytä(30)
    auto1.kiihdytä(70)
    auto1.kiihdytä(50)
    print("Nopeus:", auto1.nopeus)

    auto1.kiihdytä(-200)
    print("Nopeus:", auto1.nopeus)

print(f"Auton rekisteritunnus on: {auto.rekisteritunnus} ja sen nopeus on: {auto.nopeus} ja se on kulkenut matkan: {auto.matka}")