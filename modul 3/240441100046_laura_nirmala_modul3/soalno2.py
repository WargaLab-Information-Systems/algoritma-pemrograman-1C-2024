# membalik urutan dari sebuah bilangan bulat
angka = input("Masukkan angka bulat: ")

angka_balik = '' #angka_balik diinisialisasi sebagai string kosong (''). 
for digit in angka: # mengiterasi setiap digit
    angka_balik = digit + angka_balik

# hasil
print(f"Angka setelah dibalik: {angka_balik}")