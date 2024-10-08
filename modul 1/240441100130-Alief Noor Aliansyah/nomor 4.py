# soal nomer 4

n = 7 #semua orang
r = 4 #orang yang dipilih

# Menghitung kombinasi C(n, r)
# C(7, 4) = 7! / (4! * (7-4)!)
# = 7! / (4! * 3!)
# = (7 * 6 * 5 * 4 * 3 * 2 * 1) / (4 * 3 * 2 * 1) (3 * 2 * 1)

tujuh_faktorial = 7 * 6 * 5 * 4 * 3 * 2 * 1
empat_faktorial = 4 * 3 * 2 * 1
tiga_faktorial = 3 * 2 * 1

banyak_cara = tujuh_faktorial / (empat_faktorial * tiga_faktorial)
print("Jumlah cara membentuk tim", banyak_cara)
