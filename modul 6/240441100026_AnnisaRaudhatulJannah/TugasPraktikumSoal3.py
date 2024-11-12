def main():
    barang_list = []

    while True:
        nama_barang = input("Masukkan Nama Barang: ")
        id_barang = input("Masukkan ID Barang: ")
        prioritas = input("Masukkan Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ")

        # Menyimpan barang berdasarkan prioritas
        if prioritas.lower() == "darurat":
            barang_list.insert(0, (nama_barang, id_barang, prioritas))
        elif prioritas.lower() == "biasa":
            # Menambahkan di tengah-tengah jika ada barang
            if barang_list:
                barang_list.insert(len(barang_list)//2, (nama_barang, id_barang, prioritas))
            else:
                barang_list.append((nama_barang, id_barang, prioritas))  
        elif prioritas.lower() == "non-darurat":
            barang_list.append((nama_barang, id_barang, prioritas))
        else:
            print("Prioritas tidak valid. Silakan coba lagi.")
            continue

        print("\nData Barang yang telah diinputkan:")
        for barang in barang_list:
            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, prioritas: {barang[2]}")

        lagi = input("Apakah Anda ingin mengisi data barang lagi? (y/n): ")
        if lagi.lower() != 'y':
            break

    print("\nData Barang Akhir:")
    for barang in barang_list:
        print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, prioritas: {barang[2]}")

# if __name__ == "__main__":
main()