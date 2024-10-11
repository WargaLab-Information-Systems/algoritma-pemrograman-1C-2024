suku5 = 11 
jml_8_12 = 52 

#menghitung selisih & menentukan suku pertama
selisih = (jml_8_12 - 2 * suku5) / 10
suku1 = suku5 - 4 * selisih

#menghitung jumlah nilai dari 8 suku pertama
n = 8 
jumlah = (n / 2) * (2 * suku1 + (n - 1) * selisih)

print("Jumlah 8 suku pertama adalah :", int(jumlah))


