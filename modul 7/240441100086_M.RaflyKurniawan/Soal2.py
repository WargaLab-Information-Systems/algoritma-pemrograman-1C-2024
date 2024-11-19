ekstra_basket = {"Rafly", "Dewi", "Fajar", "Eka"}
ekstra_renang = {"Dewi", "Gita", "Hana", "Rafly"}

print("\nSiswa yang mengikuti klub Basket :", ekstra_basket)
print("\nSiswa yang mengikuti klub renang :", ekstra_renang)

#Intersection
siswa_kedua_klub = ekstra_basket & ekstra_renang
print("\nSiswa yang mengikuti kedua klub :", siswa_kedua_klub)

#Symmetric difference
siswa_satu_klub = ( ekstra_basket ^ ekstra_renang)
print("\nSiswa yang hanya mengikuti satu klub :", siswa_satu_klub)

#Union
siswa_unik = ekstra_basket | ekstra_renang
print("\nDaftar semua siswa unik yang mengikuti setidaknya satu klub :", siswa_unik)

#Jumlah setidaknya ikut 1 klub
jumlah_siswa_unik = len(siswa_unik)
print("\nJumlah siswa unik yang mengikuti setidaknya satu klub :", jumlah_siswa_unik)
