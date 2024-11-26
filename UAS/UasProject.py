# Program sistem peminjaman buku di perpustakaan Cahaya Ilmu
# Daftar buku yang tersedia di perpustakaan
# Variabel nama buku & harga buku dengan daftar list
nama_buku = ["Bahasa Indonesia", "Matematika", "PPKN", "PAI", "Algoritma Pemrograman"] 
harga_buku = [50000, 60000, 55000, 45000, 70000]
buku_tersedia = list(zip(nama_buku, harga_buku)) #list yang berisi tuple
# Dictionary untuk menyimpan data peminjaman
peminjaman = {} #variabel peminjaman dengan dictionary kosong

# fungsi tampilkan buku dengan parameter kosong
def tampilkan_buku():
    """Menampilkan daftar buku yang tersedia di perpustakaan beserta harganya."""
    print("\nDaftar Buku Tersedia:")
    # jika buku tersedia
    if buku_tersedia:
        for buku in buku_tersedia:
            print(f"- {buku[0]} (Harga: Rp {buku[1]})")
    else: #jika tidak ada buku yang tersedia cetak di bawah ini
        print("Tidak ada buku yang tersedia.")

# mendefinisikan fungsi pinjam buku dengan parameter nama anggota dan judul buku
def pinjam_buku(nama_anggota, judul_buku):
    """Memproses peminjaman buku."""
    # Mengubah input menjadi huruf kecil untuk pencocokan
    judul_buku = judul_buku.lower()
    for buku in buku_tersedia: 
        if buku[0].lower() == judul_buku:  # membandingkan dengan lowercase
            if nama_anggota in peminjaman:
                peminjaman[nama_anggota].append(buku)
            else:
                peminjaman[nama_anggota] = [buku]
            buku_tersedia.remove(buku)
            print(f"{nama_anggota} berhasil meminjam '{judul_buku}'.")
            return
    print(f"Buku '{judul_buku}' tidak tersedia.")

# mendefinisikan fungsi kembali buku dengan parameter nama anggota, judul buku, keterlambatan
def kembalikan_buku(nama_anggota, judul_buku, keterlambatan):
    """Memproses pengembalian buku."""
    judul_buku = judul_buku.lower()  # mengubah judul buku menjadi huruf kecil
    for buku in peminjaman[nama_anggota]:
        if buku[0].lower() == judul_buku:  # membandingkan dengan lowercase
            peminjaman[nama_anggota].remove(buku)
            buku_tersedia.append(buku)

            denda = keterlambatan * 1000
            if keterlambatan > 0: 
                print(f"{nama_anggota} mengembalikan buku '{judul_buku}' dengan denda Rp {denda}.")
            else:
                print(f"{nama_anggota} mengembalikan buku '{judul_buku}' tepat waktu. Tidak ada denda.")
            
            # Menghapus nama anggota dari peminjaman jika tidak ada buku lagi
            if not peminjaman[nama_anggota]:
                del peminjaman[nama_anggota]

            return
    print(f"{nama_anggota} tidak meminjam buku '{judul_buku}'.")

def tampilkan_peminjam():
    """Menampilkan daftar peminjam dan buku yang dipinjam."""
    print("\nDaftar Peminjam Buku:")
    if peminjaman:
        for nama_anggota, buku_list in peminjaman.items():
            buku_judul = ', '.join(buku[0] for buku in buku_list)
            print(f"- {nama_anggota} meminjam: {buku_judul}")
    else:
        print("Tidak ada peminjam saat ini.")

def laporkan_buku_hilang(nama_anggota, judul_buku):
    """Memproses laporan buku hilang dan menghitung denda berdasarkan harga buku."""
    judul_buku = judul_buku.lower()  # mengubah judul buku menjadi huruf kecil
    for buku in peminjaman[nama_anggota]:
        if buku[0].lower() == judul_buku:  # membandingkan dengan lowercase
            peminjaman[nama_anggota].remove(buku)
            denda = buku[1]
            print(f"{nama_anggota} melaporkan buku '{judul_buku}' hilang. Denda yang harus dibayar adalah Rp {denda}.")
            # Menghapus nama anggota dari peminjaman jika tidak ada buku lagi
            if not peminjaman[nama_anggota]:
                del peminjaman[nama_anggota]
            return
    print(f"{nama_anggota} tidak meminjam buku '{judul_buku}'.")

# Menu 
def main():
    while True:
        print("\nMenu Peminjaman Buku Di Perpustakaan Cahaya Ilmu:")
        print("1. Tampilkan Buku")
        print("2. Pinjam Buku")
        print("3. Tampilkan Peminjam")  # Pindahkan Tampilkan Peminjam ke menu nomor 3
        print("4. Kembalikan Buku")
        print("5. Laporkan Buku Hilang")
        print("6. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            tampilkan_buku()
        elif pilihan == '2':
            nama = input("Masukkan nama orang yang ingin meminjam buku: ").lower()  # Menambahkan lower() untuk nama
            judul = input("Masukkan judul buku yang ingin dipinjam: ").lower()  # Menambahkan lower() untuk judul buku
            pinjam_buku(nama, judul)
        elif pilihan == '3':  # Tampilkan peminjam berada di sini sekarang
            tampilkan_peminjam()
        elif pilihan == '4':
            nama = input("Masukkan nama orang yang ingin mengembalikan buku: ").lower()
            judul = input("Masukkan judul buku yang ingin dikembalikan: ").lower()
            keterlambatan = int(input("Masukkan jumlah hari keterlambatan: "))
            kembalikan_buku(nama, judul, keterlambatan)
        elif pilihan == '5':
            nama = input("Masukkan nama orang yang ingin melaporkan buku hilang: ").lower()
            judul = input("Masukkan judul buku yang ingin dilaporkan hilang: ").lower()
            laporkan_buku_hilang(nama, judul)
        elif pilihan == '6':
            print("Terima kasih telah menggunakan sistem peminjaman Perpustakaan 'Cahaya Ilmu'.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

main()

