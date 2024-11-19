class Siswa:
    def __init__(self, nama, asal_sekolah):
        self.nama = nama
        self.asal_sekolah = asal_sekolah

    def __str__(self):
        return f"{self.nama} (Sekolah: {self.asal_sekolah})"


class BimbinganIntensif:
    def __init__(self):
        self.kelas = {"Kelas 1": []}

    def tambah_siswa(self, nama, asal_sekolah):
        siswa = Siswa(nama, asal_sekolah)
        
        # mencari kelas yang belum penuh
        for kelas, siswa_list in self.kelas.items():
            if len(siswa_list) < 3:
                siswa_list.append(siswa)
                print(f"Siswa {nama} ditambahkan ke {kelas}.")
                return
        
        # Jika semua kelas sudah penuh, maka kita membuat kelas baru
        kelas_baru = f"Kelas {len(self.kelas) + 1}"
        self.kelas[kelas_baru] = [siswa]
        print(f"Siswa {nama} ditambahkan ke {kelas_baru}.")

    def tampilkan_siswa(self):
        if not self.kelas:
            print("Tidak ada siswa yang terdaftar.")
            return
        
        for kelas, siswa_list in self.kelas.items():
            print(f"{kelas}: {', '.join(str(siswa) for siswa in siswa_list)}")

    def update_siswa(self, nama_lama, nama_baru, asal_sekolah_baru):
        for siswa_list in self.kelas.values():
            for siswa in siswa_list:
                if siswa.nama == nama_lama:
                    siswa.nama = nama_baru
                    siswa.asal_sekolah = asal_sekolah_baru
                    print(f"Data siswa {nama_lama} telah diperbarui menjadi {nama_baru}.")
                    return
        print(f"Siswa dengan nama {nama_lama} tidak ditemukan.")

    def hapus_siswa(self, nama):
        for kelas, siswa_list in self.kelas.items():
            for siswa in siswa_list:
                if siswa.nama == nama:
                    siswa_list.remove(siswa)
                    print(f"Siswa {nama} telah dihapus dari {kelas}.")
                    return
        print(f"Siswa dengan nama {nama} tidak ditemukan.")


def main():
    bimbingan_intensif = BimbinganIntensif()

    while True:
        print("\nMenu:\n1. Tambah Siswa\n2. Tampilkan Siswa\n3. Update Siswa\n4. Hapus Siswa\n5. Keluar")
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            nama = input("Masukkan nama siswa: ")
            asal_sekolah = input("Masukkan asal sekolah siswa: ")
            bimbingan_intensif.tambah_siswa(nama, asal_sekolah)
        elif pilihan == '2':
            bimbingan_intensif.tampilkan_siswa()
        elif pilihan == '3':
            nama_lama = input("Masukkan nama siswa yang ingin diupdate: ")
            nama_baru = input("Masukkan nama baru siswa: ")
            asal_sekolah_baru = input("Masukkan asal sekolah baru siswa: ")
            bimbingan_intensif.update_siswa(nama_lama, nama_baru, asal_sekolah_baru)
        elif pilihan == '4':
            nama = input("Masukkan nama siswa yang ingin dihapus: ")
            bimbingan_intensif.hapus_siswa(nama)
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

main()