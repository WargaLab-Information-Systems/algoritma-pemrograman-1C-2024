klub_basket = set()
klub_renang = set()
print("----- Pendaftaran Klub Ekstrakulikuler -----")

while True:
    nama = input("Masukkan nama siswa (ketik '0' untuk keluar)     : ")
    if nama.lower() == '0':
        break

    while True:
        print("===== Pemilihan Klub Basket dan Klub Renang =====")
        pilihan = input("Berapa klub yang akan dipilih 1 atau 2?          : ")
        if pilihan == '1':
            klub = input("Masukkan klub yang diinginkan (basket/renang): ").lower()
            if klub == "basket":
                klub_basket.add(nama)
                break
            elif klub == "renang":
                klub_renang.add(nama)
                break
            else:
                print("Klub tidak valid. Silakan pilih 'basket' atau 'renang'.")
                break
        elif pilihan == '2':
            print("Anda masuk kedalam klub basket dan renang")
            klub_basket.add(nama)
            klub_renang.add(nama)
            break
        else:
            print("Input tidak valid!")
    
kedua_klub = klub_basket.intersection(klub_renang)
print("")
print("Siswa yang mengikuti kedua klub:", kedua_klub)

hanya_satu_klub = (klub_basket.symmetric_difference(klub_renang)) - kedua_klub
print("")
print("Siswa yang hanya mengikuti satu klub:", hanya_satu_klub)

semua_siswa = klub_basket.union(klub_renang)
print("")
print("Semua siswa unik:", semua_siswa)

jumlah_siswa = len(semua_siswa)
print("")
print("Jumlah siswa unik:", jumlah_siswa)