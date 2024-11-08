def cek_palindrom(kata):
    kata = kata.replace(" ", "")
    return kata == kata[::-1]
input_kata = str(input("Masukkan kata: "))
if cek_palindrom(input_kata):
    print(f"{input_kata} termasuk kata palindrom")
else:
    print(f"{input_kata} tidak termasuk kata palindrom")