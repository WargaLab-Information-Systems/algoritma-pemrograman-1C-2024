class KlubEkstrakurikuler:
    def __init__(self):
        self.klub = {"basket": set(), "renang": set()}

    def tambah_siswa(self, nama, klub):
        if klub in self.klub:
            self.klub[klub].add(nama)
            print(f"Siswa {nama} ditambahkan ke klub {klub}.")
        else:
            print("Klub tidak valid.")

    def tampilkan_siswa(self):
        for klub, siswa in self.klub.items():
            print(f"{klub.capitalize()}: {', '.join(siswa) or 'Tidak ada siswa'}")

    def siswa_kedua_klub(self):
        siswa_basket = self.klub["basket"]
        siswa_renang = self.klub["renang"]
        siswa_kedua_klub = siswa_basket.intersection(siswa_renang)
        return siswa_kedua_klub

    def siswa_hanya_satu_klub(self):
        siswa_basket = self.klub["basket"]
        siswa_renang = self.klub["renang"]
        siswa_hanya_satu = (siswa_basket.symmetric_difference(siswa_renang))
        return siswa_hanya_satu

    def semua_siswa_unik(self):
        semua_siswa = self.klub["basket"].union(self.klub["renang"])
        return semua_siswa

    def jumlah_siswa_unik(self):
        return len(self.semua_siswa_unik())

def main():
    klub_ekstrakurikuler = KlubEkstrakurikuler()

    while True:
        print("\nMenu:\n1. Tambah Siswa\n2. Tampilkan Siswa\n3. Siswa yang mengikuti kedua klub\n4. Siswa yang hanya mengikuti satu klub\n5. Semua siswa unik\n6. Jumlah siswa unik\n7. Keluar")
        pilihan = input("Pilih opsi (1-7): ")

        if pilihan == '1':
            nama = input("Masukkan nama siswa: ")
            klub = input("Masukkan klub (basket/renang): ").lower()
            klub_ekstrakurikuler.tambah_siswa(nama, klub)
        elif pilihan == '2':
            klub_ekstrakurikuler.tampilkan_siswa()
        elif pilihan == '3':
            siswa_kedua_klub = klub_ekstrakurikuler.siswa_kedua_klub()
            print(f"Siswa yang mengikuti kedua klub: {', '.join(siswa_kedua_klub) or 'Tidak ada siswa'}")
        elif pilihan == '4':
            siswa_hanya_satu = klub_ekstrakurikuler.siswa_hanya_satu_klub()
            print(f"Siswa yang hanya mengikuti satu klub: {', '.join(siswa_hanya_satu) or 'Tidak ada siswa'}")
        elif pilihan == '5':
            semua_siswa = klub_ekstrakurikuler.semua_siswa_unik()
            print(f"Semua siswa unik: {', '.join(semua_siswa) or 'Tidak ada siswa'}")
        elif pilihan == '6':
            jumlah_siswa = klub_ekstrakurikuler.jumlah_siswa_unik()
            print(f"Jumlah siswa unik: {jumlah_siswa}")
        elif pilihan == '7':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

main()