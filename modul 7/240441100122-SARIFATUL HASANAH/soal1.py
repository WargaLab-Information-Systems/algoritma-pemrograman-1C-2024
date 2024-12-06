alat_tersedia = {"tekanandarah", "termometer", "kadarguladarah", "pengukurtensi"}

alat = {
    "tekanandarah": 0,
    "termometer": 0,
    "kadarguladarah": 0,
    "pengukurtensi": 0,
}

def tampil():
    print("\n=== Alat yang Dipinjam Saat Ini ===")
    for alt, jumlah in alat.items():
        print(alt," : ", jumlah)
    print()

def pinjam(): 
    tampil()
    alt = input("Masukkan nama alat yang ingin dipinjam: ").lower()
    if alt in alat_tersedia:
        jumlah = int(input(f"Masukkan jumlah {alt} yang ingin dipinjam: "))
        alat[alt] += jumlah
        print(jumlah, alt ,"berhasil dipinjam.\n")
    else:
        print(f"Alat {alt} tidak ditemukan di daftar alat yang tersedia.\n")

def kembalikan():
    tampil()
    alt = input("Masukkan nama alat yang ingin dikembalikan: ").lower()
    if alt in alat_tersedia:
        jumlah = int(input(f"Masukkan jumlah {alt} yang ingin dikembalikan: "))
        if jumlah == 0 :
            print("Tidak ada barang yang dipinjam")
        elif alat[alt] >= jumlah:
            alat[alt] -= jumlah
            print(jumlah, alt ,"berhasil dikembalikan.\n")
        else:
            print(f"Gagal: Jumlah {alt} yang dikembalikan melebihi yang dipinjam.\n")
    else:
        print(f"Alat {alt} tidak ditemukan di daftar alat yang tersedia.\n")



def tukar():
    tampil()
    alt1 = input("Masukkan nama alat yang ingin ditukar: ").lower()
    if alt1 in alat_tersedia:
        jumlah1 = int(input(f"Masukkan jumlah {alt1} yang ingin ditukar: "))
        alt2 = input("Masukkan nama alat pengganti: ").lower()
        if alt2 in alat_tersedia:
            jumlah2 = int(input(f"Masukkan jumlah {alt2} yang ingin diterima: "))
            if jumlah1 == 0 or jumlah2 == 0:
                print("Barang yang ingin ditukar tidak ada")
            elif alat[alt1] >= jumlah1:
                alat[alt1] -= jumlah1
                alat[alt2] += jumlah2
                print(f"{jumlah1} {alt1} berhasil ditukar dengan {jumlah2} {alt2}.\n")
            else:
                print(f"Gagal menukar: Jumlah {alt1} tidak mencukupi.\n")
        else:
            print(f"Alat pengganti {alt2} tidak ditemukan di daftar alat yang tersedia.\n")
    else:
        print(f"Alat {alt1} tidak ditemukan di daftar alat yang tersedia.\n")

def menu_utama():
    while True:
        print("=== Menu ===")
        print("1. Pinjam Alat")
        print("2. Tampilkan")
        print("3. Kembalikan alat")
        print("4. Tukar alat")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            pinjam()
        elif pilihan == "2":
            tampil()
        elif pilihan == "3":
            kembalikan()
        elif pilihan == "4":
            tukar()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid.\n")

menu_utama()
