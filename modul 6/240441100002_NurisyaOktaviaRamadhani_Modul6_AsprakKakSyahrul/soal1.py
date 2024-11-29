def tambah_karyawan(data_karyawan):
    atribut_list = ["NIP", "Nama", "Alamat", "Departemen", "Jabatan"]
    karyawan_data = []
    for atribut in atribut_list:
        while True:
            data = input(f"Masukkan {atribut}: ")
            if data:
                karyawan_data.append(data)
                break
            else:
                print(f"{atribut} tidak boleh kosong. Silakan coba lagi.")
    karyawan = tuple(karyawan_data)
    data_karyawan.append(karyawan)
def tampilkan_karyawan(data_karyawan):
    print("\nDaftar Karyawan:")
    for karyawan in data_karyawan:
        print(" NIP       : {}".format(karyawan[0]))
        print(" Nama      : {}".format(karyawan[1]))
        print(" Alamat    : {}".format(karyawan[2]))
        print(" Departemen: {}".format(karyawan[3]))
        print(" Jabatan   : {}".format(karyawan[4]))
        print("-" * 20)
def cari_karyawan(data_karyawan, atribut, nilai):
    atribut_list = ('NIP', 'Nama', 'Alamat', 'Departemen', 'Jabatan')
    if atribut in atribut_list:
        atribut_index = atribut_list.index(atribut)
    else:
        print("Atribut pencarian tidak valid.")
        return
    hasil_pencarian = [karyawan for karyawan in data_karyawan if karyawan[atribut_index] == nilai]
    if hasil_pencarian:
        print("\nHasil Pencarian:")
        for karyawan in hasil_pencarian:
            print(" NIP       : {}".format(karyawan[0]))
            print(" Nama      : {}".format(karyawan[1]))
            print(" Alamat    : {}".format(karyawan[2]))
            print(" Departemen: {}".format(karyawan[3]))
            print(" Jabatan   : {}".format(karyawan[4]))
            print("-" * 20)
    else:
        print("\nTidak ada karyawan yang sesuai dengan pencarian.")
data_karyawan = []
jumlah_karyawan = int(input("Masukkan jumlah karyawan yang ingin diinput: "))
print("\nInput Data Karyawan")
for i in range(jumlah_karyawan):
    print("\nData Karyawan {}".format(i + 1))
    tambah_karyawan(data_karyawan)
tampilkan_karyawan(data_karyawan)
while True:
    print("\nPencarian Karyawan")
    print("1. Cari berdasarkan NIP")
    print("2. Cari berdasarkan Nama")
    print("3. Cari berdasarkan Alamat")
    print("4. Cari berdasarkan Departemen")
    print("5. Cari berdasarkan Jabatan")
    print("6. Keluar")
    pilihan = input("Pilih opsi pencarian (1-6): ")
    if pilihan == "1":
        nilai = input("Masukkan NIP: ")
        cari_karyawan(data_karyawan, 'NIP', nilai)
    elif pilihan == "2":
        nilai = input("Masukkan Nama: ")
        cari_karyawan(data_karyawan, 'Nama', nilai)
    elif pilihan == "3":
        nilai = input("Masukkan Alamat: ")
        cari_karyawan(data_karyawan, 'Alamat', nilai)
    elif pilihan == "4":
        nilai = input("Masukkan Departemen: ")
        cari_karyawan(data_karyawan, 'Departemen', nilai)
    elif pilihan == "5":
        nilai = input("Masukkan Jabatan: ")
        cari_karyawan(data_karyawan, 'Jabatan', nilai)
    elif pilihan == "6":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")