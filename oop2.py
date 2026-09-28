class RekeningBank:
    def __init__(self, pemilik, saldo_awal=0):
        self.pemilik = pemilik
        self.__saldo = saldo_awal # Atribut privat

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setoran Rp{jumlah:,} berhasil. Saldo saat ini: Rp{self.__saldo:,}")
        else:
            print("Jumlah setoran harus lebih besar dari 0.")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Penarikan Rp{jumlah:,} berhasil. Sisa saldo: Rp{self.__saldo:,}")
        else:
            print("Transaksi ditolak: saldo tidak mencukupi atau nilai tidak valid.")

# Uji Enkapsulasi
akun = RekeningBank("Budi", 500_000)
akun.setor(150_000)
akun.tarik(200_000)

# Percobaan manipulasi langsung (tidak akan mengubah atribut privat internal)
akun.__saldo = 10_000_000
print(f"Saldo resmi via getter: Rp{akun.saldo:,}")
