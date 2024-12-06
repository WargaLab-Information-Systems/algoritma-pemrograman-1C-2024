class SistemPeminjamanAlat:
    def __init__(self):
        self.alat_kesehatan = {}
    
    def tambah_alat(self):
        print("\n=== Peminjaman Alat ===")
        while True:
            nama_alat = input("Masukkan nama alat (atau 'selesai' untuk mengakhiri): ").lower()
            if nama_alat == 'selesai':
                break
                
            try:
                jumlah = int(input(f"Masukkan jumlah {nama_alat} yang dipinjam: "))
                if jumlah <= 0:
                    print("Jumlah yang diinput tidak valid")
                    continue
                    
                if nama_alat in self.alat_kesehatan:
                    self.alat_kesehatan[nama_alat] += jumlah
                else:
                    self.alat_kesehatan[nama_alat] = jumlah
                print(f"{nama_alat} sejumlah {jumlah} berhasil ditambahkan")
            except ValueError:
                print("Mohon masukkan angka yang valid!")
    
    def kembalikan_alat(self):
        if not self.alat_kesehatan:
            print("\nTidak ada alat yang dipinjam")
            return
            
        print("\n=== Pengembalian Alat ===")
        self.tampilkan_alat()
        while True:
            nama_alat = input("Masukkan nama alat yang akan dikembalikan (atau 'selesai' untuk mengakhiri): ").lower()
            if nama_alat == 'selesai':
                break
                
            if nama_alat not in self.alat_kesehatan:
                print("Alat tersebut tidak ada dalam daftar peminjaman!")
                continue
                
            try:
                jumlah = int(input(f"Masukkan jumlah {nama_alat} yang dikembalikan: "))
                if jumlah <= 0:
                    print("Jumlah yang diinput tidak valid!")
                    continue
                    
                if jumlah > self.alat_kesehatan[nama_alat]:
                    print(f"Jumlah pengembalian melebihi jumlah yang dipinjam ({self.alat_kesehatan[nama_alat]})!")
                    continue
                    
                self.alat_kesehatan[nama_alat] -= jumlah
                if self.alat_kesehatan[nama_alat] == 0:
                    del self.alat_kesehatan[nama_alat]
                print(f"{nama_alat} sejumlah {jumlah} berhasil dikembalikan")
            except ValueError:
                print("Mohon masukkan angka yang valid!")
    
    def tukar_alat(self):
        if not self.alat_kesehatan:
            print("\nTidak ada alat yang dipinjam")
            return
            
        print("\n=== Penukaran Alat ===")
        self.tampilkan_alat()
        
        # Alat yang ditukar
        nama_alat_lama = input("Masukkan nama alat yang akan ditukar: ").lower()
        if nama_alat_lama not in self.alat_kesehatan:
            print("Alat tersebut tidak ada dalam daftar peminjaman!")
            return
            
        try:
            jumlah_ditukar = int(input(f"Masukkan jumlah {nama_alat_lama} yang ditukar: "))
            if jumlah_ditukar > self.alat_kesehatan[nama_alat_lama]:
                print(f"Jumlah penukaran melebihi jumlah yang dipinjam ({self.alat_kesehatan[nama_alat_lama]})!")
                return
                
            # Alat pengganti
            nama_alat_baru = input("Masukkan nama alat pengganti: ").lower()
            jumlah_baru = int(input(f"Masukkan jumlah {nama_alat_baru} yang diterima: "))
            
            # Proses penukaran
            self.alat_kesehatan[nama_alat_lama] -= jumlah_ditukar
            if self.alat_kesehatan[nama_alat_lama] == 0:
                del self.alat_kesehatan[nama_alat_lama]
                
            if nama_alat_baru in self.alat_kesehatan:
                self.alat_kesehatan[nama_alat_baru] += jumlah_baru
            else:
                self.alat_kesehatan[nama_alat_baru] = jumlah_baru
                
            print(f"Penukaran berhasil: {jumlah_ditukar} {nama_alat_lama} ditukar dengan {jumlah_baru} {nama_alat_baru}")
        except ValueError:
            print("Mohon masukkan angka yang valid!")
    
    def tampilkan_alat(self):
        print("\n=== Daftar Alat yang Dipinjam ===")
        if not self.alat_kesehatan:
            print("Tidak ada alat yang dipinjam")
            return
            
        for alat, jumlah in self.alat_kesehatan.items():
            if jumlah > 0:
                print(f"- {alat}: {jumlah} buah")

# Program utama
def main():
    sistem = SistemPeminjamanAlat()
    
    while True:
        print("\n=== SISTEM PEMINJAMAN ALAT KESEHATAN ===")
        print("1. Pinjam Alat")
        print("2. Kembalikan Alat")
        print("3. Tukar Alat")
        print("4. Lihat Daftar Alat")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            sistem.tambah_alat()
        elif pilihan == '2':
            sistem.kembalikan_alat()
        elif pilihan == '3':
            sistem.tukar_alat()
        elif pilihan == '4':
            sistem.tampilkan_alat()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem peminjaman alat kesehatan!")
            break
        else:
            print("Pilihan tidak valid!")

main()