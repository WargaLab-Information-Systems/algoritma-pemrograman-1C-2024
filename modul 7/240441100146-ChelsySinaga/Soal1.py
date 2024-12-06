def main():
    peminjaman = {}  # Dictionary untuk menyimpan peminjaman alat
    while True:
        print("1. Tambah Peminjaman")
        print("2. Pengembalian")
        print("3. Lihat Peminjaman")
        print("4. Tukar Alat Peminjaman")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1-5): ")
        
        if pilihan == '1':
            tambah_peminjaman(peminjaman)
        
        elif pilihan == '2':
            ubah_peminjaman(peminjaman)
        
        elif pilihan == '3':
            lihat_peminjaman(peminjaman)
        
        elif pilihan == '4':
            tukar_alat(peminjaman)

        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem peminjaman alat!")
            break

        else:
            print("Pilihan tidak valid, silakan pilih opsi yang benar.")

# Fungsi untuk menambah peminjaman alat
def tambah_peminjaman(peminjaman):
    alat = input("Masukkan nama alat yang ingin dipinjam: ")
    jumlah = int(input(f"Masukkan jumlah {alat} yang ingin dipinjam: "))
    if alat in peminjaman:
        peminjaman[alat] += jumlah
    else:
        peminjaman[alat] = jumlah
    print(f"{jumlah} {alat} berhasil dipinjam.")

# Fungsi untuk pengembalian 
def ubah_peminjaman(peminjaman):
    alat = input("Masukkan nama alat yang ingin dikembalikan : ")
    if alat in peminjaman:
        jumlah = int(input(f"Masukkan jumlah {alat} yang dikembalikan atau ditambah (gunakan angka negatif untuk pengembalian): "))
        peminjaman[alat] -= jumlah #menambahkan atau mengurangi jumlah alat dalam dictionary. 
        print(f"{jumlah} {alat} berhasil diubah.")
    else:
        print(f"{alat} belum dipinjam.")

# Fungsi untuk melihat alat yang sedang dipinjam
def lihat_peminjaman(peminjaman):
    if peminjaman:
        print("Alat yang sedang dipinjam saat ini:")
        for alat, jumlah in peminjaman.items():
            print(f"{alat}: {jumlah}")
    else:
        print("Tidak ada alat yang sedang dipinjam.")

# Fungsi untuk menukar alat yang sedang dipinjam dengan alat lain
def tukar_alat(peminjaman):
    alat_lama = input("Masukkan nama alat yang ingin ditukar: ")
    if alat_lama in peminjaman:   #meriksa apa nama alat lama ada dalam daftar alat yg dipinjam peminjam
        jumlah_lama = int(input(f"Masukkan jumlah {alat_lama} yang ingin dikembalikan: "))
        if jumlah_lama <= peminjaman[alat_lama]:
            peminjaman[alat_lama] -= jumlah_lama
            if peminjaman[alat_lama] == 0:
                del peminjaman[alat_lama]
            alat_baru = input("Masukkan nama alat yang ingin dipinjam sebagai pengganti: ")
            jumlah_baru = int(input(f"Masukkan jumlah {alat_baru} yang ingin dipinjam: "))
            if alat_baru in peminjaman:
                peminjaman[alat_baru] += jumlah_baru
            else:
                peminjaman[alat_baru] = jumlah_baru
            print(f"{jumlah_lama} {alat_lama} berhasil dikembalikan dan {jumlah_baru} {alat_baru} berhasil dipinjam sebagai pengganti.")
        else:
            print(f"Jumlah yang dikembalikan melebihi jumlah {alat_lama} yang dipinjam.")
    else:
        print(f"{alat_lama} belum dipinjam.")

# Menjalankan program
if __name__ == "__main__":
    main()  