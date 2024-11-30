
data_siswa = {}
kelas_counter = {}

# create
def tambah_siswa():
    print("⋈ ⋈ Tambahkan Data Siswa ⋈ ⋈")
    while True:
        nama = input("Masukkan Nama Siswa: ")
        if not nama:
            print("Nama tidak boleh kosong, coba lagi.")
            continue

        sekolah = input("Masukkan Asal Sekolah: ")
        if not sekolah:
            print("Asal sekolah tidak boleh kosong, coba lagi.")
            continue

        plot = input("Masukkan Plot Bimbingan: ")
        if not plot:
            print("Plot tidak boleh kosong, coba lagi.")
            continue

        if plot not in data_siswa:
            data_siswa[plot] = []
            kelas_counter[plot] = 0

        kelas = kelas_counter[plot] // 3 + 1
        data_siswa[plot].append({"nama": nama, "sekolah": sekolah, "kelas": f"{plot}-{kelas}"})
        
        kelas_counter[plot] += 1
        print(f"Siswa {nama} berhasil ditambahkan ke {plot}-{kelas}\n")

        next = input("Apakah Anda ingin menambahkan data lagi? (y/n): ")
        if next.lower() != 'y':
            break
    return main()


# read
def tampilkan_siswa():
    print("⋈ ⋈ Data Siswa ⋈ ⋈")
    for plot, siswa in data_siswa.items():
        print(f"\nPlot Bimbingan: {plot}")
        for i in range(len(siswa)):
            print(f"{i+1}. Nama: {siswa[i]['nama']}, Asal Sekolah: {siswa[i]['sekolah']}, Kelas: {siswa[i]['kelas']}")
    print()

# update
def perbarui_siswa():
    print("⋈ ⋈ Update Data Siswa ⋈ ⋈")
    plot = input("Masukkan Plot Bimbingan: ")
    
    if plot in data_siswa:
        tampilkan_siswa()
        index = input("Pilih nomor siswa yang ingin diperbarui: ")

        if index.isdigit() and 0 < int(index) <= len(data_siswa[plot]):
            index = int(index) - 1
            siswa = data_siswa[plot][index]

            nama_baru = input(f"Nama baru ({siswa['nama']}): ")
            if nama_baru.strip():
                siswa['nama'] = nama_baru

            sekolah_baru = input(f"Asal sekolah baru ({siswa['sekolah']}): ")
            if sekolah_baru.strip():
                siswa['sekolah'] = sekolah_baru

            print("Data berhasil diperbarui.\n")
        else:
            print("Nomor siswa tidak valid.\n")
    else:
        print("Plot tidak ditemukan.\n")

# hapus
def hapus_siswa():
    print("⋈ ⋈ Hapus Data Siswa ⋈ ⋈")
    plot = input("Masukkan Plot Bimbingan: ")
    if plot in data_siswa:
        tampilkan_siswa()
        index = int(input("Pilih nomor siswa yang ingin dihapus: ")) - 1
        if 0 <= index < len(data_siswa[plot]):
            nama = data_siswa[plot][index]['nama']
            del data_siswa[plot][index]
            kelas_counter[plot] -= 1
            print(f"Siswa {nama} telah dihapus.\n")
        else:
            print("Nomor siswa tidak valid.\n")
    else:
        print("Plot tidak ditemukan.\n")

# Pmenu
def main():
    while True:
        print("\n⋈ ⋈ ⋈ Lembaga Bimbingan Intensif Gema Ripah ⋈ ⋈ ⋈")
        print("1. Tambah Siswa")
        print("2. Tampilkan Siswa")
        print("3. Perbarui Siswa")
        print("4. Hapus Siswa")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_siswa()
        elif pilihan == '2':
            tampilkan_siswa()
        elif pilihan == '3':
            perbarui_siswa()
        elif pilihan == '4':
            hapus_siswa()
        elif pilihan == '0':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

main()