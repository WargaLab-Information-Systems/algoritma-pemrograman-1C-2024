def pengelola_alat_kesehatan():
    alat_dipinjam = {}

    while True:
        print("\nMenu:")
        print("1. Tambah alat")
        print("2. Kurangi alat")
        print("3. Tampilkan alat")
        print("4. Tukar alat")
        print("5. Keluar")

        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 1:
            # Tambah alat
            alat = input("Masukkan nama alat: ")
            jumlah = int(input("Masukkan jumlah yang dipinjam: "))
            alat_dipinjam[alat] = alat_dipinjam.get(alat, 0) + jumlah
        elif pilihan == 2:
            # Kurangi alat
            alat = input("Masukkan nama alat yang dikembalikan: ")
            jumlah = int(input("Masukkan jumlah yang dikembalikan: "))
            if alat in alat_dipinjam:
                if jumlah > alat_dipinjam[alat]:
                    print(f"Gagal mengembalikan {alat_dipinjam}. Jumlah tidak mencukupi.")
                else:
                    alat_dipinjam[alat] <= jumlah
                    alat_dipinjam[alat] -= jumlah
                    print(f"{jumlah} {alat_dipinjam} berhasil dikembalikan!")
                    del alat_dipinjam[alat]
            else:
                print(f"Gagal mengembalikan {alat_dipinjam}. Jumlah tidak mencukupi.")
            
        elif pilihan == 3:
            # Tampilkan alat
            print("Alat kesehatan yang dipinjam saat ini:")
            for alat, jumlah in alat_dipinjam.items():
                print(f"{alat}: {jumlah}")
        elif pilihan == 4:
            # Tukar alat
            alat_lama = input("Masukkan nama alat yang ingin ditukar: ")
            alat_baru = input("Masukkan nama alat pengganti: ")
            if alat_lama in alat_dipinjam:
                jumlah = alat_dipinjam[alat_lama]
                del alat_dipinjam[alat_lama]
                alat_dipinjam[alat_baru] = alat_dipinjam.get(alat_baru, 0) + jumlah
                print(f"Alat {alat_lama} berhasil ditukar dengan {alat_baru}")
            else:
                print("Alat yang ingin ditukar tidak ditemukan")
        elif pilihan == 5:
            # Keluar
            break
        else:
            print("Pilihan tidak valid")

pengelola_alat_kesehatan()
