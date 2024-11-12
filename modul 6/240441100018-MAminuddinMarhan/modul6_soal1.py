data_karyawan = []
def tambah_karyawan(NIP, Nama, Alamat, Departemen, Jabatan):
    karyawan = [NIP, Nama, Alamat, Departemen, Jabatan]
    data_karyawan.append(karyawan)
def menampilkan_karyawan():
    print("\nData Karyawan: ")
    for a, karyawan in enumerate(data_karyawan, start=1):
        print(f"{a}. NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
def cari_karyawan(atribut, data):
    hasil = []
    if atribut == "NIP":
        index = 0
    elif atribut == "Nama":
        index = 1
    elif atribut == "Alamat":
        index = 2
    elif atribut == "Departemen":
        index = 3
    elif atribut == "Jabatan":
        index = 4
    else:
        print("Atribut tidak valid, harap masukkan atribut yang valid")
        return
    for karyawan in data_karyawan:
        if karyawan[index].lower() == data.lower():
            hasil.append(karyawan)
    if hasil:
        print("\nHasil Pencarian: ")
        for karyawan in hasil:
            print(f"NIP: {karyawan[0]}, Nama: {karyawan[1]}, Alamat: {karyawan[2]}, Departemen: {karyawan[3]}, Jabatan: {karyawan[4]}")
    else:
        print(f"Tidak ditemukan karyawan dengan {atribut} '{data}'.")
print("Masukkan 5 data karyawan: ")
for i in range(5):
    print(f"Data karyawan ke-{i+1}")
    while True:
        nip = input(f"Masukkan NIP karyawan ke-{i+1}: ")
        if nip.strip():
            break
        print("NIP tidak boleh kosong, harap masukkan NIP.")
    while True:
        nama = input(f"Masukkan Nama karyawan ke-{i+1}: ")
        if nama.strip():
            break
        print("Nama tidak boleh kosong, harap masukkan Nama.")
    while True:
        alamat = input(f"Masukkan Alamat karyawan ke-{i+1}: ")
        if alamat.strip():
            break
        print("Alamat tidak boleh kosong, harap masukkan Alamat.")
    while True:
        departemen = input(f"Masukkan Departemen karyawan ke-{i+1}: ")
        if departemen.strip():
            break
        print("Departemen tidak boleh kosong, harap masukkan Departemen.")
    while True:
        jabatan = input(f"Masukkan Jabatan karyawan ke-{i+1}: ")
        if jabatan.strip():
            break
        print("Jabatan tidak boleh kosong, harap masukkan Jabatan.")
    tambah_karyawan(nip, nama, alamat, departemen, jabatan)
menampilkan_karyawan()
while True:
    print("\nCari Karyawan")
    print("Atribut yang tersedia: NIP, Nama, Alamat, Departemen, Jabatan")
    atribut = input("Masukkan atribut yang ingin anda cari, atau ketik 'keluar' untuk keluar program: ")
    if atribut == "keluar":
        print("Terima kasih telah menggunakan program ini:D")
        break
    elif atribut not in ["NIP", "Nama", "Alamat", "Departemen", "Jabatan"]:
        print("Atribut tidak valid. Harap masukkan atribut yang tersedia")
        continue
    data = input(f"Masukkan data {atribut} yang dicari: ")
    cari_karyawan(atribut, data)