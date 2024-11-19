# List untuk menyimpan data karyawan
karyawan = []

# Fungsi untuk menambah karyawan
def tambah_karyawan():
    # Validasi agar NIP unik dan tidak boleh kosong
    while True:
        nip = input("NIP: ")
        if any(k['nip'] == nip for k in karyawan):
            print("NIP sudah ada, silakan masukkan NIP yang berbeda.")
        elif not nip.strip():
            print("NIP tidak boleh kosong.")
        else:
            break
    
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    departemen = input("Departemen: ")
    jabatan = input("Jabatan: ")
    
    # Membuat dictionary untuk menyimpan data karyawan
    data = {
        'nip': nip,
        'nama': nama,
        'alamat': alamat,
        'departemen': departemen,
        'jabatan': jabatan
    }
    karyawan.append(data)
    print("Data berhasil ditambahkan!\n")

# Fungsi untuk mencari karyawan
def cari_karyawan():
    print("\nCari berdasarkan:")
    print("1. NIP")
    print("2. Nama")
    print("3. Alamat")
    print("4. Departemen")
    print("5. Jabatan")
    
    pilihan = input("Pilih (1-5): ")
    cari = input("Masukkan kata kunci: ").lower()
    
    kategori = ['nip', 'nama', 'alamat', 'departemen', 'jabatan']
    kategori_dipilih = kategori[int(pilihan)-1]
    
    # Variabel untuk memeriksa apakah ada hasil yang ditemukan
    ditemukan = False
    print("\nHasil pencarian:")
    for k in karyawan:
        if cari in k[kategori_dipilih].lower():
            ditemukan = True
            print(f"\nNIP: {k['nip']}")
            print(f"Nama: {k['nama']}")
            print(f"Alamat: {k['alamat']}")
            print(f"Departemen: {k['departemen']}")
            print(f"Jabatan: {k['jabatan']}")
    
    # Jika tidak ada data yang ditemukan, tampilkan pesan
    if not ditemukan:
        print("Data karyawan tidak ditemukan.")

# Fungsi untuk menampilkan seluruh data karyawan
def tampilkan_semua_karyawan():
    if len(karyawan) == 0:
        print("Belum ada data karyawan.")
    else:
        print("\nData Seluruh Karyawan:")
        for k in karyawan:
            print(f"\nNIP: {k['nip']}")
            print(f"Nama: {k['nama']}")
            print(f"Alamat: {k['alamat']}")
            print(f"Departemen: {k['departemen']}")
            print(f"Jabatan: {k['jabatan']}")

# Program utama
while True:
    print("\nMenu:")
    print("1. Tambah Karyawan")
    print("2. Cari Karyawan")
    print("3. Tampilkan Seluruh Karyawan")
    print("4. Keluar")
    
    menu = input("Pilih menu (1-4): ")
    
    if menu == '1':
        # Pastikan untuk meminta minimal 5 data karyawan
        if len(karyawan) < 5:
            print(f"\nMasukkan data untuk karyawan ke-{len(karyawan) + 1}")
        tambah_karyawan()
    elif menu == '2':
        cari_karyawan()
    elif menu == '3':
        tampilkan_semua_karyawan()
    elif menu == '4':
        print("Program selesai")
        break
    else:
        print("Menu tidak valid!")
