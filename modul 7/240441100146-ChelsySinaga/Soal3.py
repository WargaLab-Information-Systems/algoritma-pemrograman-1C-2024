class Kelas:
    def __init__(self, nama_kelas):  # Menggunakan self untuk menyimpan nama sebagai atribut instance
        self.nama_kelas = nama_kelas
        self.siswa = []

    def tambah_siswa(self, nama, asal_sekolah):
        if len(self.siswa) < 3:
            self.siswa.append({"nama": nama, "asal_sekolah": asal_sekolah})
            print(f"Siswa {nama} berhasil ditambahkan ke kelas {self.nama_kelas}.")
        else:
            print(f"Kelas {self.nama_kelas} sudah penuh. Silakan buat kelas baru.")

    def tampilkan_siswa(self):
        print(f"\nDaftar siswa di kelas {self.nama_kelas}:")
        if not self.siswa:
            print("Kelas ini kosong.")
        for siswa in self.siswa:
            print(f"Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")

    def hapus_siswa(self, nama):
        for siswa in self.siswa:
            if siswa['nama'] == nama:
                self.siswa.remove(siswa)
                print(f"Siswa {nama} berhasil dihapus dari kelas {self.nama_kelas}.")
                return
        print(f"Siswa {nama} tidak ditemukan di kelas {self.nama_kelas}.")

    def update_siswa(self, nama, nama_baru, asal_sekolah_baru):
        for siswa in self.siswa:
            if siswa['nama'] == nama:
                siswa['nama'] = nama_baru
                siswa['asal_sekolah'] = asal_sekolah_baru
                print(f"Data siswa {nama} berhasil diupdate.")
                return
        print(f"Siswa {nama} tidak ditemukan di kelas {self.nama_kelas}.")

def main():
    kelas_list = []
    kelas_count = 1

    while True:
        print("\nMenu:")
        print("1. Tambah Siswa")
        print("2. Tampilkan Siswa")
        print("3. Hapus Siswa")
        print("4. Update Siswa")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah: ")

            # Cek apakah kelas pertama ada dan memiliki ruang
            if len(kelas_list) == 0 or len(kelas_list[0].siswa) == 3:
                # Kelas pertama penuh atau belum ada kelas
                if len(kelas_list) == 0 or len(kelas_list[-1].siswa) == 3:
                    kelas_baru = Kelas(f"Kelas {kelas_count}")
                    kelas_list.append(kelas_baru)
                    kelas_count += 1

            # Cek apakah kelas pertama memiliki ruang kosong, jika ya, tambahkan siswa ke kelas pertama
            if len(kelas_list[0].siswa) < 3:
                kelas_list[0].tambah_siswa(nama, asal_sekolah)
            else:
                # Jika kelas pertama penuh, tambah ke kelas terakhir
                kelas_list[-1].tambah_siswa(nama, asal_sekolah)

        elif pilihan == '2':
            if not kelas_list:
                print("Belum ada kelas yang dibuat.")
            else:
                for kelas in kelas_list:
                    kelas.tampilkan_siswa()

        elif pilihan == '3':
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            if not kelas_list:
                print("Belum ada kelas yang dibuat.")
            else:
                # Menghapus siswa hanya dari kelas pertama yang ditemukan
                for kelas in kelas_list:
                    kelas.hapus_siswa(nama)
                    break  # Hanya hapus sekali, keluar setelah berhasil

        elif pilihan == '4':
            nama = input("Masukkan nama siswa yang ingin diupdate: ")
            nama_baru = input("Masukkan nama baru siswa: ")
            asal_sekolah_baru = input("Masukkan asal sekolah baru: ")
            if not kelas_list:
                print("Belum ada kelas yang dibuat.")
            else:
                for kelas in kelas_list:
                    kelas.update_siswa(nama, nama_baru, asal_sekolah_baru)

        elif pilihan == '5':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()  # Untuk menjalankan seluruh program
