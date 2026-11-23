# Encapsulation (Bab #12)
class DompetDigital:
    def __init__(self, pemilik, saldo_awal, pin):
        self.pemilik = pemilik
        self._saldo = saldo_awal      # Protected attribute (konvensi internal/subclass)
        self.__pin = pin            # Private attribute (name mangling)

    def lihat_saldo(self, pin_input):
        if pin_input == self.__pin:
            return f"Saldo {self.pemilik}: Rp{self._saldo:,}"
        return "PIN salah! Akses saldo ditolak."

    def tambah_saldo(self, nominal, pin_input):
        if pin_input != self.__pin:
            return "PIN salah! Gagal top-up."
        if nominal <= 0:
            return "Nominal harus lebih besar dari 0."
        self._saldo += nominal
        return f"Top-up berhasil. Saldo baru: Rp{self._saldo:,}"

dompet = DompetDigital("Windi", 50000, "1234")
print(dompet.lihat_saldo("1234"))
print(dompet.tambah_saldo(25000, "1234"))
print(dompet.lihat_saldo("0000"))
