# Polymorphism (Bab #14)
class MetodePembayaran:
    def bayar(self, nominal):
        return f"Memproses pembayaran sebesar Rp{nominal:,}"

class TransferBank(MetodePembayaran):
    def bayar(self, nominal):
        return f"Transfer bank berhasil: Rp{nominal:,} (biaya admin Rp0)"

class EWallet(MetodePembayaran):
    def bayar(self, nominal):
        return f"Pembayaran E-Wallet berhasil: Rp{nominal:,} (cashback 5%)"

class Tunai(MetodePembayaran):
    def bayar(self, nominal):
        return f"Pembayaran tunai diterima sebesar Rp{nominal:,}"

daftar_pembayaran = [
    TransferBank(),
    EWallet(),
    Tunai()
]

for metode in daftar_pembayaran:
    print(metode.bayar(100000))
