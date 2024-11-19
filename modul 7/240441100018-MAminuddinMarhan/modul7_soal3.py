data_kelas = []
def tambah_siswa(nama, kelas, asal_sekolah):
    for k in data_kelas:
        if k['kelas'] == kelas:
            if len(k['siswa']) < 3:
                k['siswa'].append({'nama': nama, 'asal_sekolah': asal_sekolah})
                print(f"Siswa {nama} berhasil ditambahkan ke kelas {kelas}.")
                return
            else:
                print(f"Kelas {kelas} sudah penuh. Membuka kelas baru.")
                break
    data_kelas.append({'kelas': kelas, 'siswa': [{'nama': nama, 'asal_sekolah': asal_sekolah}]})
    print(f"Kelas {kelas} dibuat dan siswa {nama} ditambahkan.")
def tampilkan_siswa():
    if not data_kelas:
        print("Belum ada kelas yang dibuat.")
        return
    for k in data_kelas:
        print(f"\nKelas: {k['kelas']}")
        for siswa in k['siswa']:
            print(f"Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")
def update_siswa(nama_lama, nama_baru, kelas, asal_sekolah):
    for k in data_kelas:
        if k['kelas'] == kelas:
            for siswa in k['siswa']:
                if siswa['nama'] == nama_lama:
                    siswa['nama'] = nama_baru
                    siswa['asal_sekolah'] = asal_sekolah
                    print(f"Data siswa {nama_lama} berhasil diupdate menjadi {nama_baru}.")
                    return
    print(f"Siswa dengan nama {nama_lama} tidak ditemukan di kelas {kelas}.")
def hapus_siswa(nama, kelas):
    for k in data_kelas:
        if k['kelas'] == kelas:
            for siswa in k['siswa']:
                if siswa['nama'] == nama:
                    k['siswa'].remove(siswa)
                    print(f"Siswa {nama} berhasil dihapus dari kelas {kelas}.")
                    return
    print(f"Siswa dengan nama {nama} tidak ditemukan di kelas {kelas}.")
while True:
    print("\nMenu:")
    print("1. Tambah Siswa")
    print("2. Tampilkan Siswa")
    print("3. Update Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == '1':
        nama = input("Masukkan nama siswa: ")
        kelas = input("Masukkan kelas: ")
        asal_sekolah = input("Masukkan asal sekolah: ")
        tambah_siswa(nama, kelas, asal_sekolah)
    elif pilihan == '2':
        tampilkan_siswa()
    elif pilihan == '3':
        nama_lama = input("Masukkan nama siswa yang ingin diupdate: ")
        nama_baru = input("Masukkan nama baru: ")
        kelas = input("Masukkan kelas: ")
        asal_sekolah = input("Masukkan asal sekolah baru: ")
        update_siswa(nama_lama, nama_baru, kelas, asal_sekolah)
    elif pilihan == '4':
        nama = input("Masukkan nama siswa yang ingin dihapus: ")
        kelas = input("Masukkan kelas: ")
        hapus_siswa(nama, kelas)
    elif pilihan == '5':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")