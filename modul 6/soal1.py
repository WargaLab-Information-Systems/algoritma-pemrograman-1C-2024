data_karyawan = []
nip_list = []
def tambah_karyawan():
    for i in range(5):
        print(f"\nInput data karyawan ke-{i + 1}")
        while True:
            nip = input("Masukkan NIP: ")
            if nip.strip() == "":
                print("NIP tidak boleh kosong! Silakan masukkan NIP.")
            else:
                try:
                    nip = int(nip)
                    if nip in nip_list:
                        print("NIP sudah terdaftar. Harap masukkan NIP yang berbeda.")
                    else:
                        nip_list.append(nip)
                        break
                except ValueError:
                    print("NIP harus berupa angka! Silakan coba lagi.")

        while True:
            nama = input("Masukkan Nama: ")
            if nama.strip() == "":
                print("Nama tidak boleh kosong! Silakan masukkan nama.")
            else:
                break
        
        while True:
            alamat = input("Masukkan Alamat: ")
            if alamat.strip() == "":
                print("Alamat tidak boleh kosong! Silakan masukkan alamat.")
            else:
                break
        
        while True:
            departemen = input("Masukkan Departemen: ")
            if departemen.strip() == "":
                print("Departemen tidak boleh kosong! Silakan masukkan departemen.")
            else:
                break
        
        while True:
            jabatan = input("Masukkan Jabatan: ")
            if jabatan.strip() == "":
                print("Jabatan tidak boleh kosong! Silakan masukkan jabatan.")
            else:
                break

        karyawan = (nip, nama, alamat, departemen, jabatan)
        data_karyawan.append(karyawan)
        print("Data karyawan berhasil ditambahkan.")

def tampilkan_karyawan():
    if not data_karyawan:
        print("Belum ada data karyawan.")
    else:
        print("\nDaftar Karyawan:")
        for karyawan in data_karyawan:
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")

def cari_karyawan():
    print("\nPencarian Data Karyawan")
    print("Atribut pencarian: nip, nama, alamat, departemen, jabatan")
    
    while True:
        atribut = input("Masukkan atribut yang dicari: ").lower()
        if atribut in ["nip", "nama", "alamat", "departemen", "jabatan"]:
            break
        else:
            print("Atribut tidak valid. Harap masukkan atribut yang sesuai!!!")
    
    kata_kunci = input("Masukkan nilai untuk pencarian: ")
    
    hasil_cari = []

    if atribut == "nip":
        try:
            kata_kunci = int(kata_kunci)
        except ValueError:
            print("NIP yang dicari harus berupa angka.")
            return []
    
    for karyawan in data_karyawan:
        if (atribut == "nip" and karyawan[0] == kata_kunci) or \
           (atribut == "nama" and karyawan[1].lower() == kata_kunci.lower()) or \
           (atribut == "alamat" and karyawan[2].lower() == kata_kunci.lower()) or \
           (atribut == "departemen" and karyawan[3].lower() == kata_kunci.lower()) or \
           (atribut == "jabatan" and karyawan[4].lower() == kata_kunci.lower()):
            hasil_cari.append(karyawan)
    
    if hasil_cari:
        print("\nHasil Pencarian:")
        for karyawan in hasil_cari:
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
    else:
        print("Data karyawan tidak ditemukan dengan kriteria tersebut.")

def main():
    while True:
        print("\n### Data Perusahaan Sarifa ###")
        print("1. Tambah Data Karyawan")
        print("2. Tampilkan Semua Karyawan")
        print("3. Cari Karyawan Berdasarkan Atribut")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            tambah_karyawan()

        elif pilihan == "2":
            tampilkan_karyawan()
        
        elif pilihan == "3":
            cari_karyawan()
        
        elif pilihan == "4":
            print("Sampai Jumpa Lagi!!!")
            break
        
        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.")

main()

