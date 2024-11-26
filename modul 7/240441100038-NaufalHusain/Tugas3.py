# program untuk mengetahui data siswa yang ada di ploting bimbingan
class KelasBimbingan:
    # fungsi mendefinisikan init dengan parameter self, kelas
    def __init__(self, kelas):
        self.kelas = kelas
        self.siswa = []
        
    # membuat fungsi siswa dengan parameter self, nama, asal_sekolah untuk kondisi jika siswa kurang dari 3 maka menambahkan siswa dengan kelas yang sama
    def tambah_siswa(self, nama, asal_sekolah):
        if len(self.siswa) < 3:
            self.siswa.append({"nama": nama, "asal_sekolah": asal_sekolah})
        else:
            print(f"Kelas {self.kelas} sudah penuh, buat kelas baru.")

    def tampilkan_siswa(self):
        if len(self.siswa) == 0:
            print(f"Kelas {self.kelas} kosong.")
        else:
            print(f"Siswa di Kelas {self.kelas}:")
            for i, siswa in enumerate(self.siswa, 1):
                print(f"{i}. Nama: {siswa['nama']}, Asal Sekolah: {siswa['asal_sekolah']}")

    def update_siswa(self, old_nama, new_nama, new_asal_sekolah):
        for siswa in self.siswa:
            if siswa["nama"] == old_nama:
                siswa["nama"] = new_nama
                siswa["asal_sekolah"] = new_asal_sekolah
                print(f"Data siswa {old_nama} berhasil diupdate.")
                return
        print(f"Siswa dengan nama {old_nama} tidak ditemukan.")

    def delete_siswa(self, nama):
        for siswa in self.siswa:
            if siswa["nama"] == nama:
                self.siswa.remove(siswa)
                print(f"Siswa {nama} berhasil dihapus.")
                return
        print(f"Siswa dengan nama {nama} tidak ditemukan.")


class BimbinganIntensif:
    def __init__(self):
        self.kelas_list = []

    def tambah_kelas(self, kelas):
        self.kelas_list.append(KelasBimbingan(kelas))

    def cari_kelas(self, kelas):
        for k in self.kelas_list:
            if k.kelas == kelas:
                return k
        return None


# Program utama untuk mengelola data
def main():
    bimbingan = BimbinganIntensif()

    while True:
        print("\nMenu:")
        print("1. Tambah Kelas")
        print("2. Tambah Siswa")
        print("3. Tampilkan Siswa dalam Kelas")
        print("4. Update Data Siswa")
        print("5. Hapus Siswa")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            kelas = input("Masukkan nama kelas baru (misalnya: Kelas A, Kelas B): ")
            bimbingan.tambah_kelas(kelas)
            print(f"Kelas {kelas} berhasil dibuat.")

        elif pilihan == "2":
            kelas = input("Masukkan nama kelas tempat siswa akan dimasukkan: ")
            siswa_kelas = bimbingan.cari_kelas(kelas)
            if siswa_kelas:
                nama = input("Masukkan nama siswa: ")
                asal_sekolah = input("Masukkan asal sekolah siswa: ")
                siswa_kelas.tambah_siswa(nama, asal_sekolah)
            else:
                print(f"Kelas {kelas} tidak ditemukan.")

        elif pilihan == "3":
            kelas = input("Masukkan nama kelas untuk melihat daftar siswa: ")
            siswa_kelas = bimbingan.cari_kelas(kelas)
            if siswa_kelas:
                siswa_kelas.tampilkan_siswa()
            else:
                print(f"Kelas {kelas} tidak ditemukan.")

        elif pilihan == "4":
            kelas = input("Masukkan nama kelas tempat siswa akan diupdate: ")
            siswa_kelas = bimbingan.cari_kelas(kelas)
            if siswa_kelas:
                old_nama = input("Masukkan nama siswa yang ingin diupdate: ")
                new_nama = input("Masukkan nama baru siswa: ")
                new_asal_sekolah = input("Masukkan asal sekolah baru siswa: ")
                siswa_kelas.update_siswa(old_nama, new_nama, new_asal_sekolah)
            else:
                print(f"Kelas {kelas} tidak ditemukan.")

        elif pilihan == "5":
            kelas = input("Masukkan nama kelas tempat siswa akan dihapus: ")
            siswa_kelas = bimbingan.cari_kelas(kelas)
            if siswa_kelas:
                nama = input("Masukkan nama siswa yang ingin dihapus: ")
                siswa_kelas.delete_siswa(nama)
            else:
                print(f"Kelas {kelas} tidak ditemukan.")

        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

main()
