angka = int(input("Masukkan angka: "))
angka_string = str(angka)  # Konversi angka ke string

# Membalik angka menggunakan for loop
angka_balik_string = angka_string [::-1] # Menambahkan karakter ke depan angka_balik_string

angka_balik = int(angka_balik_string)
print("Angka setelah dibalik:", angka_balik)