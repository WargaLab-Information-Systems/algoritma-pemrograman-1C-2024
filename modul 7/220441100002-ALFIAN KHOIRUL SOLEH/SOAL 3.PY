
class DataSiswa:
    def __init__(self, nama, sekolah, kelas=None):
        self.nama = nama
        self.sekolah = sekolah
        self.kelas = kelas

class BimbinganGemaRipah:
    def __init__(self):
        self.siswa = []
        self.batas_siswa = 3
        
    def daftar_baru(self, nama, sekolah):
        # Hitung kelas berdasarkan jumlah siswa
        nomor_kelas = (len(self.siswa) // self.batas_siswa) + 1
        siswa_baru = DataSiswa(nama, sekolah, nomor_kelas)
        self.siswa.append(siswa_baru)
        print(f"\n[✓] Siswa {nama} masuk ke Kelas {nomor_kelas}")
        
    def tampilkan_semua(self):
        if not self.siswa:
            print("\n[!] Belum ada siswa terdaftar")
            return
            
        print("\n=== Daftar Siswa Bimbel Gema Ripah ===")
        kelas_aktif = 0
        for data in self.siswa:
            if data.kelas != kelas_aktif:
                kelas_aktif = data.kelas
                print(f"\nKelas {kelas_aktif}:")
            print(f"► {data.nama} - {data.sekolah}")
            
    def ubah_data(self, nama_cari, nama_baru, sekolah_baru):
        for data in self.siswa:
            if data.nama.lower() == nama_cari.lower():
                data.nama = nama_baru
                data.sekolah = sekolah_baru
                print(f"\n[✓] Data siswa berhasil diubah")
                return
        print("\n[!] Siswa tidak ditemukan")
        
    def keluar_bimbel(self, nama):
        for data in self.siswa:
            if data.nama.lower() == nama.lower():
                self.siswa.remove(data)
                print(f"\n[✓] Siswa {nama} telah keluar dari bimbel")
                # Atur ulang nomor kelas
                self._atur_kelas()
                return
        print("\n[!] Siswa tidak ditemukan")
        
    def _atur_kelas(self):
        for nomor, data in enumerate(self.siswa):
            data.kelas = (nomor // self.batas_siswa) + 1

def menu_utama():
    bimbel = BimbinganGemaRipah()
    
    while True:
        print("\n╔════ BIMBEL GEMA RIPAH ════╗")
        print("║ 1. Daftar Siswa Baru      ║")
        print("║ 2. Lihat Semua Siswa      ║")
        print("║ 3. Ubah Data Siswa        ║")
        print("║ 4. Keluarkan Siswa        ║")
        print("║ 5. Keluar Program         ║")
        print("╚══════════════════════════╝")
        
        pilih = input("\nPilih menu (1-5): ")
        
        if pilih == "1":
            nama = input("Masukkan nama siswa: ")
            sekolah = input("Masukkan asal sekolah: ")
            bimbel.daftar_baru(nama, sekolah)
            
        elif pilih == "2":
            bimbel.tampilkan_semua()
            
        elif pilih == "3":
            nama_cari = input("Masukkan nama siswa yang akan diubah: ")
            nama_baru = input("Masukkan nama baru: ")
            sekolah_baru = input("Masukkan sekolah baru: ")
            bimbel.ubah_data(nama_cari, nama_baru, sekolah_baru)
            
        elif pilih == "4":
            nama = input("Masukkan nama siswa yang akan dikeluarkan: ")
            bimbel.keluar_bimbel(nama)
            
        elif pilih == "5":
            print("\n[✓] Terima kasih telah menggunakan sistem Bimbel Gema Ripah")
            break
            
        else:
            print("\n[!] Menu tidak tersedia, silakan pilih 1-5")

if __name__ == "__main__":
    menu_utama()