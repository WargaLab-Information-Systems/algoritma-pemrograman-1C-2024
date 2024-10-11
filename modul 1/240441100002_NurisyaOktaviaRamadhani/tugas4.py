import math

n = int(input("masukkan total orang: "))
r = int(input("masukkan orang yang dipilih: "))
kombinasi = math.comb(n, r)

print(f"jumlah kombinasi dari {n} orang yang diambil {r} adalah : {kombinasi}")