# Virtual Environment & Pip (Bab #18)
import sys
import subprocess

print("Python executable:", sys.executable)
print("Apakah sedang di venv?:", sys.prefix != sys.base_prefix)

# Mengecek paket terinstal via pip list
hasil_pip = subprocess.run(
    [sys.executable, "-m", "pip", "list"],
    capture_output=True,
    text=True,
    check=True
)

print("\nDaftar paket di environment saat ini:")
print(hasil_pip.stdout.strip())
