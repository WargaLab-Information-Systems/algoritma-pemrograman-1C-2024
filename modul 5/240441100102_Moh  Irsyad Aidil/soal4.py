def cek_palindrom(kata):
    # Membandingkan kata dengan kebalikannya
    return kata == kata[::-1]

kota = input("Masukkan kata: ")
if cek_palindrom(kota):
    print(f"{kota} adalah palindrom")
else:
    print(f"{kota} bukan palindrom")
    print(f"{kota[::-1]}")

