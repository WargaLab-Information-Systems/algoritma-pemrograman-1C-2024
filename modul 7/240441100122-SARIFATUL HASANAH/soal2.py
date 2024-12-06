basket = set(input("Masukkan nama siswa yang mengikuti klub Basket (pisahkan dengan koma):").split(","))
renang = set(input("Masukkan nama siswa yang mengikuti klub Renang (pisahkan dengan koma):").split(","))

basket = {nama.strip() for nama in basket}
renang = {nama.strip() for nama in renang}

keduanya = basket.intersection(renang)
print("\nSiswa yang mengikuti kedua klub (Basket dan Renang):")
if keduanya:
    print(f"Ada {len(keduanya)} siswa yang mengikuti kedua klub: {', '.join(keduanya)}")
else:
    print("Tidak ada siswa yang mengikuti kedua klub.")

hanyasatu = basket.symmetric_difference(renang)
print("\nSiswa yang hanya mengikuti satu klub saja (Basket atau Renang):")
if hanyasatu:
    print(f"Ada {len(hanyasatu)} siswa yang hanya mengikuti satu klub: {', '.join(hanyasatu)}")
else:
    print("Tidak ada siswa yang hanya mengikuti satu klub.")

siswa_unik = basket.union(renang)
print("\nDaftar semua siswa unik yang mengikuti setidaknya satu klub:")
if siswa_unik:
    print(f"Ada {len(siswa_unik)} siswa unik yang mengikuti setidaknya satu klub: {', '.join(sorted(siswa_unik))}")
else:
    print("Tidak ada siswa yang mengikuti klub.")


jumlah_siswa_unik = len(siswa_unik)
print("\nJumlah siswa unik yang mengikuti setidaknya satu klub:")
print(jumlah_siswa_unik)
