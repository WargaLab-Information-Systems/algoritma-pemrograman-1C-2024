# program menentukan kata palindrom
def cek_palindrom(kata):
    # Menghapus spasi dan mengubah huruf menjadi kecil untuk perbandingan
    kata = kata.replace(" ", "").lower()
    
    # Membandingkan kata dengan kebalikannya
    return kata == kata[::-1]

kata_input = input("Masukkan kata: ")
if cek_palindrom(kata_input):
        print(f'Kata "{kata_input}" adalah kata palindrom')
else:
    print(f'Kata "{kata_input}" bukan kata palindrom')
