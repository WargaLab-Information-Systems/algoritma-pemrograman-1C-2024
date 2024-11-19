# Inisialisasi peralatan menggunakan dictionary
peralatan = {
    'Alat Pengukur Tekanan Darah': 2,
    'Termometer': 3,
    'Alat Pengukur Kadar Gula': 0,
    'Pengukur Tensi': 0
}

# Menggunakan set untuk menyimpan jenis peralatan yang dipinjam
peralatan_dipinjam = set()

# Menambahkan peralatan awal ke set
for alat, jumlah in peralatan.items():
    if jumlah > 0:
        peralatan_dipinjam.add(alat)

# Hari kedua: Meminjam 4 alat pengukur kadar gula darah
peralatan['Alat Pengukur Kadar Gula'] += 4
peralatan_dipinjam.add('Alat Pengukur Kadar Gula')

# Setelah seminggu:
# 1. Mengembalikan 1 alat pengukur tekanan darah dan 2 termometer
peralatan['Alat Pengukur Tekanan Darah'] -= 1
peralatan['Termometer'] -= 2

# 2. Menukar 3 alat pengukur tekanan darah dengan 2 pengukur tensi
peralatan['Alat Pengukur Tekanan Darah'] -= 3
peralatan['Pengukur Tensi'] += 2

# Update set peralatan yang dipinjam
peralatan_dipinjam = {alat for alat, jumlah in peralatan.items() if jumlah > 0}

# Menampilkan hasil akhir
print("Jumlah peralatan yang tersisa:")
for alat, jumlah in peralatan.items():
    print(f"{alat}: {jumlah}")

print("\nJenis peralatan yang masih dipinjam:")
for alat in peralatan_dipinjam:
    print(f"- {alat}")