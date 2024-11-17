# program peminjaman alat untuk penelitian kesehatan
# Membuat dictionary untuk mencatat jumlah alat berdasarkan jenis
alat = {}

# Fungsi tambah alat dengan dua parameter jenis, jumlah dengan type data string
def tambah_alat(jenis, jumlah):
    if jenis in alat:
        alat[jenis] += jumlah
    else:
        alat[jenis] = jumlah

# Fungsi kurangi alat dengan dua parameter jenis, jumlah dengan type data string
def kurangi_alat(jenis, jumlah):
    if jenis in alat:
        alat[jenis] -= jumlah
        if alat[jenis] <= 0:
            del alat[jenis]  # Hapus jika jumlah 0 atau negatif

# Fungsi untuk tukar alat
def tukar_alat(jenis_dikembalikan, jumlah_dikembalikan, jenis_dipinjam, jumlah_dipinjam):
    kurangi_alat(jenis_dikembalikan, jumlah_dikembalikan)
    tambah_alat(jenis_dipinjam, jumlah_dipinjam)

# proses inputan dinamis
def proses_peminjaman():
    while True:
        print("\nMenu:")
        print("1. Tambahkan alat")
        print("2. kembalikan alat")
        print("3. Tukar alat")
        print("4. Lihat alat yang sedang dipinjam")
        print("5. Selesai")
        
        pilihan = input("Pilih opsi (1-5): ")

        # jika variabel pilihan sama dengan 1 jalankan program di bawah ini
        if pilihan == "1":
            # program Tambahkan alat
            jenis = input("Masukkan jenis alat yang dipinjam: ")
            jumlah = int(input(f"Masukkan jumlah {jenis} yang dipinjam: "))
            tambah_alat(jenis, jumlah)

        # jika variabel pilihan tidak dengan 1 apakah variabel pilihan sama dengan 2 jalankan program di bawah ini
        elif pilihan == "2":
            # program kembalikan alat
            jenis = input("Masukkan jenis alat yang dikembalikan: ")
            jumlah = int(input(f"Masukkan jumlah {jenis} yang dikembalikan: "))

            kurangi_alat(jenis, jumlah)
        # jika variabel pilihan tidak dengan 3 apakah variabel pilihan sama dengan 4 jalan kan program di bawah ini
        elif pilihan == "3":
            # program Tukar alat
            jenis_dikembalikan = input("Masukkan jenis alat yang dikembalikan: ")
            jumlah_dikembalikan = int(input(f"Masukkan jumlah {jenis_dikembalikan} yang dikembalikan: "))
            jenis_dipinjam = input("Masukkan jenis alat yang dipinjam: ")
            jumlah_dipinjam = int(input(f"Masukkan jumlah {jenis_dipinjam} yang dipinjam: "))
            tukar_alat(jenis_dikembalikan, jumlah_dikembalikan, jenis_dipinjam, jumlah_dipinjam)
        
        elif pilihan == "4":
            # program melihat alat yang sedang dipinjam
            print("\nAlat yang sedang dipinjam:")
            if alat:
                for jenis, jumlah in alat.items():
                    print(f"- {jenis}: {jumlah} buah alat")
            else:
                print("Tidak ada alat yang sedang dipinjam.")
        
        elif pilihan == "5":
            # Selesai
            print("Proses selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Jalankan program
proses_peminjaman()
