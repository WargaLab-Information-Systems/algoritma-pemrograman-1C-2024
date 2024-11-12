list_barang = []

def tambah_barang(id, nama, prioritas):
    barang = [id, nama, prioritas]
    if prioritas.lower() == "darurat":
        list_barang.insert(0, barang)
    elif prioritas.lower() == "biasa":
        mid = len(list_barang) // 2
        list_barang.insert(mid, barang)
    elif prioritas.lower() == "non-darurat":
        list_barang.append(barang)
    else:
        print("Mohon pilih salah satu dari prioritas di atas (darurat, biasa, non-darurat)")

def tampilkan_barang():
    if list_barang:
        print()
        print("◈ " * 10, end=" ")
        print(" Daftar Barang ", end=" ")
        print("◈ " * 10)
        for barang in list_barang:
            print(f"Id Barang: {barang[0]}, Nama Barang: {barang[1]}, Priorotas: {barang[2]}")
    else :
        print("Tidak ada barang yang terdaftar.")

while True:
    print("◈ PALAIS MEMORIA ◈")
    print()
    id = input("Masukkan ID Barang: ")
    nama = input("Masukkan Nama Barang: ")
    prioritas = input("Pilih tingkat prioritas (darurat, biasa, non-darurat): ")

    tambah_barang(id, nama, prioritas)

    tampilkan_barang()

    ulang = input("Apakah Anda ingin menambahkan barang lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Terima kasih dan sampai jumpa!")
        break
