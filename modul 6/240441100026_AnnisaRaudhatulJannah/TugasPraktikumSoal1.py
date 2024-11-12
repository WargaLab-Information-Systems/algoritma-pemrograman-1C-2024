class Karyawan:
    def __init__(self, nip, nama, alamat, departemen, jabatan):
        self.nip = nip
        self.nama = nama
        self.alamat = alamat
        self.departemen = departemen
        self.jabatan = jabatan

    def __str__(self):
        return f"NIP: {self.nip}, Nama: {self.nama}, Alamat: {self.alamat}, Departemen: {self.departemen}, Jabatan: {self.jabatan}"

def input_karyawan():
    karyawan_list = []
    for _ in range(5):
        nip = input("Masukkan NIP: ")
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        departemen = input("Masukkan Departemen: ")
        jabatan = input("Masukkan Jabatan: ")
        karyawan = Karyawan(nip, nama, alamat, departemen, jabatan)
        karyawan_list.append(karyawan)
    return karyawan_list

def cari_karyawan(karyawan_list, keyword):
    hasil_cari = []
    for karyawan in karyawan_list:
        if (keyword.lower() in karyawan.nip.lower() or
            keyword.lower() in karyawan.nama.lower() or
            keyword.lower() in karyawan.alamat.lower() or
            keyword.lower() in karyawan.departemen.lower() or
            keyword.lower() in karyawan.jabatan.lower()):
            hasil_cari.append(karyawan)
    return hasil_cari

def main():
    karyawan_list = input_karyawan()
    keyword = input("Masukkan kata kunci untuk pencarian: ")
    hasil_cari = cari_karyawan(karyawan_list, keyword)

    if hasil_cari:
        print("Data Karyawan yang ditemukan:")
        for karyawan in hasil_cari:
            print(karyawan)
    else:
        print("Tidak ada data karyawan yang sesuai.")

if __name__ == "__main__":
    main()