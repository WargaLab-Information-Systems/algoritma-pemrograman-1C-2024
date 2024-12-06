# Membuat dictionary untuk menyimpan alat kesehatan dan jumlahnya
alat_kesehatan = {
    "alat pengukur tekanan darah": 0,
    "termometer": 0,
    "stetoskop": 0,
    "alat inhaler": 0,
}

def peminjaman():
    # Meminta inputan untuk peminjaman alat
    print("Masukkan alat yang dipinjam:")
    alat = input("Nama alat: ")
    jumlah = int(input("Jumlah yang dipinjam: "))
    
    # Menambah jumlah alat yang dipinjam
    if alat in alat_kesehatan:
        alat_kesehatan[alat] += jumlah
    else:
        print(f"Alat {alat} tidak dikenal.")
        
def pengembalian():
    # Meminta inputan untuk pengembalian alat
    print("Masukkan alat yang dikembalikan:")
    alat = input("Nama alat: ")
    jumlah = int(input("Jumlah yang dikembalikan: "))
    
    # Mengurangi jumlah alat yang dipinjam
    if alat in alat_kesehatan and alat_kesehatan[alat] >= jumlah:
        alat_kesehatan[alat] -= jumlah
    else:
        print(f"Jumlah {alat} yang dikembalikan tidak valid atau tidak cukup.")
        
def penukaran():
    # Meminta inputan untuk penukaran alat
    print("Masukkan alat yang ditukar:")
    alat_ditukar = input("Nama alat yang ditukar: ")
    jumlah_ditukar = int(input("Jumlah alat yang ditukar: "))
    
    alat_baru = input("Nama alat pengganti: ")
    jumlah_baru = int(input("Jumlah alat pengganti: "))
    
    # Menukar alat (mengurangi yang ditukar, menambah yang baru)
    if alat_ditukar in alat_kesehatan and alat_kesehatan[alat_ditukar] >= jumlah_ditukar:
        alat_kesehatan[alat_ditukar] -= jumlah_ditukar
        if alat_baru in alat_kesehatan:
            alat_kesehatan[alat_baru] += jumlah_baru
        else:
            print(f"Alat {alat_baru} tidak dikenal.")
    else:
        print(f"Jumlah {alat_ditukar} yang ditukar tidak valid atau tidak cukup.")

def tampilkan_alat():
    print("\nAlat kesehatan yang dipinjam saat ini:")
    for alat, jumlah in alat_kesehatan.items():
        if jumlah > 0:
            print(f"{alat}: {jumlah}")

# Program utama
def main():
    while True:
        print("\nPilih aksi:")
        print("1. Peminjaman alat")
        print("2. Pengembalian alat")
        print("3. Penukaran alat")
        print("4. Tampilkan alat yang dipinjam")
        print("5. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
        
        if pilihan == '1':
            peminjaman()
        elif pilihan == '2':
            pengembalian()
        elif pilihan == '3':
            penukaran()
        elif pilihan == '4':
            tampilkan_alat()
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Menjalankan program utama
main()