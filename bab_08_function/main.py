# Function (Bab #8)
def sapa_pengguna(nama, peran="Mahasiswa"):
    return f"Halo {nama} ({peran}), selamat belajar Python!"

def hitung_rata_rata(nilai_list):
    if not nilai_list:
        return 0
    return sum(nilai_list) / len(nilai_list)

pesan = sapa_pengguna("Windi")
rata2 = hitung_rata_rata([85, 90, 88, 92])

print(pesan)
print(f"Rata-rata nilai: {rata2:.2f}")
