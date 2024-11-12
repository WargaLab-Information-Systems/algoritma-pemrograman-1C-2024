barang_list = []

def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Masukkan Prioritas Barang (Darurat/Biasa/Non-Darurat): ").lower()

    if prioritas == "darurat":
        barang_list.insert(0, (nama_barang, id_barang, prioritas))
    elif prioritas == "biasa":
        if len(barang_list) > 0:
            tengah = len(barang_list) // 2
            barang_list.insert(tengah, (nama_barang, id_barang, prioritas))
        else:
            barang_list.append((nama_barang, id_barang, prioritas))
    elif prioritas == "non-darurat":
        barang_list.append((nama_barang, id_barang, prioritas))
    else:
        print("Prioritas tidak valid. Masukkan 'Darurat', 'Biasa', atau 'Non-Darurat'.")
        return

    print("\nDaftar Barang yang Telah Dimasukkan:")
    for barang in barang_list:
        print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

# Program utama
def main():
    while True:
        tambah_barang()
        
        lagi = input("\nApakah Anda ingin menambahkan barang lagi? (ya/tidak): ").lower()
        if lagi != "ya":
            print("\nTerima kasih, program selesai.")
            break

main()
