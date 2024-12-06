angka = int(input("Masukkan angka bulat: "))

balik_angka = 0

while angka > 0:
    digit = angka % 10
    balik_angka = balik_angka * 10 + digit
    angka = angka // 10

print("Angka Sudarso setelah dibalik: ", balik_angka)