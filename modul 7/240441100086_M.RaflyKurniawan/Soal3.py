data_siswa = {}

def tambah_siswa():
    nama = input("Masukkan nama siswa: ").strip()
    kelas = input("Masukkan kelas (contoh: X, XI, XII): ").strip()
    asal_sekolah = input("Masukkan asal sekolah: ").strip()

    if kelas not in data_siswa:
        data_siswa[kelas] = []

    # Membuka kelas baru jika jumlah siswa mencapai kelipatan 3
    if len(data_siswa[kelas]) % 3 == 0 and len(data_siswa[kelas]) > 0:
        kelas_baru = f"{kelas}-{len(data_siswa[kelas]) // 3 + 1}"
        data_siswa[kelas_baru] = data_siswa.pop(kelas)
        data_siswa[kelas] = []

    
    data_siswa[kelas].append({
        "nama": nama,
        "asal sekolah": asal_sekolah,
        "plotting": kelas
    })
    print(f"Siswa {nama} berhasil ditambahkan ke kelas {kelas}.")

def tampilkan_siswa():
    print("\n--- Daftar Siswa Berdasarkan Kelas ---")
    for kelas, siswa_list in data_siswa.items():
        print(f"\nKelas {kelas}:")
        if not siswa_list:
            print("  Tidak ada siswa.")
        else:
            for idx, siswa in enumerate(siswa_list, start=1):
                print(f"  {idx}. Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal sekolah']}")

def hapus_siswa():
    nama = input("Masukkan nama siswa yang ingin dihapus: ").strip()
    kelas = input("Masukkan kelas siswa tersebut: ").strip()

    if kelas in data_siswa:
        for siswa in data_siswa[kelas]:
            if siswa["nama"].lower() == nama.lower():
                data_siswa[kelas].remove(siswa)
                print(f"Siswa {nama} berhasil dihapus dari kelas {kelas}.")
                return
        print(f"Siswa {nama} tidak ditemukan di kelas {kelas}.")
    else:
        print(f"Kelas {kelas} tidak ditemukan.")

def memperbarui_data_siswa():
    nama = input("Masukkan nama siswa yang ingin diperbarui: ").strip()
    kelas = input("Masukkan kelas siswa tersebut: ").strip()

    if kelas in data_siswa:
        for siswa in data_siswa[kelas]:
            if siswa["nama"].lower() == nama.lower():
                siswa["nama"] = input("Masukkan nama baru: ").strip()
                siswa["asal sekolah"] = input("Masukkan asal sekolah baru: ").strip()
                print(f"Data siswa {nama} berhasil diperbarui.")
                return
        print(f"Siswa {nama} tidak ditemukan di kelas {kelas}.")
    else:
        print(f"Kelas {kelas} tidak ditemukan.")

def menu():
    while True:
        print("\n---Menu Program Bimbingan Intensif---")
        print("1. Tambah Siswa")
        print("2. Tampilkan Siswa")
        print("3. Hapus Siswa")
        print("4. Update Data Siswa")
        print("5. Keluar")
        print("---------------------------------------")

        pilihan = input("Pilih opsi (1-5): ").strip()
        if pilihan == "1":
            tambah_siswa()
        elif pilihan == "2":
            tampilkan_siswa()
        elif pilihan == "3":
            hapus_siswa()
        elif pilihan == "4":
            memperbarui_data_siswa()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Input tidak valid, silakan coba lagi.")

menu()

