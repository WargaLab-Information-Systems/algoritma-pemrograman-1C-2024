class Siswa:
    # Atribut kelas untuk menyimpan daftar siswa
    daftar_siswa = []

    def tambah_siswa(nama, asal_sekolah):
        # Hitung jumlah kelas yang ada
        jumlah_kelas = (len(Siswa.daftar_siswa) // 3) + 1
        kelas = f"Kelas {jumlah_kelas}"
        plotting = input("Masukkan plotting bimbingan siswa: ")

        # Tambahkan siswa baru sebagai dictionary
        siswa_baru = {
            'nama': nama,
            'kelas': kelas,
            'asal_sekolah': asal_sekolah,
            'plotting': plotting
        }
        Siswa.daftar_siswa.append(siswa_baru)
        print(f"Siswa {nama} berhasil ditambahkan ke {kelas} dengan plotting {plotting}.")

    def hapus_siswa(nama):
        for siswa in Siswa.daftar_siswa:
            if siswa['nama'] == nama:
                Siswa.daftar_siswa.remove(siswa)
                print(f"Siswa {nama} berhasil dihapus.")
                return
        print(f"Siswa {nama} tidak ditemukan.")

    def tampilkan_siswa():
        if not Siswa.daftar_siswa:
            print("Tidak ada siswa yang terdaftar.")
            return

        kelas_dict = {}
        for siswa in Siswa.daftar_siswa:
            if siswa['kelas'] not in kelas_dict:        # Pengecekan Kelas dalam Dictionary
                kelas_dict[siswa['kelas']] = []
            kelas_dict[siswa['kelas']].append(siswa)    # digunakan untuk menambahkan siswa ke list yang sudah ada.

        for kelas, siswa in kelas_dict.items():         # Loop ini akan mengiterasi setiap kelas yang ada dalam kelas_dict.
            print(f"\n{kelas}:")
            for s in siswa:
                print(f" - {s['nama']} ({s['asal_sekolah']}) - Plotting: {s['plotting']}")

    def perbarui_siswa(nama):
        for siswa in Siswa.daftar_siswa:
            if siswa['nama'] == nama:
                print(f"Siswa ditemukan: {siswa}")
                siswa['asal_sekolah'] = input("Masukkan asal sekolah baru: ")
                siswa['plotting'] = input("Masukkan plotting baru: ")
                print(f"Siswa {nama} berhasil diperbarui.")
                return
        print(f"Siswa {nama} tidak ditemukan.")

    def menu():
        while True:
            print("\n=== Menu CRUD Bimbingan Intensif Gema Ripah ===")
            print("1. Tambah Siswa")
            print("2. Hapus Siswa")
            print("3. Tampilkan Siswa")
            print("4. Perbarui Siswa")
            print("5. Keluar")

            pilihan = input("Pilih menu (1-5): ")

            if pilihan == '1':
                nama = input("Masukkan nama siswa: ")
                asal_sekolah = input("Masukkan asal sekolah: ")
                Siswa.tambah_siswa(nama, asal_sekolah)
            elif pilihan == '2':
                nama = input("Masukkan nama siswa yang ingin dihapus: ")
                Siswa.hapus_siswa(nama)
            elif pilihan == '3':
                Siswa.tampilkan_siswa()
            elif pilihan == '4':
                nama = input("Masukkan nama siswa yang ingin diperbarui: ")
                Siswa.perbarui_siswa(nama)
            elif pilihan == '5':
                print("Terima kasih! Program selesai.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
Siswa.menu()
