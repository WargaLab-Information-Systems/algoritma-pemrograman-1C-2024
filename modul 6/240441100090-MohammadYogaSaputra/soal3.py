prioritas_barang = []

def tambah_barang():
    # Meminta input nama barang dan ID barang
    nama = input("Masukkan nama barang: ").strip()
    while not nama:
        nama = input("Nama barang tidak boleh kosong, masukkan nama barang: ").strip()

    id_barang = input("Masukkan ID barang: ").strip()
    while not id_barang:
        id_barang = input("ID barang tidak boleh kosong, masukkan ID barang: ").strip()

    # Meminta input prioritas dengan opsi yang tersedia
    print("Tingkat prioritas barang:\n1. Darurat\n2. Biasa\n3. Non-Darurat")
    prioritas_opsi = {"1": "Darurat", "2": "Biasa", "3": "Non-Darurat"}
    prioritas = prioritas_opsi.get(input("Masukkan tingkat prioritas barang: "))
    
    if prioritas:
        prioritas_barang.append((nama, id_barang, prioritas))
        print(f"Barang '{nama}' dengan prioritas '{prioritas}' telah ditambahkan.")
    else:
        print("Input tidak valid. Masukkan nomor 1, 2, atau 3.")

def menampilkan():
    sorted_list = sorted(prioritas_barang, key=lambda x: {"Darurat": 1, "Biasa": 2, "Non-Darurat": 3}[x[2]])
    print("\nDaftar prioritas barang:")
    for i, barang in enumerate(sorted_list, 1):
        print(f"{i}. Nama barang: {barang[0]}, ID barang: {barang[1]}, Prioritas: {barang[2]}")

def main():
    while True:
        print("\n=== PROGRAM DAFTAR BARANG BERDASARKAN PRIORITAS ===")
        print("1. Tambah barang\n2. Tampilkan list barang\n3. Keluar dari program")
        pilihan = input("Pilih salah satu dari menu di atas: ")
        
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            menampilkan()
        elif pilihan == "3":
            print("Program berakhir.")
            break
        else:
            print("Input tidak valid, harap masukkan opsi yang tersedia.")
main()
