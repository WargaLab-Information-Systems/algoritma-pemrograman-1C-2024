#PROJECT AKHITR ARZHA, RIZKY 
import random
import string

print("=== Program Pengiriman Shopee ===")
print("Selamat datang di layanan pengiriman Shopee. Program ini memungkinkan Anda untuk mengelola pengiriman barang, menghitung biaya pengiriman, dan menambahkan garansi jika diperlukan Program dibuat oleh : Arzha Dwi A.A.W (2404411000621) dan Rizky Yudha P (240441100082).")

# Mendefinisikan biaya pengiriman per 1000 gram (1 kg)
biaya_per_1000_gram = {
    "JNT": 5000,  # Biaya pengiriman per 1000 gram untuk JNT
    "Shopee Express": 6000  # Biaya pengiriman per 1000 gram untuk Shopee Express
}

# Garansi untuk barang elektronik dan non-elektronik
garansi = {
    "elektronik": 15000,  # Garansi barang elektronik
    "non_elektronik": 10000  # Garansi barang non-elektronik
}

# Fungsi untuk menghitung biaya pengiriman berdasarkan berat barang
def hitung_biaya_pengiriman(berat_barang, jasa_pengiriman):
    if berat_barang <= 1000:
        biaya = biaya_per_1000_gram[jasa_pengiriman] 
    else:
        kelipatan_1000 = (berat_barang // 1000) * 1000
        if kelipatan_1000 < berat_barang:
            kelipatan_1000 += 1000  # Mengambil kelipatan berikutnya
        biaya = (kelipatan_1000 / 1000) * biaya_per_1000_gram[jasa_pengiriman]
    return biaya

# Fungsi untuk menanyakan apakah barang membutuhkan garansi
def tawarkan_garansi():
    while True:
        pilihan = input("Apakah Anda ingin menambah garansi? (ya/tidak): ").lower()
        if pilihan == 'ya':
            return True
        elif pilihan == 'tidak':
            return False
        else:
            print("Pilihan tidak valid. Harap masukkan 'ya' atau 'tidak'.")

# Fungsi untuk menanyakan tipe barang (elektronik atau non-elektronik)
def tipe_barang():
    while True:
        pilihan = input("Apakah barang Anda elektronik atau non-elektronik? ").lower()
        if pilihan == 'elektronik':
            return "elektronik"
        elif pilihan == 'non-elektronik':
            return "non_elektronik"
        else:
            print("Tipe barang tidak valid. Harap pilih antara 'elektronik' atau 'non-elektronik'.")

# Fungsi untuk membuat nomor resi acak
def generate_resi(jasa_pengiriman):
    if jasa_pengiriman == "JNT":
        awalan = "JNT"
    elif jasa_pengiriman == "Shopee Express":
        awalan = "SE"
    else:
        awalan = "UNK"
    resi_number = ''.join(random.choices(string.digits, k=6))
    return awalan + resi_number

# Fungsi untuk menambahkan pengiriman baru (Create)
def create_pengiriman(data_pengiriman):
    print("Menambahkan pengiriman baru...")
    while True:
        print("Pilih jasa pengiriman:")
        print("1. JNT\n2. Shopee Express")
        try:
            pilihan_pengiriman = int(input("Masukkan nomor jasa pengiriman (1/2): "))
            if pilihan_pengiriman == 1:
                jasa_pengiriman = "JNT"
                break
            elif pilihan_pengiriman == 2:
                jasa_pengiriman = "Shopee Express"
                break
            else:
                print("Pilihan tidak valid, harap masukkan angka 1 atau 2.")
        except ValueError:
            print("Masukkan angka yang valid (1 atau 2).")
    
    while True:
        try:
            berat_barang = float(input("Masukkan total berat paket dalam satuan gram: "))
            if berat_barang > 0:
                break
            else:
                print("Berat barang harus lebih dari 0 gram.")
        except ValueError:
            print("Masukkan angka yang valid untuk berat barang.")

    biaya = hitung_biaya_pengiriman(berat_barang, jasa_pengiriman)
    tipe = tipe_barang()
    biaya_garansi = garansi[tipe] if tawarkan_garansi() else 0
    total_biaya = biaya + biaya_garansi
    resi = generate_resi(jasa_pengiriman)
    
    pengiriman = (jasa_pengiriman, berat_barang, biaya, tipe, biaya_garansi, total_biaya, resi)
    data_pengiriman.append(pengiriman)
    print(f"Pengiriman berhasil ditambahkan dengan resi: {resi}")
    return data_pengiriman

# Fungsi untuk menampilkan semua data pengiriman (Read)
def read_pengiriman(data_pengiriman):
    if not data_pengiriman:
        print("Tidak ada data pengiriman.")
    else:
        print("\n" + "="*60)
        print(" " * 20 + "Daftar Pengiriman Shopee" + " " * 20)
        print("="*60)
        for i, pengiriman in enumerate(data_pengiriman, 1):
            jasa_pengiriman, berat_barang, biaya, tipe, biaya_garansi, total_biaya, resi = pengiriman
            print("="*60)
            print(f" Pengiriman {i}".center(60))
            print("-" * 60)
            print(f" Jasa Pengiriman   : {jasa_pengiriman}".ljust(30) + f": {jasa_pengiriman}")
            print(f" Berat Barang      : {berat_barang}g".ljust(30) + f": {berat_barang}g")
            print(f" Biaya Pengiriman  : Rp {biaya}".ljust(30) + f": Rp {biaya}")
            print(f" Tipe Barang       : {tipe}".ljust(30) + f": {tipe}")
            print(f" Biaya Garansi     : Rp {biaya_garansi}".ljust(30) + f": Rp {biaya_garansi}")
            print(f" Total Biaya       : Rp {total_biaya}".ljust(30) + f": Rp {total_biaya}")
            print(f" Resi             : {resi}".ljust(30) + f": {resi}")
            print("-" * 60)
        print("="*60)

# Fungsi untuk memperbarui data pengiriman (Update)
def update_pengiriman(data_pengiriman):
    read_pengiriman(data_pengiriman)
    while True:
        try:
            index = int(input("\nMasukkan nomor pengiriman yang ingin diperbarui: ")) - 1
            if 0 <= index < len(data_pengiriman):
                break
            else:
                print("Nomor pengiriman tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid.")
    
    print("Perbarui jasa pengiriman:")
    print("1. JNT\n2. Shopee Express")
    while True:
        try:
            pilihan_pengiriman = int(input("Masukkan nomor jasa pengiriman (1/2): "))
            if pilihan_pengiriman == 1:
                jasa_pengiriman = "JNT"
                break
            elif pilihan_pengiriman == 2:
                jasa_pengiriman = "Shopee Express"
                break
            else:
                print("Pilihan tidak valid, harap masukkan angka 1 atau 2.")
        except ValueError:
            print("Masukkan angka yang valid (1 atau 2).")
    
    while True:
        try:
            berat_barang = float(input("Masukkan berat barang dalam gram: "))
            if berat_barang > 0:
                break
            else:
                print("Berat barang harus lebih dari 0 gram.")
        except ValueError:
            print("Masukkan angka yang valid untuk berat barang.")
    
    biaya = hitung_biaya_pengiriman(berat_barang, jasa_pengiriman)
    tipe = tipe_barang()
    biaya_garansi = garansi[tipe] if tawarkan_garansi() else 0
    total_biaya = biaya + biaya_garansi
    resi = generate_resi(jasa_pengiriman)
    
    data_pengiriman[index] = (jasa_pengiriman, berat_barang, biaya, tipe, biaya_garansi, total_biaya, resi)
    print("Pengiriman berhasil diperbarui.")

# Fungsi untuk menghapus data pengiriman (Delete)
def delete_pengiriman(data_pengiriman):
    read_pengiriman(data_pengiriman)
    while True:
        try:
            index = int(input("\nMasukkan nomor pengiriman yang ingin dihapus: ")) - 1
            if 0 <= index < len(data_pengiriman):
                break
            else:
                print("Nomor pengiriman tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid.")
    
    del data_pengiriman[index]
    print("Pengiriman berhasil dihapus.")

# Fungsi utama untuk memilih menu CRUD dan menghitung biaya
def main():
    data_pengiriman = []  # List untuk menyimpan data pengiriman
    while True:
        print("\nMain Menu Pengiriman Shopee:")
        print("1. Tambah Pengiriman")
        print("2. Lihat Pengiriman")
        print("3. Perbarui Pengiriman")
        print("4. Hapus Pengiriman")
        print("5. Keluar")
        
        try:
            pilihan = int(input("Pilih menu (1-5): "))
            if pilihan == 1:
                data_pengiriman = create_pengiriman(data_pengiriman)
            elif pilihan == 2:
                read_pengiriman(data_pengiriman)
            elif pilihan == 3:
                update_pengiriman(data_pengiriman)
            elif pilihan == 4:
                delete_pengiriman(data_pengiriman)
            elif pilihan == 5:
                print("Terima kasih! Program selesai.")
                break
            else:
                print("Pilihan tidak valid. Harap masukkan angka antara 1 dan 5.")
        except ValueError:
            print("Masukkan angka yang valid.")
        
if __name__ == "__main__":
    main()
