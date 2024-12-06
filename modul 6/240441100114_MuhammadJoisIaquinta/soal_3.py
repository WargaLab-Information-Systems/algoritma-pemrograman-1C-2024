daftar_barang = []
def tambah_barang(nama_barang, id_barang, prioritas, daftar_barang):
    if prioritas == "darurat":
        daftar_barang.insert(0, (nama_barang, id_barang, prioritas))
    elif prioritas == "biasa":
        daftar_barang.insert(len(daftar_barang) // 2, (nama_barang, id_barang, prioritas))
    elif prioritas == "non-darurat":
        daftar_barang.append((nama_barang, id_barang, prioritas))
    else:
        print("Prioritas tidak valid. Masukkan 'Darurat', 'Biasa', atau 'Non-Darurat'.")
 
def tampilkan_daftar_barang(daftar_barang):
    print("Daftar Barang:")
    for barang in daftar_barang:
        print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")
                                                                                            
def main(): 

    while True:
        print("Input Data Barang")
        nama_barang = input("Masukkan Nama Barang: ")
        id_barang = input("Masukkan ID Barang: ")
        prioritas = input("Masukkan Prioritas (Darurat, Biasa, Non-Darurat): ")

        tambah_barang(nama_barang, id_barang, prioritas, daftar_barang)
        tampilkan_daftar_barang(daftar_barang)

        lanjut = input("Apakah ingin menambahkan barang lagi? (y/n): ")
        if lanjut.lower() != 'y':
            break

main()