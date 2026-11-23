# Dictionary (Bab #10)
profil_mahasiswa = {
    "nama": "Windi",
    "topik": "Python Dasar",
    "bab_saat_ini": 10
}

print("Nama:", profil_mahasiswa["nama"])
print("Topik:", profil_mahasiswa.get("topik"))

# Menambah & memperbarui key-value
profil_mahasiswa["status"] = "Aktif"
profil_mahasiswa["bab_saat_ini"] = 10

print("\nIsi Dictionary:")
for kunci, nilai in profil_mahasiswa.items():
    print(f"- {kunci}: {nilai}")
