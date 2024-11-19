daftar_barang = []

def tambah_barang(nama_barang, id_barang, prioritas, daftar_barang):
    # Menambahkan barang ke daftar sesuai prioritas
    if prioritas == "darurat":
        daftar_barang.insert(0, (nama_barang, id_barang, prioritas))
    elif prioritas == "biasa":
        daftar_barang.insert(len(daftar_barang) // 2, (nama_barang, id_barang, prioritas))
    elif prioritas == "non-darurat":
        daftar_barang.append((nama_barang, id_barang, prioritas))
    else:
        print("Prioritas tidak valid. Masukkan 'Darurat', 'Biasa', atau 'Non-Darurat'.")
        return
    
    urutan_prioritas = {"darurat": 0, "biasa": 1, "non-darurat": 2}
    daftar_barang.sort(key=lambda x: urutan_prioritas.get(x[2]))  
    
def tampilkan_daftar_barang(daftar_barang):
    print("\nDaftar Barang:")
    if not daftar_barang:
        print("Tidak ada barang yang terdaftar.")
    else:
        for barang in daftar_barang:
            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

def main(): 
    while True:
        print("\nInput Data Barang")
        nama_barang = input("Masukkan Nama Barang: ")
        id_barang = input("Masukkan ID Barang: ")
        prioritas = input("Masukkan Prioritas (Darurat, Biasa, Non-Darurat): ").lower()

       
        if prioritas not in ["darurat", "biasa", "non-darurat"]:
            print("Prioritas tidak valid. Masukkan 'Darurat', 'Biasa', atau 'Non-Darurat'.")
            continue
        
        tambah_barang(nama_barang, id_barang, prioritas, daftar_barang)
        tampilkan_daftar_barang(daftar_barang)

        lanjut = input("Apakah ingin menambahkan barang lagi? (y/n): ")
        if lanjut.lower() != 'y':
            break


main()
