# Dictionary untuk menyimpan barang yang dipinjam beserta jumlahnya
barang_dipinjam = {}  

# Set untuk mencatat semua barang yang pernah dipinjam (tanpa duplikasi)
barang_tercatat = set()  

# Fungsi untuk menampilkan total barang yang dipinjam
def tampilkan_total():
    print("\nTotal barang yang masih dipinjam:")
    if len(barang_dipinjam) == 0:  # Jika dictionary kosong
        print("- Tidak ada barang yang dipinjam.")
    else:
        # Menampilkan barang dan jumlahnya dari dictionary
        for barang, jumlah in barang_dipinjam.items():
            if jumlah > 0:  # Hanya menampilkan barang dengan jumlah > 0
                print(f"- {barang}: {jumlah}")
    
    # Menampilkan semua barang yang pernah dipinjam dari set
    print("\nDaftar semua barang yang pernah dipinjam:")
    if len(barang_tercatat) == 0:  # Jika set kosong
        print("- Tidak ada barang yang tercatat.")
    else:
        print(", ".join(barang_tercatat))  # Menggabungkan barang dalam set menjadi string
    print()

# Fungsi untuk memasukkan jumlah barang dengan validasi
def input_jumlah_barang():
    while True:
        jumlah = input("Masukkan jumlah barang: ")
        # Validasi input apakah berupa angka
        if jumlah != "" and all(c in "0123456789" for c in jumlah):
            jumlah = int(jumlah)  # Mengubah input menjadi integer
            if jumlah > 0:  # Memastikan jumlah lebih besar dari 0
                return jumlah
            else:
                print("Jumlah harus lebih besar dari 0. Coba lagi.")
        else:
            print("Input tidak valid. Masukkan angka positif.")

# Fungsi untuk memasukkan nama barang dengan validasi
def input_nama_barang():
    while True:
        nama_barang = input("Masukkan nama barang: ")
        if nama_barang != "":  # Memastikan input tidak kosong
            return nama_barang  # Mengembalikan nama barang yang valid
        else:
            print("Nama barang tidak boleh kosong. Coba lagi.")

# Fungsi untuk melanjutkan ke hari berikutnya dengan validasi
def input_lanjut():
    while True:
        lanjut = input("Apakah Anda ingin melanjutkan ke hari berikutnya? ya/tidak: ")
        if lanjut in {"ya", "tidak"}:  # Validasi input hanya menerima "ya" atau "tidak"
            return lanjut
        else:
            print("Input tidak valid. Harap ketik 'ya' atau 'tidak'.")

# Fungsi untuk proses peminjaman barang
def peminjaman_barang():
    hari = 1  # Menghitung hari peminjaman
    while True:
        print(f"\nHari ke-{hari}: Peminjaman Barang")
        while True:
            nama_barang = input_nama_barang()
            if nama_barang == "end":  # Jika pengguna mengetik "end", keluar dari loop
                break

            jumlah = input_jumlah_barang()  # Meminta input jumlah barang
            if nama_barang in barang_dipinjam:
                barang_dipinjam[nama_barang] += jumlah  # Menambahkan jumlah jika barang sudah ada
            else:
                barang_dipinjam[nama_barang] = jumlah  # Menambahkan barang baru ke dictionary
            
            # Menambahkan barang ke set
            barang_tercatat.add(nama_barang)  

            print(f"{jumlah} {nama_barang} berhasil dipinjam.")
            tampilkan_total()  # Menampilkan total barang yang dipinjam
        
        lanjut = input_lanjut()  # Menanyakan apakah ingin lanjut ke hari berikutnya
        if lanjut == "tidak":
            break
        hari += 1

# Fungsi untuk proses pengembalian barang
def pengembalian_barang():
    print("\nPengembalian Barang")
    while True:
        nama_barang = input_nama_barang()
        if nama_barang == "end":  # Jika pengguna mengetik "end", keluar dari loop
            break

        jumlah = input_jumlah_barang()  # Meminta input jumlah barang
        if nama_barang in barang_dipinjam:
            if barang_dipinjam[nama_barang] >= jumlah:  # Validasi apakah jumlah cukup untuk dikembalikan
                barang_dipinjam[nama_barang] -= jumlah  # Mengurangi jumlah barang
                print(f"{jumlah} {nama_barang} berhasil dikembalikan.")
            else:
                print(f"Jumlah pengembalian melebihi jumlah barang yang dipinjam.")
        else:
            print(f"{nama_barang} tidak ditemukan dalam daftar peminjaman.")
        tampilkan_total()  # Menampilkan total barang yang dipinjam

# Fungsi untuk proses penukaran barang
def penukaran_barang():
    print("\nPenukaran Barang")
    while True:
        nama_barang = input_nama_barang()
        if nama_barang == "end":  # Jika pengguna mengetik "end", keluar dari loop
            break

        if nama_barang in barang_dipinjam:
            print(f"Anda telah meminjam {barang_dipinjam[nama_barang]} {nama_barang}.")
            jumlah_pengembalian = input_jumlah_barang()  # Meminta jumlah barang yang akan dikembalikan
            
            if jumlah_pengembalian <= barang_dipinjam[nama_barang]:
                barang_dipinjam[nama_barang] -= jumlah_pengembalian  # Mengurangi jumlah barang
                print(f"{jumlah_pengembalian} {nama_barang} berhasil dikembalikan.")
                
                nama_barang_baru = input_nama_barang()  # Meminta nama barang baru
                jumlah_baru = input_jumlah_barang()  # Meminta jumlah barang baru

                if nama_barang_baru in barang_dipinjam:
                    barang_dipinjam[nama_barang_baru] += jumlah_baru  # Menambahkan jumlah jika barang sudah ada
                else:
                    barang_dipinjam[nama_barang_baru] = jumlah_baru  # Menambahkan barang baru ke dictionary
                
                # Menambahkan barang baru ke set
                barang_tercatat.add(nama_barang_baru)

                print(f"{jumlah_baru} {nama_barang_baru} berhasil dipinjam sebagai penukaran.")
            else:
                print(f"Jumlah pengembalian melebihi jumlah barang yang dipinjam.")
        else:
            print(f"{nama_barang} tidak ditemukan dalam daftar peminjaman.")
        tampilkan_total()  # Menampilkan total barang yang dipinjam

# Program utama
print("Program Peminjaman, Pengembalian, dan Penukaran Barang")
peminjaman_barang()  # Memulai proses peminjaman barang
pengembalian_barang()  # Memulai proses pengembalian barang
penukaran_barang()  # Memulai proses penukaran barang

# Menampilkan data akhir setelah semua proses selesai
print("\nData Akhir Peminjaman:")
tampilkan_total()