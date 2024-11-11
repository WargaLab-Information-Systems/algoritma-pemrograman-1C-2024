buku = []

def create():
    id_peminjaman = input("Masukkan ID Peminjaman: ")
    nama_peminjam = input("Masukkan Nama Peminjam: ")
    judul_buku = input("Masukkan Judul Buku: ")
    tanggal_peminjaman = input("Masukkan Tanggal Peminjaman: ")
    
    buku.append({
        "id_peminjaman": id_peminjaman,
        "nama_peminjam": nama_peminjam,
        "judul_buku": judul_buku,
        "tanggal_peminjaman": tanggal_peminjaman
    })
    print("Data berhasil ditambahkan.")

def read():
    if not buku:
        print("Belum ada data.")
        return
    
    print("Daftar Peminjaman Buku:")
    for i, data in enumerate(buku):
        print(f"{i+1}. ID Peminjaman: {data['id_peminjaman']}, Nama Peminjam: {data['nama_peminjam']}, Judul Buku: {data['judul_buku']}, Tanggal Peminjaman: {data['tanggal_peminjaman']}")

def update():
    read()
    index_update = int(input("Masukkan nomor data yang ingin diubah: ")) - 1 
    
    if 0 <= index_update < len(buku):
        buku[index_update]["id_peminjaman"] = input("Masukkan ID Peminjaman baru: ")
        buku[index_update]["nama_peminjam"] = input("Masukkan Nama Peminjam baru: ")
        buku[index_update]["judul_buku"] = input("Masukkan Judul Buku baru: ")
        buku[index_update]["tanggal_peminjaman"] = input("Masukkan Tanggal Peminjaman baru: ")
        print("Data berhasil diubah.")
    else:
        print("Nomor data tidak valid.")

def delete():
    read()
    index_delete = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
    
    if 0 <= index_delete < len(buku):
        del buku[index_delete]
        print("Data berhasil dihapus.")
    else:
        print("Nomor data tidak valid.")

def menu():
    while True:
        print("=== Pilih Fitur ===")
        print("[1] Create")
        print("[2] Read")
        print("[3] Update")
        print("[4] Delete")
        print("[0] Exit")
        print("----------------------")
        pilih_menu = input("Pilihan menu: ")

        if pilih_menu == '1':
            create()
        elif pilih_menu == '2':
            read()
        elif pilih_menu == '3':
            update()
        elif pilih_menu == '4':
            delete()
        elif pilih_menu == '0':
            break
        else:
            print("Input tidak valid")

menu()