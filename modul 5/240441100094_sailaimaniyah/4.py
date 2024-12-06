def cek_palindrom(kata):
    # Membandingkan kata dengan kebalikannya
    return kata == kata[::-1]

kata = input("Masukkan kata: ")
if cek_palindrom(kata):
    print(kata,"adalah palindrom")
else:
    print(kata,"bukan palindrom")