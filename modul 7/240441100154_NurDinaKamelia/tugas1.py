# dictionary alat kesehatan dengan jumlah awal kosong
alat_kesehatan = {
    "pengukur tekanan darah": 0,
    "termometer": 0,
    "pengukur kadar gula darah": 0,
    "pengukur tensi": 0
}

# Fungsi untuk menampilkan alat kesehatan yang masih dipinjam
def tampilkan_alat():
    print("\nStatus alat kesehatan yang masih dipinjam:")
    for alat, jumlah in alat_kesehatan.items():
        if jumlah > 0:
            print(f"{alat}: {jumlah} buah")
    print("-" * 40)

# Fungsi untuk memproses peminjaman alat
def pinjam_alat():
    print("\nMasukkan data peminjaman alat kesehatan:")
    for alat in alat_kesehatan.keys():
        try:
            jumlah = int(input(f"Berapa {alat} yang dipinjam? "))
            if jumlah > 0:
                alat_kesehatan[alat] += jumlah
        except ValueError:
            
            print("Input harus berupa angka. Data ini dilewati.")
    tampilkan_alat()

# Fungsi untuk memproses pengembalian alat
def kembalikan_alat():
    print("\nMasukkan data pengembalian alat kesehatan:")
    for alat in alat_kesehatan.keys():
        try:
            jumlah = int(input(f"Berapa {alat} yang dikembalikan? "))
            if jumlah > 0 and jumlah <= alat_kesehatan[alat]:
                alat_kesehatan[alat] -= jumlah
            elif jumlah > alat_kesehatan[alat]:
                print(f"Jumlah yang dikembalikan melebihi yang dipinjam. Dibatalkan untuk {alat}.")
        except ValueError:
            print("Input harus berupa angka. Data ini dilewati.")
    tampilkan_alat()

# Fungsi untuk memproses pertukaran alat
def tukar_alat():
    print("\nMasukkan data pertukaran alat kesehatan:")
    try:
        alat_keluar = input("Alat yang ditukar (keluar): ").lower()
        alat_masuk = input("Alat yang ditukar (masuk): ").lower()
        jumlah_keluar = int(input(f"Jumlah {alat_keluar} yang ditukar keluar: "))
        jumlah_masuk = int(input(f"Jumlah {alat_masuk} yang ditukar masuk: "))
        
        if alat_keluar in alat_kesehatan and alat_masuk in alat_kesehatan:
            if alat_kesehatan[alat_keluar] >= jumlah_keluar:
                alat_kesehatan[alat_keluar] -= jumlah_keluar
                alat_kesehatan[alat_masuk] += jumlah_masuk
            else:
                print(f"Jumlah {alat_keluar} yang tersedia tidak mencukupi untuk ditukar.")
        else:
            print("Nama alat tidak valid.")
    except ValueError:
        print("Input harus berupa angka. Pertukaran dibatalkan.")
    tampilkan_alat()

# Menu utama
while True:
    print("\n--- Menu Peminjaman Alat Kesehatan ---")
    print("1. Pinjam alat")
    print("2. Kembalikan alat")
    print("3. Tukar alat")
    print("4. Tampilkan alat yang masih dipinjam")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        pinjam_alat()
    elif pilihan == "2":
        kembalikan_alat()
    elif pilihan == "3":
        tukar_alat()
    elif pilihan == "4":
        tampilkan_alat()
    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
