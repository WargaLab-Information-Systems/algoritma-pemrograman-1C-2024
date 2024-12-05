# Data siswa dan kelas
kelas = []  # Daftar kelas
kelas_counter = 1  # Menyimpan ID kelas berikutnya
max_siswa_per_kelas = 3  # Batas maksimal siswa per kelas

def tambah_siswa(nama, asal_sekolah):
    global kelas_counter

    # Cari kelas yang masih bisa menampung siswa
    if len(kelas) == 0 or len(kelas[-1]) >= max_siswa_per_kelas:
        kelas.append([])  # Tambahkan kelas baru jika kelas sebelumnya penuh
        kelas_counter += 1
    
    # Tambahkan siswa ke kelas terakhir
    kelas[-1].append({'nama': nama, 'asal_sekolah': asal_sekolah})

def tampilkan_semua_kelas():
    if len(kelas) == 0:
        print("Belum ada siswa yang terdaftar.")
    else:
        for i, k in enumerate(kelas, start=1):
            print(f"\nKelas {i}:")
            for siswa in k:
                print(f" - {siswa['nama']} ({siswa['asal_sekolah']})")

def update_siswa(nama_lama, nama_baru, asal_sekolah_baru):
    for k in kelas:
        for siswa in k:
            if siswa['nama'] == nama_lama:
                siswa['nama'] = nama_baru
                siswa['asal_sekolah'] = asal_sekolah_baru
                print(f"Siswa {nama_lama} berhasil diupdate.")
                return
    print(f"Siswa dengan nama {nama_lama} tidak ditemukan.")

def hapus_siswa(nama):
    for k in kelas:
        for siswa in k:
            if siswa['nama'] == nama:
                k.remove(siswa)
                print(f"Siswa {nama} telah dihapus.")
                return
    print(f"Siswa dengan nama {nama} tidak ditemukan.")

def menu():
    while True:
        print("\n--- Menu Bimbingan ---")
        print("1. Tambah Siswa")
        print("2. Tampilkan Semua Kelas")
        print("3. Update Data Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah siswa: ")
            tambah_siswa(nama, asal_sekolah)
            print(f"Siswa {nama} berhasil ditambahkan.")
        
        elif pilihan == '2':
            tampilkan_semua_kelas()

        elif pilihan == '3':
            nama_lama = input("Masukkan nama siswa yang ingin diupdate: ")
            nama_baru = input("Masukkan nama baru: ")
            asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
            update_siswa(nama_lama, nama_baru, asal_sekolah_baru)
        
        elif pilihan == '4':
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            hapus_siswa(nama)
        
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

menu()