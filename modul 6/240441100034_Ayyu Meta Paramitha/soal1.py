def input_data_karyawan():
    karyawan_list = []
    print("Masukkan data karyawan (minimal 5 karyawan):")
    for i in range(5):
        print(f"\nKaryawan {i+1}")
        nip = input("Masukkan NIP: ")
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        departemen = input("Masukkan Departemen: ")
        jabatan = input("Masukkan Jabatan: ")
        karyawan_list.append({
            'nip': nip,
            'nama': nama,
            'alamat': alamat,
            'departemen': departemen,
            'jabatan': jabatan
        })
    return karyawan_list

def cari_karyawan(karyawan_list, keyword, atribut):
    hasil_pencarian = []
    for karyawan in karyawan_list:
        if keyword.lower() in karyawan[atribut].lower():
            hasil_pencarian.append(karyawan)
    return hasil_pencarian

def tampilkan_hasil(hasil):
    if hasil:
        print("\nHasil pencarian:")
        for karyawan in hasil:
            print(f"NIP: {karyawan['nip']}, Nama: {karyawan['nama']}, Alamat: {karyawan['alamat']}, Departemen: {karyawan['departemen']}, Jabatan: {karyawan['jabatan']}")
    else:
        print("Tidak ada data yang sesuai dengan pencarian.")

def main():
    karyawan_list = input_data_karyawan()

    while True:
        print("\nMenu Pencarian:")
        print("1. Cari berdasarkan NIP")
        print("2. Cari berdasarkan Nama")
        print("3. Cari berdasarkan Alamat")
        print("4. Cari berdasarkan Departemen")
        print("5. Cari berdasarkan Jabatan")
        print("6. Keluar")
        
        pilihan = input("Masukkan pilihan (1-6): ")

        if pilihan == '1':
            keyword = input("Masukkan NIP : ")
            hasil = cari_karyawan(karyawan_list, keyword, 'nip')
        elif pilihan == '2':
            keyword = input("Masukkan Nama : ")
            hasil = cari_karyawan(karyawan_list, keyword, 'nama')
        elif pilihan == '3':
            keyword = input("Masukkan Alamat : ")
            hasil = cari_karyawan(karyawan_list, keyword, 'alamat')
        elif pilihan == '4':
            keyword = input("Masukkan Departemen : ")
            hasil = cari_karyawan(karyawan_list, keyword, 'departemen')
        elif pilihan == '5':
            keyword = input("Masukkan Jabatan : ")
            hasil = cari_karyawan(karyawan_list, keyword, 'jabatan')
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")
            continue
        
        tampilkan_hasil(hasil)

main()
