data_karyawan = []

def tambah_karyawan():
    nip = input("Masukkan NIP: ")
    for karyawan in data_karyawan:
        if karyawan[0] == nip:
            print("NIP sudah ada. Program dihentikan.")
            return False 
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    departemen = input("Masukkan Departemen: ")
    jabatan = input("Masukkan Jabatan: ")
    print("______________________________")
    data_karyawan.append((nip, nama, alamat, departemen, jabatan))
   
def cari_karyawan(atribut, nilai):
    atribut = ["nip", "nama", "alamat", "departemen", "jabatan"].index(atribut)
    hasil_cari = []
    for karyawan in data_karyawan:
        if karyawan[atribut] == nilai:
            hasil_cari.append(karyawan)
    return hasil_cari

def main():
    print("=== Input Data Karyawan ===")
    while True:
        tambah_karyawan()
        lanjut = input("Apakah ingin menambahkan karyawan lagi? (y/n): ")
        if lanjut.lower() != "y":
            break

    while True:
        print("=== Cari Data Karyawan ===")
        atribut = input("Masukkan atribut pencarian (nip/nama/alamat/departemen/jabatan): ")
        if atribut not in ["nip", "nama", "alamat", "departemen", "jabatan"]:
            print("Atribut tidak valid. Silakan coba lagi.")
            continue
        
        nilai = input(f"Masukkan nilai untuk {atribut}: ")
        hasil_cari = cari_karyawan(atribut, nilai)
      
        print("=== Hasil Pencarian ===")
        if hasil_cari:
            for karyawan in hasil_cari:
                print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
        else:
            print("Tidak ada data yang ditemukan.")
        
        lanjut = input("Apakah ingin mencari lagi? (y/n): ")
        if lanjut != "y":
            break
main()
