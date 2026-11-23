# Control Flow (Bab #7)
nilai = 88

# Percabangan if / elif / else
if nilai >= 85:
    predikat = "A"
elif nilai >= 75:
    predikat = "B"
else:
    predikat = "C"

print(f"Nilai: {nilai} | Predikat: {predikat}")

# Perulangan for
print("Daftar bab yang sudah dilewati:")
for bab in range(1, 8):
    print(f"- Bab #{bab}")

# Perulangan while
hitungan = 3
while hitungan > 0:
    print(f"Mulai dalam {hitungan}...")
    hitungan -= 1
