

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

main() #untuk menjalankan semua program
=======
# List untuk menyimpan data barang berdasarkan prioritas
barang_list = []

# Fungsi untuk menambah barang berdasarkan prioritas
def tambah_barang():
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Masukkan Prioritas Barang (Darurat/Biasa/Non-Darurat): ").lower()
    
    # Menyimpan barang berdasarkan prioritas
    if prioritas == "darurat":
        # Menambahkan barang pada posisi awal list
        barang_list.insert(0, (id_barang, nama_barang, prioritas))
    elif prioritas == "biasa":
        # Menambahkan barang pada posisi tengah list
        tengah = len(barang_list) // 2
        barang_list.insert(tengah, (id_barang, nama_barang, prioritas))
    elif prioritas == "non-darurat":
        # Menambahkan barang di akhir list
        barang_list.append((id_barang, nama_barang, prioritas))
    else:
        print("Prioritas tidak valid! Barang tidak ditambahkan.")
        return
    
    print("\nBarang berhasil ditambahkan!")

# Fungsi untuk menampilkan semua barang yang ada di list
def tampilkan_barang():
    if barang_list:
        print("\nDaftar Barang yang Dikirim:")
        for barang in barang_list:
            print(f"ID Barang: {barang[0]}, Nama Barang: {barang[1]}, Prioritas: {barang[2]}")
    else:
        print("Belum ada barang yang ditambahkan.")

# Program utama
def main():
    while True:
        # Menambahkan barang
        tambah_barang()

        # Menampilkan semua barang yang ada
        tampilkan_barang()

        # Menanyakan apakah ingin menambah barang lagi
        lanjut = input("\nApakah Anda ingin menambah barang lagi? (ya/tidak): ").lower()
        if lanjut != "ya":
            print("\nProgram selesai. Terima kasih!")
            break

# Menjalankan program

main()

