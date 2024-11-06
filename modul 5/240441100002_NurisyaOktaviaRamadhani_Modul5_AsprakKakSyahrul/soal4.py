def cek_palindrom(kata):
    kata = kata
    return kata == kata[::-1]
kata_input = input("Masukkan kata untuk dicek apakah palindrom atau tidak: ")
if cek_palindrom(kata_input):
    print(f"{kata_input} True.")
else:
    print(f"{kata_input} False.")