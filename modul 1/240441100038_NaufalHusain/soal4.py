# Import Modul untuk menyediakan berbagai fungsi matematika
import math

Jumlah_orang =int(input("Masukkan Jumlah total orang : "))
Jumlah_Orang_pertim = int(input("Masukkan berapa orang dalam 1 tim : "))

# Rumus menghitung kombinasi C(n, r) = n! / (r! * (n - r)!)

# math.comb untuk menghitung kombinasi
jumlah_cara = math.comb(Jumlah_orang, Jumlah_Orang_pertim)

# Menampilkan hasil
print(f"Banyak cara untuk membentuk tim dari {Jumlah_orang} orang dengan memilih {Jumlah_Orang_pertim} orang adalah: {jumlah_cara}")

