# Program Pengelola Pengiriman Barang
def tampilkan_data(barang_list):
    print("\nDaftar Barang:")
    for barang in barang_list:
        print(f"ID: {barang['id']}, Nama: {barang['nama']}, Prioritas: {barang['prioritas']}")
    print("\n")

def tambah_barang(barang_list):
    # Input data barang
    nama = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    
    print("Pilih tingkat prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    
    pilihan = input("Masukkan pilihan (1/2/3): ")
    
    if pilihan == "1":
        prioritas = "Darurat"
        # Menambahkan barang di awal list , # untuk memasukkan item baru pada indeks 0
        barang_list.insert(0, {'nama': nama, 'id': id_barang, 'prioritas': prioritas})
    elif pilihan == "2":
        prioritas = "Biasa"
        # Menambahkan barang di tengah-tengah list
        tengah = len(barang_list) // 2  # untuk menghitung jumlah elemen dalam sebuah objek
        barang_list.insert(1, {'nama': nama, 'id': id_barang, 'prioritas': prioritas})
    elif pilihan == "3":
        prioritas = "Non-Darurat"
        # Menambahkan barang di akhir list
        barang_list.append({'nama': nama, 'id': id_barang, 'prioritas': prioritas})
    else:
        print("Pilihan tidak valid. Barang tidak ditambahkan.")
    
    tampilkan_data(barang_list)

# Program utama
def main():
    barang_list = []
    while True:
        tambah_barang(barang_list)
        ulang = input("Apakah ingin menambahkan barang lagi? (y/n): ")
        if ulang.lower() != 'y': # untuk mengubah semua huruf dalam sebuah teks menjadi huruf kecil
            break
    print("Program selesai. Terima kasih!")

# Menjalankan program
main() # fungsi utama untuk menjalankan program
