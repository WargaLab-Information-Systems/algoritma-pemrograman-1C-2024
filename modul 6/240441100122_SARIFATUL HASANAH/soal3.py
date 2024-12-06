barang = []
list_id = []

def tambah_barang():
    while True:
        id_barang = input("Masukkan ID Barang: ")
        id = int(id_barang)
        if id in list_id:
            print("id sudah terdaftar. Harap masukkan id yang berbeda.")
        else:
            list_id.append(id)
            break
    nama_barang = input("Masukkan Nama Barang: ")
    prioritas = input("Masukkan Prioritas Barang (Darurat/Biasa/Non-Darurat): ").lower()

    if prioritas == "darurat":
        barang.insert(0, (id_barang, nama_barang, prioritas))
    elif prioritas == "biasa":
        tengah = len(barang) // 2
        barang.insert(tengah, (id_barang, nama_barang, prioritas))
    elif prioritas == "non-darurat":
        barang.append((id_barang, nama_barang, prioritas))
    else:
        print("Prioritas tidak valid! Barang tidak ditambahkan.")
        return  
    
    print("\nBarang berhasil ditambahkan!")

def tampilkan_barang():
    if barang:
        print("\nDaftar Barang yang Dikirim:")
        for brg in barang:
            print(f"ID Barang: {brg[0]}, Nama Barang: {brg[1]}, Prioritas: {brg[2]}")
    else:
        print("Belum ada barang yang ditambahkan.")

def main():
    while True:
        tambah_barang()

        tampilkan_barang()

        lanjut = input("\nApakah Anda ingin menambah barang lagi? (ya/tidak): ").lower()
        if lanjut != "ya":
            print("\nProgram selesai. Terima kasih!")
            break

main()

