# Inisialisasi data siswa
data_siswa = []

# Fungsi CRUD
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah siswa: ")
    
    # Menentukan kelas berdasarkan jumlah siswa
    kelas = len(data_siswa) // 3 + 1
    
    data_siswa.append({"nama": nama, "asal_sekolah": asal_sekolah, "kelas": kelas})
    print(f"Siswa {nama} berhasil ditambahkan ke kelas {kelas}.")

def tampilkan_siswa():
    print("\nDaftar Siswa dan Kelas:")
    if len(data_siswa) == 0:
        print("Tidak ada data siswa.")
    else:
        for siswa in data_siswa:
            print(f"Nama: {siswa['nama']}, Kelas: {siswa['kelas']}, Asal Sekolah: {siswa['asal_sekolah']}")
    print()

def perbarui_siswa():
    nama = input("Masukkan nama siswa yang ingin diperbarui: ")
    siswa_ditemukan = [siswa for siswa in data_siswa if siswa['nama'] == nama]
    
    if siswa_ditemukan:
        siswa = siswa_ditemukan[0]
        print(f"Siswa ditemukan: {siswa['nama']}, Kelas: {siswa['kelas']}, Asal Sekolah: {siswa['asal_sekolah']}")
        siswa['asal_sekolah'] = input("Masukkan asal sekolah baru: ")
        print(f"Data siswa {nama} berhasil diperbarui.")
    else:
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

def hapus_siswa():
    nama = input("Masukkan nama siswa yang ingin dihapus: ")
    siswa_ditemukan = [siswa for siswa in data_siswa if siswa['nama'] == nama]
    
    if siswa_ditemukan:
        data_siswa.remove(siswa_ditemukan[0])
        print(f"Siswa dengan nama {nama} berhasil dihapus.")
    else:
        print(f"Siswa dengan nama {nama} tidak ditemukan.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Siswa")
        print("2. Tampilkan Siswa")
        print("3. Perbarui Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")
        pilihan = input("Pilih nomor menu: ")
        
        if pilihan == "1":
            tambah_siswa()
        elif pilihan == "2":
            tampilkan_siswa()
        elif pilihan == "3":
            perbarui_siswa()
        elif pilihan == "4":
            hapus_siswa()
        elif pilihan == "5":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
menu()