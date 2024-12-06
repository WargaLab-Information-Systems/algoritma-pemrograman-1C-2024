alat_kesehatan = {
                  'tekanan darah': 0,
                  'termometer': 0,
                  'stetoskop': 0,
                  'inhaler': 0
                  }

def pinjam_alat(hari):
  print(f"--- Peminjaman Hari ke-{hari + 1} ---")  
  alat_kesehatan['tekanan darah'] += int(input("Masukkan jumlah peminjaman alat pengukur tekanan darah: "))
  alat_kesehatan['termometer'] += int(input("Masukkan jumlah peminjaman termometer: "))
  alat_kesehatan['stetoskop'] += int(input("Masukkan jumlah peminjaman stetoskop: "))
  alat_kesehatan['inhaler'] += int(input("Masukkan jumlah peminjaman inhaler: "))

def pengembalian_alat(hari):
  print("--- Pengembalian ---")
  alat_kesehatan['tekanan darah'] -= int(input("Masukkan jumlah pengembalian alat pengukur tekanan darah: "))
  alat_kesehatan['termometer'] -= int(input("Masukkan jumlah pengembalian termometer: "))
  alat_kesehatan['stetoskop'] -= int(input("Masukkan jumlah pengembalian stetoskop: "))
  alat_kesehatan['inhaler'] -= int(input("Masukkan jumlah alat pengembalian inhaler: ")) 

def penukaran_alat():
    print("--- Penukaran Alat ---")
    alat_awal = input("Masukkan alat yang ingin ditukar (tekanan darah, termometer, stetoskop, inhaler): ").lower()
    alat_tujuan = input("Masukkan alat yang ingin ditukar menjadi (tekanan darah, termometer, stetoskop, inhaler): ").lower()
    jumlah_tukar = int(input("Masukkan jumlah alat yang ingin ditukar: "))

    if alat_awal not in alat_kesehatan or alat_tujuan not in alat_kesehatan:
        print("Nama alat tidak valid.")
        return
    if jumlah_tukar <= 0:
        print("Jumlah alat yang ditukar harus lebih dari 0.")
        return
    if alat_kesehatan[alat_awal] < jumlah_tukar:
        print("Stok alat yang ingin ditukar tidak mencukupi.")
        return
    alat_kesehatan[alat_awal] -= jumlah_tukar
    alat_kesehatan[alat_tujuan] += jumlah_tukar
    print(f"Berhasil menukar {jumlah_tukar} {alat_awal} menjadi {alat_tujuan}")

def menampilkan_alat():
  for alat, jumlah in alat_kesehatan.items():
    print(f" Heni meminjam {jumlah} {alat}")


hari = 0
while True:
  tambah = input(f"Apakah anda ingin menambah data untuk hari ke-{hari + 1} ?: ").lower()
  if tambah == 'ya':
    pinjam_alat(hari)
    pengembalian_alat(hari)
    penukaran_alat()
    hari += 1  
  else:
    menampilkan_alat()
    break