def cek_palindrom(kata):
    # Ubah kata menjadi huruf kecil 
    kata = kata.lower()
    # Balik kata menggunakan slicing
    kata_terbalik = kata[::-1]
    # Periksa apakah kata asli sama dengan kata yang dibalik
    return kata == kata_terbalik

# Meminta input dari pengguna
kata_input = input("Masukkan sebuah kata untuk dicek apakah itu palindrom: ")

# Memanggil fungsi dan mencetak hasil
if cek_palindrom(kata_input):
    print(f"'{kata_input}' adalah palindrom.")
else:
    print(f"'{kata_input}' bukan palindrom.")
