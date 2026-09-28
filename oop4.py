class Pembayaran:
    def proses(self, jumlah):
    	raise NotImplementedError("Subclass harus menerapkan method ini.")

class TransferBank(Pembayaran):
    def proses(self, jumlah):
        print(f"[Virtual Account] Verifikasi transfer bank sebesar Rp{jumlah:,}")

class EWallet(Pembayaran):
    def proses(self, jumlah):
        print(f"[QRIS/E-Wallet] Pemotongan saldo instan sebesar Rp{jumlah:,}")

class KartuKredit(Pembayaran):
    def proses(self, jumlah):
        print(f"[Credit Card] Otorisasi kartu kredit sebesar Rp{jumlah:,}")

# Pemanggilan polimorfik
saluran_transaksi = [
    TransferBank(),
    EWallet(),
    KartuKredit()
]

tagihan = 250_000
for saluran in saluran_transaksi:
    saluran.proses(tagihan)
