def cek_palindrom(kata):
    # Membandingkan kata dengan kata yang dibalik
    return kata == kata[::-1]

# Program untuk menerima input dari pengguna
kata = input("Masukkan sebuah kata: ")
if cek_palindrom(kata):
    print(f"'{kata}' adalah palindrom.")
else:
    print(f"'{kata}' bukan palindrom.")
