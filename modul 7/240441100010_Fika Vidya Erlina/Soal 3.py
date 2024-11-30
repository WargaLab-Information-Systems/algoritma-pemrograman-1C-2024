# Struktur data untuk menyimpan kelas dan siswa
kelas_list = []  # Menyimpan kelas-kelas yang ada
kelas_counter = 1  # Nomor kelas yang akan digunakan

# Fungsi untuk menambah siswa ke kelas yang tepat
def tambah_siswa_ke_kelas(nama, asal_sekolah):
    global kelas_counter
    siswa = {'nama': nama, 'asal_sekolah': asal_sekolah}

    # Cek apakah ada kelas yang memiliki ruang
    for kelas in kelas_list:
        if len(kelas['siswa']) < 3:
            kelas['siswa'].append(siswa)
            print(f"Siswa {nama} berhasil ditambahkan ke Kelas {kelas['nomor_kelas']}.")
            return

    # Jika semua kelas penuh, buat kelas baru
    kelas_baru = {
        'nomor_kelas': kelas_counter,
        'siswa': [siswa]
    }
    kelas_list.append(kelas_baru)
    kelas_counter += 1
    print(f"Siswa {nama} berhasil ditambahkan ke Kelas {kelas_baru['nomor_kelas']}.")

# Fungsi untuk menampilkan semua kelas dan siswa
def tampilkan_semua_kelas():
    if not kelas_list:
        print("Tidak ada kelas yang terdaftar.")
        return

    for kelas in kelas_list:
        print(f"\nDaftar Siswa Kelas {kelas['nomor_kelas']}:")
        if not kelas['siswa']:
            print("Belum ada siswa di kelas ini.")
        for siswa in kelas['siswa']:
            print(f"Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")

# Fungsi untuk menghapus siswa berdasarkan nama
def hapus_siswa(nama):
    for kelas in kelas_list:
        for siswa in kelas['siswa']:
            if siswa['nama'].lower() == nama.lower():
                kelas['siswa'].remove(siswa)
                print(f"Siswa {nama} berhasil dihapus dari Kelas {kelas['nomor_kelas']}.")
                return
    print(f"Siswa dengan nama {nama} tidak ditemukan.")

# Fungsi untuk memperbarui data siswa
def update_siswa(nama_lama, nama_baru, asal_sekolah_baru):
    for kelas in kelas_list:
        for siswa in kelas['siswa']:
            if siswa['nama'].lower() == nama_lama.lower():
                siswa['nama'] = nama_baru
                siswa['asal_sekolah'] = asal_sekolah_baru
                print(f"Data siswa {nama_lama} berhasil diperbarui.")
                return
    print(f"Siswa dengan nama {nama_lama} tidak ditemukan.")

# Fungsi utama untuk menampilkan menu dan menangani input pengguna
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Tambah Siswa")
        print("2. Tampilkan Semua Kelas")
        print("3. Hapus Siswa")
        print("4. Update Data Siswa")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah siswa: ")
            tambah_siswa_ke_kelas(nama, asal_sekolah)

        elif pilihan == '2':
            tampilkan_semua_kelas()

        elif pilihan == '3':
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            hapus_siswa(nama)

        elif pilihan == '4':
            nama_lama = input("Masukkan nama siswa yang ingin diperbarui: ")
            nama_baru = input("Masukkan nama baru siswa: ")
            asal_sekolah_baru = input("Masukkan asal sekolah baru siswa: ")
            update_siswa(nama_lama, nama_baru, asal_sekolah_baru)

        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Menjalankan program
menu()
