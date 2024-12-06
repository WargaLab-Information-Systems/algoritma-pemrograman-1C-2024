data_barang = []

def tambah_barang(data_barang):
    ID_barang = input("Masukkan ID Barang: ")
    nama_barang = input("Masukkan Nama Barang: ")
    prioritas = input("Masukkan Tingkat Prioritas (Darurat/Biasa/Non-Darurat): ").lower()

    barang = (nama_barang, ID_barang, prioritas)

    if prioritas == "Darurat":
        data_barang.insert(0, barang)
    elif prioritas == "Biasa":
        tengah = len(data_barang) 
        data_barang.insert(tengah, barang)
    elif prioritas == "Non-Darurat":
        data_barang.append(barang)
    else:
        print("Prioritas tidak valid. Silakan pilih antara 'Darurat', 'Biasa', atau 'Non-Darurat'.")
        return  

    print("Data barang berhasil ditambahkan")

def tampilkan_barang(data_barang):
        for barang in data_barang:
            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")
        print() 

def menu():
    while True:
        tambah_barang(data_barang)  
        tampilkan_barang(data_barang) 

        lagi = input("Apakah Anda ingin menambahkan barang lagi? (ya/tidak): ")
        if lagi == "ya":
            continue 
        elif lagi == "tidak":
            print("Program selesai.")  
            break  
        else:
            print("Pilihan tidak valid, program selesai.")  
            break 

menu()