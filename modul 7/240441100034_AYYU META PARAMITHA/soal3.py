# Fungsi untuk menampilkan menu pilihan
def tampilkan_menu():
    print("\nMenu:")
    print("1. Tambah Siswa")
    print("2. Lihat Data Siswa")
    print("3. Ubah Data Siswa")
    print("4. Hapus Data Siswa")
    print("5. Keluar")

# Fungsi untuk menambah siswa ke dalam kelas
def tambah_siswa(data_siswa):
    nama = input("\nMasukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah siswa: ")
    
    # Tentukan kelas siswa berdasarkan jumlah siswa yang ada
    kelas_terakhir = len(data_siswa) // 3 + 1
    kelas = f"Kelas {kelas_terakhir}"

    # Menambahkan data siswa ke dalam kelas
    data_siswa.append({"nama": nama, "asal_sekolah": asal_sekolah, "kelas": kelas})
    print(f"Siswa {nama} berhasil ditambahkan ke {kelas}.")

# Fungsi untuk melihat semua data siswa dan plotting bimbingan
def lihat_data_siswa(data_siswa):
    if not data_siswa:
        print("\nTidak ada data siswa.")
        return

    print("\nDaftar Siswa:")
    kelas_terdaftar = {}
    for siswa in data_siswa:
        if siswa["kelas"] not in kelas_terdaftar:
            kelas_terdaftar[siswa["kelas"]] = []
        kelas_terdaftar[siswa["kelas"]].append(siswa)

    for kelas, siswa_list in kelas_terdaftar.items():
        print(f"\n{kelas}:")
        for siswa in siswa_list:
            print(f"- {siswa['nama']} (Asal Sekolah: {siswa['asal_sekolah']})")

# Fungsi untuk mengubah data siswa (misalnya, mengubah asal sekolah atau kelas)
def ubah_data_siswa(data_siswa):
    nama = input("\nMasukkan nama siswa yang akan diubah: ")
    
    siswa_ditemukan = False
    for siswa in data_siswa:
        if siswa["nama"].lower() == nama.lower():
            siswa_ditemukan = True
            print(f"Data siswa ditemukan: {siswa['nama']} - {siswa['asal_sekolah']} - {siswa['kelas']}")
            pilihan = input("Apa yang ingin diubah? (1) Asal Sekolah, (2) Kelas: ")

            if pilihan == "1":
                siswa["asal_sekolah"] = input("Masukkan asal sekolah baru: ")
                print(f"Data asal sekolah {nama} telah diperbarui.")
            elif pilihan == "2":
                siswa["kelas"] = input("Masukkan kelas baru: ")
                print(f"Data kelas {nama} telah diperbarui.")
            else:
                print("Pilihan tidak valid.")
            break

    if not siswa_ditemukan:
        print(f"\nSiswa dengan nama {nama} tidak ditemukan.")

# Fungsi untuk menghapus data siswa
def hapus_data_siswa(data_siswa):
    nama = input("\nMasukkan nama siswa yang akan dihapus: ")

    siswa_ditemukan = False
    for siswa in data_siswa:
        if siswa["nama"].lower() == nama.lower():
            siswa_ditemukan = True
            data_siswa.remove(siswa)
            print(f"Siswa {nama} telah dihapus.")
            break

    if not siswa_ditemukan:
        print(f"\nSiswa dengan nama {nama} tidak ditemukan.")

# Program utama
def main():
    data_siswa = []  # List untuk menyimpan data siswa
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_siswa(data_siswa)
        elif pilihan == "2":
            lihat_data_siswa(data_siswa)
        elif pilihan == "3":
            ubah_data_siswa(data_siswa)
        elif pilihan == "4":
            hapus_data_siswa(data_siswa)
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")

main()
