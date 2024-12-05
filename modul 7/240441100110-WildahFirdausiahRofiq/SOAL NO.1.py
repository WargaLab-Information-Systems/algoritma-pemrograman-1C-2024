def pengelola_alat_kesehatan():
    alat_dipinjam = {}

    while True:
        print("\nMenu:")
        print("1. Tambah alat")
        print("2. Kembalikan alat")
        print("3. Tampilkan alat")
        print("4. Tukar alat")
        print("5. Keluar")

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
            alat_keluar = input("Masukkan nama alat yang akan ditukar: ")
            jumlah_keluar = int(input("Masukkan jumlah alat yang akan ditukar: "))
            if alat_keluar in alat_dipinjam and alat_dipinjam[alat_keluar] >= jumlah_keluar:
                alat_dipinjam[alat_keluar] -= jumlah_keluar
                if alat_dipinjam[alat_keluar] == 0:
                    del alat_dipinjam[alat_keluar]
                
                # Memasukkan alat pengganti
                alat_masuk = input("Masukkan nama alat pengganti: ")
                jumlah_masuk = int(input("Masukkan jumlah alat pengganti yang diterima: "))
                if alat_masuk in alat_dipinjam:
                    alat_dipinjam[alat_masuk] += jumlah_masuk
                else:
                    alat_dipinjam[alat_masuk] = jumlah_masuk
                print(f"Tukar berhasil: {jumlah_keluar} {alat_keluar} ditukar dengan {jumlah_masuk} {alat_masuk}.")
            else:
                print("Alat yang akan ditukar tidak cukup atau tidak ditemukan.")

        elif pilihan == 5:
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid")

pengelola_alat_kesehatan()
