def cek_palindrom(kata):
    return kata.lower() == kata[::-1].lower()
while True:
    kata_input = input("Masukkan kata yang ingin di cek: ")
    if cek_palindrom(kata_input):
        print(f'"{kata_input.lower()}" adalah palindrom.')
        break
    else:
        print(f'"{kata_input.lower()}" bukan palindrom. Silakan Coba lagi.')