class AlatKesehatan:
    def __init__(self):
        self.alat = {}  # Dictionary untuk menyimpan jumlah alat yang dipinjam
        self.jenis_alat = set()  # Set untuk menyimpan jenis alat yang dipinjam

    def pinjam_alat(self, jenis, jumlah):
        self.alat[jenis] = self.alat.get(jenis, 0) + jumlah
        self.jenis_alat.add(jenis)
        print(f"{jumlah} {jenis} dipinjam.")

    def kembalikan_alat(self, jenis, jumlah):
        if jenis in self.alat and self.alat[jenis] >= jumlah:
            self.alat[jenis] -= jumlah
            print(f"{jumlah} {jenis} dikembalikan.")
            if self.alat[jenis] == 0:  # Jika jumlahnya menjadi 0, di hapus dari dictionary
                del self.alat[jenis]
                self.jenis_alat.discard(jenis)  # Menghapus dari set jika alat sudah tidak ada
        else:
            print("Jumlah tidak valid.")

    def tukar_alat(self, jenis_tukar, jumlah_tukar):
        if jenis_tukar in self.alat and self.alat[jenis_tukar] >= jumlah_tukar:
            self.alat[jenis_tukar] -= jumlah_tukar
            print(f"{jumlah_tukar} {jenis_tukar} ditukar.")
            if self.alat[jenis_tukar] == 0:
                del self.alat[jenis_tukar]
                self.jenis_alat.discard(jenis_tukar)  # Menghapus dari set jika alat sudah tidak ada
        else:
            print("Jumlah tidak valid untuk ditukar.")

    def tampilkan_alat(self):
        print("\nAlat yang dipinjam:")
        if not self.alat:
            print("Tidak ada alat yang dipinjam.")
        else:
            for jenis, jumlah in self.alat.items():
                print(f"{jenis}: {jumlah}")

def main():
    alat_kesehatan = AlatKesehatan()

    while True:
        print("\nMenu:\n1. Pinjam Alat\n2. Kembalikan Alat\n3. Tukar Alat\n4. Tampilkan Alat\n5. Keluar")
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            jenis = input("Jenis alat: ")
            jumlah = int(input("Jumlah: "))
            alat_kesehatan.pinjam_alat(jenis, jumlah)
        elif pilihan == '2':
            jenis = input("Jenis alat: ")
            jumlah = int(input("Jumlah: "))
            alat_kesehatan.kembalikan_alat(jenis, jumlah)
        elif pilihan == '3':
            jenis_tukar = input("Jenis alat yang ingin ditukar: ")
            jumlah_tukar = int(input("Jumlah: "))
            alat_kesehatan.tukar_alat(jenis_tukar, jumlah_tukar)
        elif pilihan == '4':
            alat_kesehatan.tampilkan_alat()
        elif pilihan == '5':
            print("Keluar.")
            break
        else:
            print("Pilihan tidak valid.")

main()