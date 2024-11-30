def input_data_karyawan():
    karyawan_list = []
    for i in range(5):
        print(f"\nInput data karyawan {i+1}:")

        while True:
            nip = input("NIP: ")
            if not nip.isdigit():
                print("NIP tidak boleh kosong, dan harus berupa angka. Silakan isi kembali.")
                continue
            break
        while True:
            nama = input("Nama: ")
            if not nama.isalpha():
                print("Nama tidak boleh kosong, tidak boleh berupa angka. Silakan isi kembali.")
                continue
            break
        while True:
            alamat = input("Alamat: ")
            if not alamat.isalpha():
                print("Alamat tidak boleh kosong, tidak boleh berupa angka. Silakan isi kembali.")
                continue
            break
        while True:
            departemen = input("Departemen: ")
            if not departemen.isalpha():
                print("Departemen tidak boleh kosong, tidak boleh berupa angka. Silakan isi kembali.")
                continue
            break
        while True:
            jabatan = input("Jabatan: ")
            if not jabatan.isalpha():
                print("Jabatan tidak boleh kosong, tidak boleh berupa angka. Silakan isi kembali.")
                continue
            break

        karyawan_list.append({
            'nip': nip,
            'nama': nama,
            'alamat': alamat,
            'departemen': departemen,
            'jabatan': jabatan
        })
    return karyawan_list

def cari_karyawan(karyawan_list, pencarian):
    hasil_pencarian = []
    for karyawan in karyawan_list:
        if pencarian in karyawan['nip'] or \
           pencarian in karyawan['nama'] or \
           pencarian in karyawan['alamat'] or \
           pencarian in karyawan['departemen'] or \
           pencarian in karyawan['jabatan']:
            hasil_pencarian.append(karyawan)
    
    return hasil_pencarian

def main():
    print("Selamat datang di program data karyawan.")
    karyawan_list = input_data_karyawan()
    

    while True:
        print("\n--- Menu Pencarian ---")
        print("1. Pencarian Berdasarkan NIP, Nama, Alamat, Departemen, atau Jabatan")
        print("2. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '2':
            print("Terima kasih telah menggunakan program ini.")
            break

        pencarian = input("Masukkan kata kunci pencarian: ")
        hasil = cari_karyawan(karyawan_list, pencarian)

        if hasil:
            print("\nHasil Pencarian:")
            for karyawan in hasil:
                print(f"NIP: {karyawan['nip']}, Nama: {karyawan['nama']}, Alamat: {karyawan['alamat']}, Departemen: {karyawan['departemen']}, Jabatan: {karyawan['jabatan']}")
        else:
            print("Data tidak ditemukan.")

if __name__ == "__main__":
    main()

