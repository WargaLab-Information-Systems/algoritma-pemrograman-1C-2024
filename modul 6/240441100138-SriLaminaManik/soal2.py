def main():
    peminjaman_list = []

    while True:
        print("1. Tambah")
        print("2. Tampilkan")
        print("3. Update")
        print("4. Hapus")
        print("5. Keluar")
        pilihan = input("Pilih menunya (1-5): ")

        if pilihan == '1':  #menambah data
            peminjaman_list.append((
                input("ID Peminjaman: "),
                input("Nama Peminjam: "),
                input("Judul Buku: "),
                input("Tanggal Peminjaman: ")
            ))
            print("Peminjaman ditambahkan.")
        
        elif pilihan == '2':  #Tampilkan data
            if not peminjaman_list:
                print("Tidak ada data.")
            else:
                print("\nDaftar Peminjaman:")
                for p in peminjaman_list:
                    print(f"ID: {p[0]}, Nama: {p[1]}, Judul: {p[2]}, Tanggal: {p[3]}")
        
        elif pilihan == '3': #Update
            id_peminjaman = input("ID untuk diupdate: ")
            for i in range(len(peminjaman_list)):
                if peminjaman_list[i][0] == id_peminjaman:
                    peminjaman_list[i] = (
                        id_peminjaman,
                        input("Nama baru: "),
                        input("Judul baru: "),
                        input("Tanggal baru: ")
                    )
                    print("Peminjaman diupdate.")
                    break
            else:
                print("ID tidak ditemukan.")
        
        elif pilihan == '4':  #Hapus
            id_peminjaman = input("ID untuk dihapus: ")
            for i in range(len(peminjaman_list)):
                if peminjaman_list[i][0] == id_peminjaman:
                    peminjaman_list.pop(i)
                    print("Peminjaman dihapus.")
                    break
            else:
                print("ID tidak ditemukan.")
        
        elif pilihan == '5':  #Keluar
            print("Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid.")

main() #memanggil seluruh program 