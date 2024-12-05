# Dictionary untuk menyimpan data siswa berdasarkan kelas
kelas_siswa = {}

# Menambahkan siswa ke kelas
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah: ")

    # Tentukan kelas berdasarkan jumlah siswa yang sudah ada
    kelas = (sum(len(siswa) for siswa in kelas_siswa.values()) // 3) + 1

    # Tambahkan siswa ke kelas yang sesuai
    if kelas not in kelas_siswa:
        kelas_siswa[kelas] = []
        
    # Jika kelas penuh, buat kelas baru
    if len(kelas_siswa[kelas]) < 3:
        kelas_siswa[kelas].append({"nama": nama, "asal_sekolah": asal_sekolah})
        print(f"Siswa {nama} berhasil ditambahkan ke kelas {kelas}.")
    else:
        # Kelas penuh, buat kelas baru dan masukkan siswa ke kelas baru
        kelas += 1
        kelas_siswa[kelas] = [{"nama": nama, "asal_sekolah": asal_sekolah}]
        print(f"Kelas penuh! Siswa {nama} dipindahkan ke kelas {kelas}.")

# Menampilkan siswa dalam setiap kelas
def tampilkan_siswa():
    if not kelas_siswa:
        print("Belum ada siswa terdaftar.")
        return

    for kelas, siswa_list in kelas_siswa.items():
        print(f"\nKelas {kelas}:")
        for siswa in siswa_list:
            print(f"  Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")

# Mengupdate data siswa
def update_siswa():
    nama = input("Masukkan nama siswa yang ingin diupdate: ")

    # Cari siswa berdasarkan nama
    for kelas, siswa_list in kelas_siswa.items():
        for siswa in siswa_list:
            if siswa["nama"].lower() == nama.lower():
                print(f"Data siswa ditemukan: Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")
                # Update data asal sekolah
                siswa["asal_sekolah"] = input("Masukkan asal sekolah baru: ")
                print(f"Data siswa {nama} berhasil diupdate.")
                break

    if not kelas_siswa:
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

# Menghapus siswa dari kelas
def hapus_siswa():
    nama = input("Masukkan nama siswa yang ingin dihapus: ")

    # Cari siswa dan hapus
    for kelas, siswa_list in kelas_siswa.items():
        for siswa in siswa_list:
            if siswa["nama"].lower() == nama.lower():
                siswa_list.remove(siswa)
            
                print(f"Siswa {nama} telah dihapus.")
                break
    
    if not kelas_siswa:
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

# Main program
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Siswa")
        print("2. Tampilkan Siswa per Kelas")
        print("3. Update Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Keluar")
        pilihan= input("Pilih nomor menu: ")

        if pilihan == "1":
            tambah_siswa()
        elif pilihan == "2":
            tampilkan_siswa()
        elif pilihan == "3":
            update_siswa()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih menu yang benar.")

menu()