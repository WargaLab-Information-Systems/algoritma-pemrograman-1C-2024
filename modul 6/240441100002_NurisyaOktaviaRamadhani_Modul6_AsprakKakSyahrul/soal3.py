barang_list = []
def tambah_barang(barang_list):
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    print("\nPilih Tingkat Prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    prioritas = input("Masukkan pilihan prioritas (1-3): ")
    barang = (nama_barang, id_barang, prioritas)
    if prioritas == '1':
        barang_list.insert(0, barang)
    elif prioritas == '2':
        mid_index = len(barang_list) // 2
        barang_list.insert(mid_index, barang)
    elif prioritas == '3':
        barang_list.append(barang)
    else:
        print("Pilihan prioritas tidak valid. Barang tidak ditambahkan.")
    print("\nBarang berhasil ditambahkan.\n")
def tampilkan_barang(barang_list):
    print("\nDaftar Barang yang Telah Dimasukkan:")
    for barang in barang_list:
        prioritas_str = ""
        if barang[2] == '1':
            prioritas_str = "Darurat"
        elif barang[2] == '2':
            prioritas_str = "Biasa"
        elif barang[2] == '3':
            prioritas_str = "Non-Darurat"
        print(f"Nama Barang   : {barang[0]}")
        print(f"ID Barang     : {barang[1]}")
        print(f"Prioritas     : {prioritas_str}")
        print("-" * 30)
while True:
    tambah_barang(barang_list)
    tampilkan_barang(barang_list)
    lagi = input("\nApakah Anda ingin menambah barang lagi? (ya/tidak): ")
    if lagi != "ya" and lagi != "Ya":
        print("Terima kasih telah menggunakan program ini!")
        break