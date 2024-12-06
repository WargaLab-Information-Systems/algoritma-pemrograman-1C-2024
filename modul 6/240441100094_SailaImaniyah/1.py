data_karyawan = []

# Fungsi untuk menambah data karyawan
def tambah_karyawan():
    nip = input("Masukkan NIP: ")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")
    data_karyawan.append((nip, nama, alamat, departemen, jabatan))
    print("Data karyawan berhasil ditambahkan.\n")

# Fungsi untuk mencari data karyawan berdasarkan atribut
def cari_karyawan(atribut, nilai):
    index = ["nip", "nama", "alamat", "departemen", "jabatan"].index(atribut)
    hasil_cari = []

    for karyawan in data_karyawan:
        if karyawan[index].lower() == nilai.lower():
            hasil_cari.append(karyawan)

    return hasil_cari

def main():
    # Tambahkan minimal 5 data karyawan
    print("=== Input Data Karyawan ===")
    for i in range(5):
        print(f"Data Karyawan {i+1}")
        tambah_karyawan()
    
    # Cari data karyawan berdasarkan atribut
    while True:
        print("=== Cari Data Karyawan ===")
        atribut = input("Masukkan atribut pencarian (nip/nama/alamat/departemen/jabatan): ").lower()
        if atribut not in ["nip", "nama", "alamat", "departemen", "jabatan"]:
            print("Atribut tidak valid. Silakan coba lagi.")
            continue
        
        nilai = input(f"Masukkan nilai untuk {atribut}: ")
        hasil_cari = cari_karyawan(atribut, nilai)

        print("\n=== Hasil Pencarian ===")
        if hasil_cari:
            # Menampilkan hasil pencarian jika ada yang cocok
            for karyawan in hasil_cari:
                print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
        else:
            print("Tidak ada data yang ditemukan.")
        
        lanjut = input("Apakah ingin mencari lagi? (y/n): ").lower()
        if lanjut != "y":
            break

# Jalankan program
main()