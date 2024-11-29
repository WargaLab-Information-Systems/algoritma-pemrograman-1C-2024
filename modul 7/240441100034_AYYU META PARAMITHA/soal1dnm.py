# Fungsi untuk memproses peminjaman
def pinjam_alat(alat, jenis_alat, jumlah):
    if jenis_alat in alat:
        alat[jenis_alat] += jumlah
    else:
        alat[jenis_alat] = jumlah 
    print(f"{jumlah} {jenis_alat} berhasil dipinjam.\n")

# Fungsi untuk memproses pengembalian
def kembalikan_alat(alat, jenis_alat, jumlah):
    if jenis_alat in alat and alat[jenis_alat] >= jumlah:
        alat[jenis_alat] -= jumlah
        print(f"{jumlah} {jenis_alat} berhasil dikembalikan.\n")
    else:
        print(f"Gagal mengembalikan {jumlah} {jenis_alat}. Tidak cukup jumlahnya.\n")

# Fungsi untuk memproses penukaran alat
def tukar_alat(alat, jenis_alat_dipinjam, jumlah_dipinjam, jenis_alat_ditukar, jumlah_ditukar):
    if jenis_alat_dipinjam in alat and alat[jenis_alat_dipinjam] >= jumlah_dipinjam:
        alat[jenis_alat_dipinjam] -= jumlah_dipinjam
        if jenis_alat_ditukar in alat:
            alat[jenis_alat_ditukar] += jumlah_ditukar
        else:
            alat[jenis_alat_ditukar] = jumlah_ditukar
        print(f"{jumlah_dipinjam} {jenis_alat_dipinjam} berhasil ditukar dengan {jumlah_ditukar} {jenis_alat_ditukar}.\n")
    else:
        print(f"Gagal menukar {jumlah_dipinjam} {jenis_alat_dipinjam}. Tidak cukup jumlahnya.\n")

# Program utama
def main():
    # Dictionary untuk menyimpan jumlah alat kesehatan yang dipinjam
    alat = {}

    while True:
        print("Menu:")
        print("1. Pinjam alat")
        print("2. Kembalikan alat")
        print("3. Tukar alat")
        print("4. Lihat alat yang dipinjam")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            jenis_alat = input("Masukkan jenis alat yang dipinjam: ")
            jumlah = int(input(f"Masukkan jumlah {jenis_alat} yang dipinjam: "))
            pinjam_alat(alat, jenis_alat, jumlah)
        
        elif pilihan == '2':
            jenis_alat = input("Masukkan jenis alat yang dikembalikan: ")
            jumlah = int(input(f"Masukkan jumlah {jenis_alat} yang dikembalikan: "))
            kembalikan_alat(alat, jenis_alat, jumlah)
        
        elif pilihan == '3':
            jenis_alat_dipinjam = input("Masukkan jenis alat yang akan ditukar: ")
            jumlah_dipinjam = int(input(f"Masukkan jumlah {jenis_alat_dipinjam} yang akan ditukar: "))
            jenis_alat_ditukar = input("Masukkan jenis alat yang akan diterima sebagai ganti: ")
            jumlah_ditukar = int(input(f"Masukkan jumlah {jenis_alat_ditukar} yang ditukar: "))
            tukar_alat(alat, jenis_alat_dipinjam, jumlah_dipinjam, jenis_alat_ditukar, jumlah_ditukar)

        elif pilihan == '4':
            print("Alat kesehatan yang dipinjam saat ini:")
            if alat:
                for nama, jumlah in alat.items():
                    print(f"{nama}: {jumlah}")
            else:
                print("Tidak ada alat yang dipinjam.\n")
        
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-5.")

main()

