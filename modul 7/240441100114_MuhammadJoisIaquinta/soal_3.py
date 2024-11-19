daftar_siswa = []

def tambah_siswa():
    nama = input("Masukkan Nama Siswa: ")
    asal_sekolah = input("Masukkan Asal Sekolah: ")
    plotting = input("Masukkan Plotting Siswa: ")

    siswa = {"nama": nama,"asal_sekolah": asal_sekolah,"plotting": plotting,"kelas": 0}
    daftar_siswa.append(siswa)
    for i, siswa in enumerate(daftar_siswa):
        siswa['kelas'] = (i // 3) + 1
    print(f"Siswa berhasil ditambahkan ke kelas ke-{'kelas'}.")

def tampilkan_siswa():
    if not daftar_siswa:
        print("Belum ada siswa yang terdaftar.")
        return
    else:
        syarat_tampil = input('Masukkan Jabatan Anda (Hanya untuk staff dan pengajar): ')
        if syarat_tampil in ['staff', 'pengajar']:
            print("=== Daftar Semua Siswa ===")
            for i, siswa in enumerate(daftar_siswa):
                print(f"Data Siswa ke-{i+1}")
                print(f"KELAS KE-{siswa['kelas']}")
                print(f"Nama         : {siswa['nama']}")
                print(f"Asal Sekolah : {siswa['asal_sekolah']}")
                print(f"Plotting     : {siswa['plotting']}")
        else:
            print("Anda tidak berhak melihat daftar siswa.")

def update_siswa():
    if not daftar_siswa:
        print("Belum ada siswa untuk diupdate.")
        return
    else:
        cek_nama = input("Masukkan nama siswa yang ingin diupdate: ")
        for siswa in daftar_siswa:
         if siswa['nama'] == cek_nama:
            print("Data Siswa Sebelumnya:")
            print(f"Nama         : {siswa['nama']}")
            print(f"Asal Sekolah : {siswa['asal_sekolah']}")
            print(f"Plotting     : {siswa['plotting']}")
            print(f"Kelas        : {siswa['kelas']}")

            siswa['nama'] = input("Masukkan Nama Siswa Baru: ")
            siswa['asal_sekolah'] = input("Masukkan Asal Sekolah Baru: ")
            siswa['plotting'] = input("Masukkan Plotting Baru: ")
            print("Data siswa berhasil diupdate.")
            for i, siswa in enumerate(daftar_siswa):
                siswa['kelas'] = (i // 3) + 1

            return
        print("Siswa tidak ditemukan.")

def hapus_siswa():
    if not daftar_siswa:
        print("Belum ada siswa yang terdaftar.")
        return
    else:
        cek_nama = input("Masukkan nama siswa yang ingin dihapus: ")
        for i, siswa in enumerate(daftar_siswa):
            if siswa['nama'] == cek_nama:
                del daftar_siswa[i]
                print("Data siswa berhasil dihapus.")
                for j, siswa in enumerate(daftar_siswa):
                    siswa['kelas'] = (j // 3) + 1
                return
        print("Siswa tidak ditemukan.")

def main():
    while True:
        print("\n=== Lembaga Bimbingan Intensif Gema Ripah ===")
        print("1. Tambah Daftar Siswa")
        print("2. Tampilkan Daftar Siswa")
        print("3. Update Daftar Siswa")
        print("4. Hapus Daftar Siswa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            tambah_siswa()
        elif pilihan == '2':
            tampilkan_siswa()
        elif pilihan == '3':
            update_siswa()
        elif pilihan == '4':
            hapus_siswa()
        elif pilihan == '5':
            print("Program Selesai.")
            break
        else:
            print("Masukkan input yang benar!")

main()
