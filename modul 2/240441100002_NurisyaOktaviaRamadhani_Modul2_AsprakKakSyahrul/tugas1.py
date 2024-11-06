
angka = float(input("Masukkan angka: "))

if 81 <= angka <= 100:
        nilai = "A"
elif 71 <= angka <= 80:
        nilai = "B"
elif 61 <= angka <= 70:
        nilai = "C"
elif 41 <= angka <= 60:
        nilai = "D"
elif 0 <= angka <= 40:
        nilai = "E"
else:
        nilai = "angka tidak valid"

print(f"nilai anda: {nilai}")