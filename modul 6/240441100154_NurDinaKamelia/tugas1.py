# Membuat list kosong untuk menyimpan data karyawan
karyawan = []

# Fungsi untuk menginput data karyawan
def input_data():
    while True:
        nip = input("Masukkan NIP (atau ketik 'keluar' untuk berhenti): ")
        if nip.lower() == 'keluar': # untuk mengubah semua huruf menjadi huruf kecil
            break
        
        # Cek apakah NIP sudah ada dalam data karyawan
        if any(data['NIP'] == nip for data in karyawan): # kondisi untuk mengecek,nip itu sudah di gunakan atau tidak
            print("NIP sudah ada, data tidak valid. Silakan masukkan NIP yang berbeda.")
            continue

        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        departemen = input("Masukkan Departemen: ")
        jabatan = input("Masukkan Jabatan: ")

        # Menyimpan data karyawan ke dalam list data karyawan
        data_karyawan = {
            'NIP': nip,
            'Nama': nama,
            'Alamat': alamat,
            'Departemen': departemen,
            'Jabatan': jabatan
        }
        karyawan.append(data_karyawan) #untuk menambah list ke data karyawan
        
    
        
# Fungsi untuk mencari data karyawan
def cari_data():
    cari = input("Masukkan kata kunci pencarian: ")
    hasil = []
    for data in karyawan:
        for key, value in data.items():
            if cari.lower() in value.lower():
                hasil.append(data) # jika hasil cocok maka di tambahkan ke dalam list
                break
    if hasil:
        print("Data karyawan yang ditemukan:")
        for data in hasil:
            print(data)
    else:
        print("Data tidak ditemukan.")
        
# Memanggil fungsi untuk menginput data
input_data()

# Memanggil fungsi untuk mencari data
cari_data()
