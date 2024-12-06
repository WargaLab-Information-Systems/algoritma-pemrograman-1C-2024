karyawan = []

def tambah_karyawan():
    print(f"=== Masukkan data karyawan ===")
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")
    print("-----------------------------")

    karyawan.append({'NIP': nip, 'Nama': nama, 'Alamat': alamat, 'Departemen': departemen, 'Jabatan': jabatan})

def cari_karyawan(cari):
    hasil = []
    for karyawan_data in karyawan:
        if cari in karyawan_data.values():
            hasil.append(karyawan_data)
    return hasil

    

while True:
    tambah_lagi = input("Apakah ingin menambah data? ya/tidak :")
    if tambah_lagi == 'ya':
        tambah_karyawan()
    else:
        cari = input("Masukkan kata kunci pencarian (atau kosong untuk keluar): ")
        if not cari:
            break
        hasil_pencarian = cari_karyawan(cari)
        if hasil_pencarian:
            for data in hasil_pencarian:
                print(data)
            break
        else:
            print("Data tidak ditemukan.")