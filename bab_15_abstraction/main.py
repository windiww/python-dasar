# Abstraction (Bab #15)
from abc import ABC, abstractmethod
import math

class BangunDatar(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass

    @abstractmethod
    def hitung_keliling(self):
        pass

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return math.pi * (self.jari_jari ** 2)

    def hitung_keliling(self):
        return 2 * math.pi * self.jari_jari

pp = PersegiPanjang(10, 5)
ling = Lingkaran(7)

print(f"Persegi Panjang -> Luas: {pp.hitung_luas()}, Keliling: {pp.hitung_keliling()}")
print(f"Lingkaran       -> Luas: {ling.hitung_luas():.2f}, Keliling: {ling.hitung_keliling():.2f}")
