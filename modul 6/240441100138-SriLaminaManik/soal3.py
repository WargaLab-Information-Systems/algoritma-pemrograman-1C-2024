def tambah_barang(barang_list):
    id_barang = input("ID Barang: ")
    nama_barang = input("Nama Barang: ")
    prioritas = input("Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ").strip().lower()
    
    if prioritas == 'darurat':
        barang_list.insert(0, (id_barang, nama_barang, prioritas))
    elif prioritas == 'biasa':
        # Mencari posisi untuk memasukkan barang prioritas biasa
        darurat_count = 0
        for item in barang_list:
            if item[2] == 'darurat':
                darurat_count += 1
        barang_list.insert(darurat_count, (id_barang, nama_barang, prioritas))
    elif prioritas == 'non-darurat':
        barang_list.append((id_barang, nama_barang, prioritas))
    else:
        print("Prioritas tidak valid.")

def main():
    barang_list = []
    while True:
        tambah_barang(barang_list)
        print("\nDaftar Barang:")
        for id_barang, nama_barang, prioritas in barang_list:
            print(f"ID: {id_barang}, Nama: {nama_barang}, Prioritas: {prioritas}")
        
        if input("\nTambah lagi? (ya/tidak): ").strip().lower() != 'ya':
            break

if __name__ == "__main__":
    main()