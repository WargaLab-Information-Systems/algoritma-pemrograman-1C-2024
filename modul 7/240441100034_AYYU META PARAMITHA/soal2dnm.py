# Fungsi untuk mendapatkan input siswa yang mengikuti klub
def input_siswa(klub_name):
    print(f"Masukkan nama siswa yang mengikuti klub {klub_name}. Ketik 'selesai' untuk berhenti.")
    siswa_set = set()
    while True:
        siswa = input(f"Masukkan nama siswa untuk klub {klub_name}: ")
        if siswa.lower() == 'selesai':
            break
        siswa_set.add(siswa)
    return siswa_set

# Fungsi utama untuk menjalankan program
def main():
    # Input nama siswa yang mengikuti klub Basket dan Renang
    siswa_basket = input_siswa('Basket')
    siswa_renang = input_siswa('Renang')

    # a. Menampilkan dua set yang berisi nama siswa yang mengikuti klub Basket dan Renang
    print("\nDaftar siswa yang mengikuti klub Basket:", siswa_basket)
    print("Daftar siswa yang mengikuti klub Renang:", siswa_renang)

    # b. Daftar siswa yang mengikuti kedua klub (irisan antara dua set)
    siswa_kedua_klub = siswa_basket.intersection(siswa_renang)
    print("\nSiswa yang mengikuti kedua klub (Basket dan Renang):", siswa_kedua_klub)

    # c. Daftar siswa yang hanya mengikuti satu klub saja (selisih antara set)
    siswa_hanya_basket = siswa_basket - siswa_renang
    siswa_hanya_renang = siswa_renang - siswa_basket
    siswa_hanya_satu_klub = siswa_hanya_basket.union(siswa_hanya_renang)
    print("\nSiswa yang hanya mengikuti satu klub saja:", siswa_hanya_satu_klub)

    # d. Daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub (gabungan antara dua set)
    siswa_unik = siswa_basket.union(siswa_renang)
    print("\nSiswa unik yang mengikuti setidaknya satu klub (Basket atau Renang):", siswa_unik)

    # e. Jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub
    jumlah_siswa_unik = len(siswa_unik)
    print("\nJumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)

main()
