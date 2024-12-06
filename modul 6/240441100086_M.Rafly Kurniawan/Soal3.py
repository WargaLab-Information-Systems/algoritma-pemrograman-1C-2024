print("---DATA BARANG---")
darurat = []
biasa = []
non_darurat = []


#Tambah dan Menampilkan
def tambah_dan_tampilkan_barang():

    id_barang = input("Masukkan ID Barang: ")
    nama_barang = input("Masukkan Nama Barang: ")
    prioritas = input("Masukkan Prioritas Barang (Darurat, Biasa, Non-Darurat): ").lower()

    if prioritas == "darurat":
        darurat.append((id_barang, nama_barang, "Darurat"))
    elif prioritas == "biasa":
        biasa.append((id_barang, nama_barang, "Biasa"))
    elif prioritas == "non-darurat":
        non_darurat.append((id_barang, nama_barang, "Non-Darurat"))
    else:
        print("Pilihan tidak valid. Data tidak ditambahkan.")
        return

    semua_barang = darurat + biasa + non_darurat

    print("\nDaftar Barang:")

    for index, barang in enumerate(semua_barang, 1):
        print(f"{index}.ID Barang: {barang[0]}, Nama Barang: {barang[1]}, Prioritas Barang: {barang[2]}")


#Menambah barang
while True:
    tambah_dan_tampilkan_barang()
    lanjut = input("\nIngin menambah barang lagi? (Ya/Tidak): ").lower()
    if lanjut == 'tidak':
        print("Program selesai.")
        break