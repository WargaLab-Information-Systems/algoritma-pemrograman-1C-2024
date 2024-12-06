nama = input("Masukkan Nama ")
nim = int(input("Masukkan NIM "))
n_uts = int(input("Masukkan Nilai UTS: "))
n_uas = int(input("Masukkan Nilai UAS: "))

n_rerata = (n_uts + n_uas) / 2

print("Nama: ", nama)
print("NIM Anda: ", nim)
print("Nilai Rata-Rata Anda ", n_rerata)


if n_rerata > 80 and n_rerata <= 100 :
    print("Anda Mendapatkan Nilai A")

elif n_rerata > 70 and n_rerata <= 80 :
    print("Anda Mendapatkan Nilai B")

elif n_rerata > 60 and n_rerata <= 70 :
    print("Anda Mendapatkan Nilai C")

elif n_rerata > 40 and n_rerata <= 60 :
    print("Anda Mendapatkan Nilai D")

elif n_rerata >= 0 and n_rerata < 41:
    print("Anda Mendapatkan Nilai E")
    
else:
    print("Nilai tidak valid!")


