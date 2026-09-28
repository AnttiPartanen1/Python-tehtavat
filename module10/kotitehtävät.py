class hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ylin_kerros:
            kerros = self.ylin_kerros
        elif kerros < self.alin_kerros:
            kerros = self.alin_kerros

        while self.nykyinen_kerros < kerros:
            self.kerros_ylos()

        while self.nykyinen_kerros > kerros:
            self.kerros_alas()


def paaohjelma():
    h = hissi(0, 200000000)

    print("Hissi on kerroksessa", h.nykyinen_kerros)

    print("Hissi siirtyy kerrokseen 5:")
    h.siirry_kerrokseen(4567890)

    print("Hissi siirtyy alimpaan kerrokseen:")
    h.siirry_kerrokseen(h.alin_kerros)


if __name__ == "__main__":
    paaohjelma()

