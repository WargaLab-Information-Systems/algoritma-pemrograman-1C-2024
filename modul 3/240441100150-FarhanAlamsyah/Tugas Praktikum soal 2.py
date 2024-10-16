angka = input("Masukkan angka bulat: ")
if angka.isdigit():
    angka_balik = str(angka)[::-1]
    print(f"Angka setelah dibalik: {angka_balik}")
else:
    print("hanya bisa bilangan bulat")