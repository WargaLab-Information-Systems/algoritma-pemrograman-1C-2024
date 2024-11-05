# Input angka
angka = input("Masukkan angka bulat: ")

angka_terbalik = ""

for char in angka:
    angka_terbalik = char + angka_terbalik

print("Angka setelah dibalik:", angka_terbalik)
