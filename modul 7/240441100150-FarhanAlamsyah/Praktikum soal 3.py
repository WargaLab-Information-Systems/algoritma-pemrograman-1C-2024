daftar_siswa = []
kapasitas_kelas = 3

def tambah_siswa():
    print("===== Tambah Siswa =====")
    nama = input("Masukkan nama :   ")
    asal = input("Masukkan asal sekolah :   ")
    plotting = input("Masukkan plotting bimbingan intensif  :   ")
    siswa = {'nama': nama, 'kelas': 0, 'asal_sekolah': asal, 'plotting': plotting}
    kelas = (len(daftar_siswa) // kapasitas_kelas) + 1
    siswa['kelas'] = kelas
    daftar_siswa.append(siswa)
    print(f"Siswa berhasil ditambahkan.")

def tampilkan_siswa():
    print("===== Daftar Siswa =====")
    if not daftar_siswa:
        print("Belum ada siswa yang terdaftar.")
        return
    else:
        for i, siswa in enumerate(daftar_siswa):
            print(f">>> Siswa {i + 1} <<<")
            print(f"Nama         : {siswa['nama']}")
            print(f"Kelas        : {siswa['kelas']}")
            print(f"Asal Sekolah : {siswa['asal_sekolah']}")
            print(f"Plotting     : {siswa['plotting']}")

def perbarui_siswa():
    tampilkan_siswa()
    update = input("Masukkan nama siswa yang ingin diperbarui   :   ")
    for siswa in daftar_siswa:
        if siswa['nama'] == update:
            siswa['nama'] = input("Masukkan Nama Siswa Baru: ")
            siswa['asal_sekolah'] = input("Masukkan Asal Sekolah Baru: ")
            siswa['plotting'] = input("Masukkan Plotting Baru: ")
            print("Data siswa berhasil diupdate.")
            return
    print("Input tidak valid!")

def hapus_siswa():
    tampilkan_siswa()
    hapus = input("Masukkan nama siswa yang akan dihapus    :   ")
    for i in range(len(daftar_siswa)):
        if daftar_siswa[i]['nama'] == hapus:
            del daftar_siswa[i]
            print("Data siswa berhasil dihapus.")
            return
    print("Input tidak valid!")
    
def menu():
    while True:
        print("----- Pilih Fitur -----")
        print("[1] Tambah Siswa")
        print("[2] Tampilkan Daftar Siswa")
        print("[3] Perbarui Data Siswa")
        print("[4] Hapus Data Siswa")
        print("[0] Exit")
        print("----------------------")
        pilih_menu = input("Pilihan menu: ")

        if pilih_menu == '1':
            tambah_siswa()
        elif pilih_menu == '2':
            tampilkan_siswa()
        elif pilih_menu == '3':
            perbarui_siswa()
        elif pilih_menu == '4':
            hapus_siswa()
        elif pilih_menu == '0':
            break
        else:
            print("Input tidak valid")

menu()
