# Inisialisasi data siswa
data_siswa = []

# Fungsi menambah siswa
def tambah_siswa():
    jumlah = int(input("Masukkan jumlah siswa yang ingin didaftarkan: "))
    for i in range(jumlah):
        nama = input("Nama siswa: ")
        asal_sekolah = input("Asal sekolah: ")
        data_siswa.append({"nama": nama, "asal_sekolah": asal_sekolah})
    print(f"{jumlah} siswa berhasil ditambahkan.")

# Fungsi menampilkan semua data siswa
def tampilkan_siswa():
    if not data_siswa:
        print("Belum ada data siswa.")
        return
    print("Data Siswa:")
    for index, siswa in enumerate(data_siswa, start=1):
        print(f"{index}. Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")

# Fungsi memperbarui data siswa
def update_siswa():
    tampilkan_siswa()
    if not data_siswa:
        return
    try:
        nomor = int(input("Masukkan nomor siswa yang ingin diperbarui: ")) - 1
        if 0 <= nomor < len(data_siswa):
            nama_baru = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
            sekolah_baru = input("Masukkan asal sekolah baru (kosongkan jika tidak diubah): ")
            if nama_baru:
                data_siswa[nomor]["nama"] = nama_baru
            if sekolah_baru:
                data_siswa[nomor]["asal_sekolah"] = sekolah_baru
            print("Data siswa berhasil diperbarui.")
        else:
            print("Nomor siswa tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Fungsi menghapus data siswa
def hapus_siswa():
    tampilkan_siswa()
    if not data_siswa:
        return
    try:
        nomor = int(input("Masukkan nomor siswa yang ingin dihapus: ")) - 1
        if 0 <= nomor < len(data_siswa):
            siswa_terhapus = data_siswa.pop(nomor)
            print(f"Siswa bernama {siswa_terhapus['nama']} berhasil dihapus.")
        else:
            print("Nomor siswa tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Fungsi utama program
def main():
    while True:
        print(" Sistem Administrasi Bimbingan ")
        print("1. Tambah Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")
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
            print("Pilihan tidak valid. Coba lagi.")

# Menjalankan program
main()
