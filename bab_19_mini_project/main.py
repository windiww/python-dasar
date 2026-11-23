# Mini Project / Penutup Python Dasar (Bab #19)
class Tugas:
    def __init__(self, judul):
        self.judul = judul
        self.selesai = False

    def tandai_selesai(self):
        self.selesai = True

    def __str__(self):
        status = "[x]" if self.selesai else "[ ]"
        return f"{status} {self.judul}"


class ManajerTugas:
    def __init__(self):
        self.daftar_tugas = []

    def tambah(self, judul):
        judul_bersih = judul.strip()
        if not judul_bersih:
            raise ValueError("Judul tugas tidak boleh kosong.")
        self.daftar_tugas.append(Tugas(judul_bersih))

    def selesaikan(self, nomor):
        if nomor < 1 or nomor > len(self.daftar_tugas):
            raise IndexError("Nomor tugas tidak ditemukan.")
        self.daftar_tugas[nomor - 1].tandai_selesai()

    def tampilkan(self):
        if not self.daftar_tugas:
            print("Belum ada tugas.")
            return
        for idx, item in enumerate(self.daftar_tugas, start=1):
            print(f"{idx}. {item}")


manajer = ManajerTugas()

try:
    manajer.tambah("Menyelesaikan Bab #19 Python Dasar")
    manajer.tambah("Merapikan README.md dan requirements.txt")
    manajer.selesaikan(1)
except ValueError as err:
    print("Error:", err)

print("Daftar Tugas Saat Ini:")
manajer.tampilkan()
