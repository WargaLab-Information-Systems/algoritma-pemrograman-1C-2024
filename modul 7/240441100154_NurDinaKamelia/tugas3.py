# Dictionary untuk menyimpan data kelas
kelas = {}

# Fungsi untuk menambahkan siswa ke kelas
def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    asal_sekolah = input("Masukkan asal sekolah: ")

    # Cari kelas dengan slot kurang dari 3 atau buat kelas baru
    kelas_tersedia = None
    for key, siswa in kelas.items():
        if len(siswa) < 3:
            kelas_tersedia = key
            break

    if kelas_tersedia is None:
        kelas_baru = f"Kelas-{len(kelas) + 1}"
        kelas[kelas_baru] = []
        kelas_tersedia = kelas_baru

    # Tambahkan siswa ke kelas
    kelas[kelas_tersedia].append({"nama": nama, "asal_sekolah": asal_sekolah})
    print(f"Siswa {nama} dari {asal_sekolah} telah ditambahkan ke {kelas_tersedia}.")

# Fungsi untuk menampilkan data kelas
def lihat_kelas():
    for key, siswa in kelas.items():
        print(f"\n{key}:")
        for i, data in enumerate(siswa, 1):
            print(f"  {i}. {data['nama']} (Asal Sekolah: {data['asal_sekolah']})")

# Fungsi untuk memperbarui data siswa
def perbarui_siswa():
    lihat_kelas()
    kelas_pilih = input("Pilih kelas untuk memperbarui data (mis. Kelas-1): ")
    if kelas_pilih in kelas:
        lihat_kelas()
        indeks = int(input("Masukkan nomor siswa yang akan diperbarui: ")) - 1
        if 0 <= indeks < len(kelas[kelas_pilih]):
            nama_baru = input("Masukkan nama baru: ")
            asal_baru = input("Masukkan asal sekolah baru: ")
            kelas[kelas_pilih][indeks] = {"nama": nama_baru, "asal_sekolah": asal_baru}
            print("Data siswa berhasil diperbarui.")
        else:
            print("Indeks siswa tidak valid.")
    else:
        print("Kelas tidak ditemukan.")

# Fungsi untuk menghapus data siswa
def hapus_siswa():
    lihat_kelas()
    kelas_pilih = input("Pilih kelas untuk menghapus data (mis. Kelas-1): ")
    if kelas_pilih in kelas:
        indeks = int(input("Masukkan nomor siswa yang akan dihapus: ")) - 1
        if 0 <= indeks < len(kelas[kelas_pilih]):
            siswa_dihapus = kelas[kelas_pilih].pop(indeks)
            print(f"Siswa {siswa_dihapus['nama']} berhasil dihapus.")
            if not kelas[kelas_pilih]:  # Hapus kelas jika kosong
                del kelas[kelas_pilih]
                print(f"{kelas_pilih} telah dihapus karena kosong.")
        else:
            print("Indeks siswa tidak valid.")
    else:
        print("Kelas tidak ditemukan.")

# Program utama
while True:
    print("\nMenu:")
    print("1. Tambah siswa")
    print("2. Lihat kelas")
    print("3. Perbarui data siswa")
    print("4. Hapus data siswa")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        lihat_kelas()
    elif pilihan == "3":
        perbarui_siswa()
    elif pilihan == "4":
        hapus_siswa()
    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")