# Exception Handling & File I/O (Bab #17)
from pathlib import Path

folder_bab = Path(__file__).parent
file_catatan = folder_bab / "catatan.txt"

def bagi_angka(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        return "Error: Tidak bisa membagi dengan nol."
    except TypeError:
        return "Error: Input harus berupa angka."
    else:
        return f"Hasil pembagian {a} / {b} = {hasil}"
    finally:
        pass

print(bagi_angka(20, 4))
print(bagi_angka(20, 0))

# Menulis dan membaca file teks
with open(file_catatan, "w", encoding="utf-8") as f:
    f.write("Progress belajar Python Dasar mencapai Bab #17.\n")
    f.write("Exception handling dan file I/O berjalan normal.\n")

with open(file_catatan, "r", encoding="utf-8") as f:
    isi = f.read()

print("\nIsi berkas catatan.txt:")
print(isi.strip())
