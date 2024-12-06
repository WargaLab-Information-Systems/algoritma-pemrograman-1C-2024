# Inisialisasi data awal
alat_kesehatan = {
    "alat pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "alat inhaler": 0
}

# Fungsi untuk menambah alat
def pinjam_alat():
    alat = input("Masukkan nama alat yang ingin dipinjam: ")
    jumlah = int(input(f"Masukkan jumlah {alat} yang ingin dipinjam: "))
    if alat in alat_kesehatan:
        alat_kesehatan[alat] += jumlah
        print(f"{jumlah} {alat} berhasil dipinjam.")
    else:
        print(f"{alat} tidak tersedia.")

# Fungsi untuk mengembalikan alat
def kembalikan_alat():
    alat = input("Masukkan nama alat yang ingin dikembalikan: ")
    jumlah = int(input(f"Masukkan jumlah {alat} yang ingin dikembalikan: "))
    if alat in alat_kesehatan and alat_kesehatan[alat] >= jumlah:
        alat_kesehatan[alat] -= jumlah
        print(f"{jumlah} {alat} berhasil dikembalikan.")
    else:
        print(f"Pengembalian gagal. Jumlah {alat} tidak mencukupi atau alat tidak terdaftar.")

# Fungsi untuk menukar alat
def tukar_alat():
    alat_awal = input("Masukkan nama alat yang ingin ditukar: ")
    jumlah_awal = int(input(f"Masukkan jumlah {alat_awal} yang ingin ditukar: "))
    alat_tukar = input("Masukkan nama alat pengganti: ")
    jumlah_tukar = int(input(f"Masukkan jumlah {alat_tukar} yang diinginkan: "))
    
    if alat_awal in alat_kesehatan and alat_tukar in alat_kesehatan:
        if alat_kesehatan[alat_awal] >= jumlah_awal:
            alat_kesehatan[alat_awal] -= jumlah_awal
            alat_kesehatan[alat_tukar] += jumlah_tukar
            print(f"{jumlah_awal} {alat_awal} ditukar dengan {jumlah_tukar} {alat_tukar}")
        else:
            print(f"Tukar gagal. Jumlah {alat_awal} tidak mencukupi")
    else:
        print("Salah satu alat tidak terdaftar")

# Fungsi untuk menampilkan alat yang masih dipinjam
def tampilkan_alat_terpinjam():
    alat_terpinjam = {nama: jumlah for nama, jumlah in alat_kesehatan.items() if jumlah > 0}
    if alat_terpinjam:
        print("\nAlat kesehatan yang masih dipinjam:")
        for nama, jumlah in alat_terpinjam.items():
            print(f"- {nama}: {jumlah} buah")
    else:
        print("\nTidak ada alat yang sedang dipinjam.")

# Menu interaktif
while True:
    print("\nMenu:")
    print("1. Pinjam alat")
    print("2. Kembalikan alat")
    print("3. Tukar alat")
    print("4. Tampilkan alat yang masih dipinjam")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        pinjam_alat()
    elif pilihan == "2":
        kembalikan_alat()
    elif pilihan == "3":
        tukar_alat()
    elif pilihan == "4":
        tampilkan_alat_terpinjam()
    elif pilihan == "5":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi")
