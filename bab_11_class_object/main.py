# Class & Object - OOP Dasar (Bab #11)
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan
        self.bab_selesai = 0

    def selesaikan_bab(self, nomor_bab):
        self.bab_selesai = nomor_bab
        return f"{self.nama} menyelesaikan Bab #{nomor_bab}"

    def info(self):
        return f"Mahasiswa: {self.nama} | Jurusan: {self.jurusan} | Bab Selesai: {self.bab_selesai}"

mhs1 = Mahasiswa("Windi", "Informatika")
print(mhs1.selesaikan_bab(11))
print(mhs1.info())
