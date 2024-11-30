alat = {
    1: "alat pengukur tekanan darah",
    2: "termometer",
    3: "stetoskop",
    4: "alat inhaler"
}

alat_dipinjam = {}
id_tersedia = set(range(1, 100))

def buat_id():
    return id_tersedia.pop() if id_tersedia else None

def hapus_id(id_peminjam):
    id_tersedia.add(id_peminjam)

def daftar_alat():
    print("\n◆ ◆ Daftar Alat Kesehatan ◆ ◆")
    for kode, nama in alat.items():
        print(f"{kode}. {nama}")

def tampilkan_peminjaman():
    if alat_dipinjam:
        print("\n◇ Alat yang Sedang Dipinjam ◇")
        for id_peminjam, info in alat_dipinjam.items():
            print(f"ID: {id_peminjam}, Nama: {info['nama']}, Alat Dipinjam: {info['alat']}")
    else:
        print("\n ... Tidak ada alat yang sedang dipinjam.")
def tampilkan_jumlah_alat():
    print("\n◆ ◆ Jumlah Total Alat yang Dipinjam ◆ ◆")
    jumlah_alat = {}

    for data in alat_dipinjam.values():
        for nama_alat, jumlah in data["alat"].items():
            if nama_alat in jumlah_alat:
                jumlah_alat[nama_alat] += jumlah
            else:
                jumlah_alat[nama_alat] = jumlah

    if jumlah_alat:
        for nama_alat, total in jumlah_alat.items():
            print(f"{nama_alat}: {total}")
    else:
        print("Tidak ada alat yang sedang dipinjam.\n")

while True:
    print("\n◇ ◇ ◇ Menu ◇ ◇ ◇")
    print("1. Daftar Alat Kesehatan")
    print("2. Pinjam Alat")
    print("3. Kembalikan Alat")
    print("4. Tukar Alat")
    print("5. Total Alat yang Dipinjam")
    print("0. Keluar")

    pilihan = input("Pilih Menu: ")

    if pilihan == '1':
        daftar_alat()

    elif pilihan == '2':
        print("\n◇ ◇ ◇ Peminjaman Alat ◇ ◇ ◇")
        id_peminjam = buat_id()
        if id_peminjam is None:
            print("Maaf, ID tidak lagi tersedia")
            continue
        nama_peminjam = input("Masukkan Nama Peminjam: ")
        if not nama_peminjam:
            print("Nama tidak boleh kosong.")
            hapus_id(id_peminjam)
            continue

        alat_dipinjam[id_peminjam] = {"nama": nama_peminjam, "alat": {}}

        jumlah_items = int(input("Berapa banyak jenis alat yang ingin dipinjam? "))
        for _ in range(jumlah_items):
            kode = int(input("Masukkan kode alat yang ingin dipinjam: "))
            if kode in alat:
                jumlah = int(input(f"Masukkan Jumlah {alat[kode]} yang ingin dipinjam: "))
                alat_dipinjam[id_peminjam]["alat"][alat[kode]] = jumlah
                print(f"{alat[kode]} berhasil dipinjam sebanyak {jumlah}.\n")
        print(f"ID: {id_peminjam} - Peminjaman berhasil oleh {nama_peminjam}.\n")

    elif pilihan == '3':
        print("\n◇ ◇ ◇ Pengembalian Alat ◇ ◇ ◇")
        tampilkan_peminjaman()
        id_peminjam = int(input("Masukkan ID Peminjaman: "))
        if id_peminjam not in alat_dipinjam:
            print("ID tidak ditemukan.")
            continue

        kode = int(input("Masukkan kode alat yang ingin dikembalikan: "))
        if kode in alat and alat[kode] in alat_dipinjam[id_peminjam]["alat"]:
            jumlah = int(input(f"Masukkan Jumlah {alat[kode]} yang dikembalikan: "))
            alat_dipinjam[id_peminjam]["alat"][alat[kode]] -= jumlah
            
            if alat_dipinjam[id_peminjam]["alat"][alat[kode]] <= 0:
                alat_dipinjam[id_peminjam]["alat"].pop(alat[kode])  
            
            if not alat_dipinjam[id_peminjam]["alat"]:
                hapus_id(id_peminjam)
                alat_dipinjam.pop(id_peminjam)
                print("Semua alat telah dikembalikan.")
            else:
                print("Sebagian alat masih dipinjam.")

    elif pilihan == '4':
        print("\n◇ Penukaran Alat ◇ ")
        tampilkan_peminjaman()
        id_peminjam = int(input("Masukkan ID Peminjaman: "))
        if id_peminjam in alat_dipinjam:
            kode_tukar = int(input("Masukkan kode alat yang ingin ditukar: "))
            if kode_tukar in alat:
                jumlah_tukar = int(input(f"Masukkan jumlah {alat[kode_tukar]} yang ditukar: "))
                kode_alat_baru = int(input("Masukkan kode alat baru yang diterima: "))
                if kode_alat_baru in alat:
                    jumlah_baru = int(input(f"Masukkan jumlah {alat[kode_alat_baru]} yang diterima: "))
                    alat_dipinjam[id_peminjam]["alat"][alat[kode_tukar]] -= jumlah_tukar
                    if alat_dipinjam[id_peminjam]["alat"][alat[kode_tukar]] <= 0:
                        alat_dipinjam[id_peminjam]["alat"].pop(alat[kode_tukar])
                    alat_dipinjam[id_peminjam]["alat"][alat[kode_alat_baru]] = jumlah_baru
                    print(f"{alat[kode_tukar]} ditukarkan dengan {alat[kode_alat_baru]}.\n")

    elif pilihan == '5':
        tampilkan_jumlah_alat()

    elif pilihan == '0':
        print("Keluar dari program")
        break
    else:
        print("Pilihan tidak valid, mohon memilih salah satu menu di atas.")

# hari pertama
# 2 pengukur tekanan darah
# 3 termometer

# hsri kedua
# 4 stetoskop

# a week 
# mengembalikan:
# 1 pengukur tekanan darah
# 2 termometer

# menukar:
# 3 stetoskop ke 2 inhaler