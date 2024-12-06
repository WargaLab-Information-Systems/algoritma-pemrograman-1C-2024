basket_club = {"Andi", "Budi", "Cici", "Dewi", "Edi"}
renang_club = {"Budi", "Cici", "Fajar", "Gina", "Hana"}

print("a. Himpunan (set) dari setiap Klub")
print("   Siswa yang mengikuti klub Basket:", basket_club)
print("   Siswa yang mengikuti klub Renang:", renang_club)

# operasi irisan (intersection): mencari anggota yang sama di kedua himpunan
siswa_kedua_klub = basket_club & renang_club
print("b. Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

# operasi selisih simetris (symmetric difference): mencari anggota yang unik di masing-masing himpunan
siswa_satu_klub = basket_club ^ renang_club
print("c. Siswa yang hanya mengikuti satu klub:", siswa_satu_klub)

# operasi gabungan(union): menggabungkan semua anggota dari kedua himpunan
siswa_unik = basket_club | renang_club
print("d. Daftar semua siswa unik yang mengikuti setidaknya satu klub:", siswa_unik)

# menghitung jumlah anggota dalam himpunan gabungan
jumlah_siswa_unik = len(siswa_unik)
print("e. Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)