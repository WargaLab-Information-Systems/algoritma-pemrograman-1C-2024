data_peminjaman = []
counter_id = 1
# create
def tambah_peminjaman(data_peminjaman, counter_id):
    print("✦ Input Data Peminjaman ✦")
    while True:
        print(f"ID: {counter_id}")
        nama = input("Nama: ")
        judul = input("Judul: ")
        tgl = input("Tanggal: ")

        #save
        peminjaman = (str(counter_id), nama, judul, tgl)
        data_peminjaman.append(peminjaman)
        print("Data Peminjaman berhasil ditambahkan.\n")

        counter_id += 1

        next = input("Apakah Anda ingin menambahkan peminjaman lainnya? (y/n): ")
        if next.lower() != 'y':
            break
    return counter_id

# read
def tampilkan_peminjaman(data_peminjaman):
    if not data_peminjaman:
        print("Data peminjaman tidak ditemukan")
    else:
        print("✦")
        print("✦ Data peminjaman buku ✦")
        for peminjaman in data_peminjaman:
            print(f"ID: {peminjaman[0]}")
            print(f"Nama: {peminjaman[1]}")
            print(f"Judul: {peminjaman[2]}")
            print(f"Tanggal: {peminjaman[3]}")
            print("✦"*15)

# update
def ubah_peminjaman(data_peminjaman):
    id = input("✦ Masukkan ID peminjaman yang ingin diubah: ")
    found = False
    for i in range(len(data_peminjaman)):
        if data_peminjaman[i][0] == id:
            print("⋆ - Tidak perlu mengisi apapun bila tidak ingin mengubah data.")
            nama = input(f"Nama baru (sekarang: '{data_peminjaman[i][1]}'): ") or data_peminjaman[i][1]
            judul = input(f"Judul baru (sekarang: '{data_peminjaman[i][2]}'): ") or data_peminjaman[i][2]
            tgl = input(f"Tanggal baru (sekarang: '{data_peminjaman[i][3]}'): ") or data_peminjaman[i][3]

            data_peminjaman[i] = (id, nama, judul, tgl)
            print("Data peminjaman berhasil diubah.")
            found = True
            break
    if not found:
        print("ID peminjaman tidak ditemukan.")
    
# delete
def hapus_peminjaman(data_peminjaman):
    id = input("✦ Masukkan ID peminjaman yang ingin dihapus: ")
    found = False
    for i in range(len(data_peminjaman)):
        if data_peminjaman[i][0] == id:
            del data_peminjaman[i]
            print("Data peminjaman berhasil dihapus.")
            found = True
            break
    if not found:
        print("ID peminjaman tidak ditemukan.")

# main
def menu():
    counter_id = 1
    while True:
        print("\n ✦✦ Menu Utama ✦✦")
        print("1. Peminjaman")
        print("2. Edit Peminjaman")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            tambah_peminjaman(data_peminjaman, counter_id)
        elif pilihan == '2':
            while True:
                print()
                print("✦ "*13)
                print("1. Tampilkan Peminjaman")
                print("2. Update Peminjaman")
                print("3. Hapus Peminjaman")
                print("4. Kembali ke Menu Utama")
                print("✦ "*13)
                print()

                pilih = input("✦ Masukkan menu yang ingin Anda pilih: ")
                if pilih == '1':
                    tampilkan_peminjaman(data_peminjaman)
                elif pilih == '2':
                    ubah_peminjaman(data_peminjaman)
                elif pilih == '3':
                    hapus_peminjaman(data_peminjaman)
                elif pilih == '4':
                    break
                else :
                    print("Tolong masukkan salah satu dari menu di atas.")
        elif pilihan == '3':
            print(" ⋆ Farewell ...")
            break
        else:
            print("Pilihan anda tidak valid. Silahkan pilih salah satu menu di atas")

menu()