# Inheritance (Bab #13)
class Pengguna:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def perkenalan(self):
        return f"Halo, saya {self.nama} ({self.email})."

class Siswa(Pengguna):
    def __init__(self, nama, email, kelas):
        super().__init__(nama, email)
        self.kelas = kelas

    # Override method dari kelas induk
    def perkenalan(self):
        return f"{super().perkenalan()} Saya siswa kelas {self.kelas}."

    def belajar_bab(self, bab):
        return f"{self.nama} sedang mempelajari Bab #{bab}."

siswa1 = Siswa("Windi", "windi@example.com", "XII RPL")
print(siswa1.perkenalan())
print(siswa1.belajar_bab(13))
