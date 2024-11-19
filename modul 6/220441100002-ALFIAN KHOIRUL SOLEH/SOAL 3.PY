# List untuk menyimpan daftar barang
daftar_barang = []

# Fungsi untuk menampilkan daftar barang
def tampilkan_daftar():
    print("\nDaftar Barang:")
    for barang in daftar_barang:
        print(f"Nama: {barang[0]}, ID: {barang[1]}, Prioritas: {barang[2]}")
    print()  # Line kosong untuk pemisah

while True:
    print("\nProgram Pengiriman Barang")
    
    # Input nama barang dan ID barang
    nama = input("Masukkan nama barang: ").strip()
    id_barang = input("Masukkan ID barang: ").strip()
    
    # Validasi agar nama dan ID barang tidak boleh kosong
    if not nama or not id_barang:
        print("Nama dan ID barang tidak boleh kosong. Silakan ulangi.")
        continue
    
    # Pilihan prioritas dengan validasi input
    print("\nPilih prioritas:")
    print("1. Darurat")
    print("2. Biasa")
    print("3. Non-Darurat")
    prioritas = input("Pilih (1-3): ").strip()
    
    # Validasi input prioritas agar hanya menerima pilihan 1, 2, atau 3
    if prioritas not in ["1", "2", "3"]:
        print("Input tidak valid. Silakan pilih prioritas 1, 2, atau 3.")
        continue
    
    # Konversi pilihan ke teks prioritas dan masukkan data ke daftar_barang
    if prioritas == "1":
        prioritas_text = "Darurat"
        daftar_barang.insert(0, [nama, id_barang, prioritas_text])
    elif prioritas == "2":
        prioritas_text = "Biasa"
        # Hitung posisi setelah item dengan prioritas "Darurat"
        pos = len([x for x in daftar_barang if x[2] == "Darurat"])
        daftar_barang.insert(pos, [nama, id_barang, prioritas_text])
    else:
        prioritas_text = "Non-Darurat"
        daftar_barang.append([nama, id_barang, prioritas_text])

    # Tampilkan daftar barang dengan memanggil fungsi tampilkan_daftar
    tampilkan_daftar()

    # Tanya user apakah ingin menambahkan barang lagi
    if input("\nTambah barang lagi? (y/t): ").strip().lower() != 'y':
        break

print("Program selesai!")
