class Mobil:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.kecepatan = 0

    def akselerasi(self, tambah_kecepatan):
        self.kecepatan += tambah_kecepatan
        print(f"{self.merk} {self.model} melaju: {self.kecepatan} km/jam")

    def rem(self, kurangi_kecepatan):
        self.kecepatan = max(0, self.kecepatan - kurangi_kecepatan)
        print(f"{self.merk} {self.model} melambat: {self.kecepatan} km/jam")

# Instansiasi objek
mobil_a = Mobil("Toyota", "Avanza", 2022)
mobil_b = Mobil("Honda", "Civic", 2021)

mobil_a.akselerasi(50)
mobil_a.rem(20)
