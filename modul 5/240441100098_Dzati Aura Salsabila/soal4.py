def cek_palindrom(kata):
    # Membandingkan kata dengan kebalikannya
     kata == kata[::-1]

# Contoh penggunaan
kata = input("Masukkan kata: ")
if cek_palindrom(kata):
    print(f"{kata} adalah palindrom")
else:
    print(f"{kata} bukan palindrom")
cek_palindrom(kata)