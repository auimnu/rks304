class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info(self):
        return f"Nama: {self.nama} | Gaji Pokok: Rp{self.gaji_pokok:,}"

class Manajer(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def total_pendapatan(self):
        return self.gaji_pokok + self.tunjangan

    def info(self):
        detail_dasar = super().info()
        return f"{detail_dasar} | Tunjangan: Rp{self.tunjangan:,} | Total: Rp{self.total_pendapatan():,}"

# Uji Pewarisan
staf = Karyawan("Fulan", 5_000_000)
lead = Manajer("Siti", 12_000_000, 3_500_000)

print(staf.info())
print(lead.info())
