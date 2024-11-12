def main():
    karyawan_list = []  # list kosong untuk menyimpan data karyawan

    while True:  
        nip = input("\nInput NIP karyawan (ketik 'keluar' untuk berhenti): ")
        if nip.lower() == 'keluar':
            break
        
        if any(k[0] == nip for k in karyawan_list):        
            print("NIP sudah terdaftar, masukkan NIP yang lain.")
            continue  # Jika NIP sudah ada, lanjutkan ke input berikutnya
        
        nama = input("Nama: ")
        alamat = input("Alamat: ")
        departemen = input("Departemen: ")
        jabatan = input("Jabatan: ")
    
        karyawan_list.append((nip, nama, alamat, departemen, jabatan))

    print("\nData Karyawan yang Dimasukkan:")
    for k in karyawan_list:
        print(f"NIP: {k[0]}, Nama: {k[1]}, Alamat: {k[2]}, Departemen: {k[3]}, Jabatan: {k[4]}")

    # Pencarian berdasarkan kata kunci
    keyword = input("\nMasukkan kata kunci untuk pencarian: ")
    hasil_cari = [k for k in karyawan_list if keyword.lower() in map(str.lower, k)]  # map untuk pencarian case-insensitive
    
    if hasil_cari:
        print("\nHasil Pencarian:")
        for k in hasil_cari:
            print(f"NIP: {k[0]}, Nama: {k[1]}, Alamat: {k[2]}, Departemen: {k[3]}, Jabatan: {k[4]}")
    else:
        print("Tidak ada data yang ditemukan.")

# Program akan langsung memanggil fungsi main saat dijalankan
main()
