prioritas_barang = []
def tambah_barang():
    while True:
        nama = input("Masukkan nama barang: ")
        if nama.strip():
            break
        print("Nama barang tidak boleh kosong, harap masukkan nama barang.")
    while True:
        id = input("Masukkan ID barang: ")
        if id.strip():
            break
        print("ID barang tidak boleh kosong, harap masukkan ID barang.")
    print("Tingkat prioritas barang:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    pilih_prioritas = input("Masukkan tingkat prioritas barang: ")
    if pilih_prioritas == "1":
        prioritas = "Darurat"
    elif pilih_prioritas == "2":
        prioritas = "Biasa"
    elif pilih_prioritas == "3":
        prioritas = "Non-Darurat"
    else:
        print("Input tidak valid. Masukkan berdasarkan pilihan yang ada")
        return
    prioritas_barang.append((nama, id, prioritas))
    prioritas_barang.sort(key=lambda a: a[2])
    print(f"Barang '{nama}' dengan prioritas {prioritas} telah ditambahkan ke dalam list.")
def menampilkan():
    if not prioritas_barang:
        print("Daftar prioritas barang kosong.")
    else:
        urutan_prioritas = ["Darurat", "Biasa", "Non-Darurat"]
        sorted_list = sorted(prioritas_barang, key=lambda x: urutan_prioritas.index(x[2]))
        print("Daftar prioritas barang:")
        for indeks, (nama, id, prioritas) in enumerate(sorted_list, 1):
            print(f"{indeks}. Nama barang: {nama}, ID barang: {id}, tingkat prioritas: {prioritas}.")
while True:
    print("\n=== PROGRAM DAFTAR BARANG BERDASARKAN PRIORITAS ===")
    print("1. Tambah barang")
    print("2. Tampilkan list barang")
    print("3. Keluar dari program")
    pilihan = input("Pilih salah satu dari menu di atas: ")
    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        menampilkan()
    elif pilihan == "3":
        print("Program berakhir")
        break
    else:
        print("Input tidak valid, harap masukkan opsi yang tersedia.")