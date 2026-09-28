from abc import ABC, abstractmethod

class Notifikasi(ABC):
    def __init__(self, penerima):
        self.penerima = penerima

    @abstractmethod
    def kirim_pesan(self, pesan):
        pass

class NotifikasiTelegram(Notifikasi):
    pass

class NotifikasiWhatsapp(Notifikasi):
    def kirim_pesan(self, pesan):
        print(f"SENT TO: {self.penerima}: '{pesan}'")

wa = NotifikasiWhatsapp("08123456789")
wa.kirim_pesan("Halo, ini uji coba pesan WhatsApp.")
