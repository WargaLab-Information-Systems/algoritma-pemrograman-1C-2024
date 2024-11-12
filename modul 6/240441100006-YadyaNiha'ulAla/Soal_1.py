def input_data_karyawan(daftar_karyawan):
    print("->> Input Data Karyawan <<-")
    while True:
        nip = input("NIP: ")
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")

        #save
        karyawan = (nip, nama, alamat, departemen, jabatan)

        daftar_karyawan.append(karyawan)

        print("Data karyawan berhasil ditambahkan.\n")

        next = input("Apakah Anda ingin menambahkan data lagi? (y/n): ")
        if next.lower() != 'y':
            break
    return daftar_karyawan

def tampilkan_data_karyawan(karyawan):
    print(f"NIP: {karyawan[0]}")
    print(f"Nama: {karyawan[1]}")
    print(f"Alamat: {karyawan[2]}")
    print(f"Departemen: {karyawan[3]}")
    print(f"Jabatan: {karyawan[4]}")
    print("-"*25)

def cari(daftar_karyawan):
    print("->> Pencarian Data Karyawan <<-")
    keyword = input("Masukkan kata kunci pencarian: ") 
    hasil_pencarian = []

    for karyawan in daftar_karyawan:
        if (
            keyword.lower() in karyawan[0].lower() or
            keyword.lower() in karyawan[1].lower() or
            keyword.lower() in karyawan[2].lower() or
            keyword.lower() in karyawan[3].lower() or
            keyword.lower() in karyawan[4].lower()
            ):
            hasil_pencarian.append(karyawan)
    if hasil_pencarian:
        print("\n ->> Hasil Pencarian: ")
        for karyawan in hasil_pencarian:
            tampilkan_data_karyawan(karyawan)
    else:
        print("Maaf, tidak ada data karyawan yang sesuai.")

def main():
    daftar_karyawan = []
    while True:
        print("\n ->> Menu Utama <<-")
        print("1. Input Data Karyawan")
        print("2. pencarian Data Karyawan")
        print("3. Keluar")
        print()

        pilihan = input("-> Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            input_data_karyawan(daftar_karyawan)
        elif pilihan == '2':
            cari(daftar_karyawan)
        elif pilihan == '3':
            print("Bye!")
            break
        else:
            print("Pilihan anda tidak valid. Silahkan pilih salah satu menu di atas")

main()