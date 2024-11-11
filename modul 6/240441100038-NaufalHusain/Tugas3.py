# Program Pengelola Pengiriman Barang

# List untuk menyimpan data barang
data_barang = []

# Fungsi untuk menambahkan barang ke dalam list berdasarkan prioritas
def tambah_barang():
    
    nama_barang = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Masukkan Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ")

    # Data barang sebagai tuple
    barang = (nama_barang, id_barang, prioritas)

    # Menambahkan barang sesuai prioritas
    if prioritas == "Darurat":
        data_barang.insert(0, (nama_barang, id_barang, prioritas))
    elif prioritas == "Biasa":
        data_barang.insert(len(data_barang) // 2, (nama_barang, id_barang, prioritas))
    elif prioritas == "Non-Darurat":
        data_barang.append((nama_barang, id_barang, prioritas))
    else:
        print("Prioritas tidak valid. Barang tidak ditambahkan.")
        return

    print("Data barang berhasil ditambahkan!")

# Fungsi untuk menampilkan semua data barang
def lihat_barang():
    print("--- Daftar Data Barang ---")
    if len(data_barang) == 0:
        print("Belum ada data barang.")
    else:
        for barang in data_barang:
            print(f"Nama Barang: {barang[0]}, ID Barang: {barang[1]}, Prioritas: {barang[2]}")

# Fungsi utama untuk menjalankan program
def main():
    
    while True:
        tambah_barang()  # Tambah data barang baru
        lihat_barang()   # Tampilkan semua data barang

        # Tanya apakah ingin menambahkan data lagi
        lagi = input("Apakah ingin menambah barang lagi? (ya/tidak): ")
        if lagi != "ya":
            print("Keluar dari program.")
            break

# Menjalankan program
main()
