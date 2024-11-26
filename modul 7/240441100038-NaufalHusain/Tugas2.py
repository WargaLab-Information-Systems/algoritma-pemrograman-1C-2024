# program menampilkan siswa yang mengikuti klub ekstrakulikuler di sekolah


# Membuat dua set untuk siswa yang mengikuti klub Basket dan Renang
# variabel basket, renang diinisialisasi sebagai set
basket = set()
renang = set()

# program untuk menambahkan siswa ke set tertentu
# fungsi tambah siswa dengan parameter nama, dan klub menggunakan tipe data string
def tambah_siswa(nama, klub):
    if klub.lower() == "basket": #lower untuk mengubah huruf tipe data string menjadi huruf krcil
        basket.add(nama) #tambahkan nama ke dalam basket
    elif klub.lower() == "renang":
        renang.add(nama)
    else:
        print("Klub tidak dikenal. Pilih antara 'basket' atau 'renang'.")

# Fungsi untuk menampilkan siswa yang mengikuti kedua klub
def siswa_kedua_klub():
    return basket.intersection(renang) #kembalikan irisan antara basket dan renang

# Fungsi untuk menampilkan siswa yang hanya mengikuti satu klub
def siswa_satu_klub():
    return basket.symmetric_difference(renang)

# Fungsi untuk menampilkan semua siswa unik yang mengikuti setidaknya satu klub
def semua_siswa_unik():
    return basket.union(renang)

# Fungsi untuk menampilkan jumlah siswa unik
def jumlah_siswa_unik():
    return len(semua_siswa_unik())

# Menu dinamis
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambahkan dua set siswa yang mengikuti klub basket dan renang")
        print("2. Tampilkan siswa yang mengikuti kedua klub")
        print("3. Tampilkan siswa yang hanya mengikuti satu klub")
        print("4. Tampilkan daftar semua siswa unik yang mengikuti setidaknya 1 klub")
        print("5. Tampilkan jumlah siswa unik yang mengikuti setidaknya 1 klub")
        print("6. Keluar")
        
        pilihan = input("Pilih opsi (1-6): ")

        # jika variabel pilihan sama dengan 1 jalankan program di bawah ini
        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            klub = input("Masukkan klub ('basket' atau 'renang'): ")
            tambah_siswa(nama, klub)
        # jika variabel pilihan tidak dengan 1 apakah variabel pilihan sama dengan 2, jalankan pemrograman di bawah ini
        elif pilihan == "2":
            print("Siswa yang mengikuti kedua klub:")
            hasil = siswa_kedua_klub()
            if hasil:
                print(hasil)
            else:
                print("Tidak ada siswa yang mengikuti kedua klub.")

        # jika variabel pilihan tidak dengan 2 apakah variabel pilihan sama dengan 3, jalankan pemrograman di bawah ini
        elif pilihan == "3":
            print("Siswa yang hanya mengikuti satu klub:")
            hasil = siswa_satu_klub()
            if hasil:
                print(hasil)
            else:
                print("Semua siswa mengikuti kedua klub atau tidak ada siswa yang terdaftar.")

        # jika variabel pilihan tidak dengan 3 apakah variabel pilihan sama dengan 4, jalankan pemrograman di bawah ini
        elif pilihan == "4":
            print("Semua siswa unik yang mengikuti setidaknya satu klub:")
            hasil = semua_siswa_unik()
            if hasil:
                print(hasil)
            else:
                print("Belum ada siswa yang terdaftar di klub.")

        # jika variabel pilihan tidak dengan 4 apakah variabel pilihan sama dengan 5, jalankan pemrograman di bawah ini
        elif pilihan == "5":
            print("Jumlah siswa unik yang mengikuti setidaknya satu klub:")
            print(jumlah_siswa_unik())
        
        elif pilihan == "6":
            print("Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan menu
menu()

