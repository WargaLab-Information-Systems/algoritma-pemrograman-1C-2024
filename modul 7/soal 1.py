

def pengelola_alat_kesehatan():
    alat_dipinjam = {}

    while True:
        print("\nMenu:")
        print("1. Tambah alat")
        print("2. Kurangi alat")
        print("3. Tampilkan alat")
        print("4. Keluar")

        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 1:
            alat = input("Masukkan nama alat: ")
            jumlah = int(input("Masukkan jumlah yang dipinjam: "))
            if alat in alat_dipinjam:
                alat_dipinjam[alat] += jumlah
            else:
                alat_dipinjam[alat] = jumlah
        elif pilihan == 2:
            alat = input("Masukkan nama alat yang dikembalikan: ")
            jumlah = int(input("Masukkan jumlah yang dikembalikan: "))
            if alat in alat_dipinjam:
                alat_dipinjam[alat] -= jumlah
                if alat_dipinjam[alat] <= 0:
                    del alat_dipinjam[alat]
            else:
                print("Alat tidak ditemukan")
        elif pilihan == 3:
            print("Alat kesehatan yang dipinjam saat ini:")
            for alat, jumlah in alat_dipinjam.items():
                print(f"{alat}: {jumlah}")
        elif pilihan == 4:
            break
        else:
            print("Pilihan tidak valid")

pengelola_alat_kesehatan()
