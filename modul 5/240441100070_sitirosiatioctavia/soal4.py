def cek_palindrom(kata):

    # Membandingkan kata dengan kata terbalik
    return kata == kata[::-1]

# Contoh penggunaan
# Meminta input dari pengguna
kata_input = input("Masukkan kata: ")

if cek_palindrom(kata_input):
    print(f'"{kata_input}" adalah palindrom.')
else:
    print(f'"{kata_input}" bukan palindrom.')
