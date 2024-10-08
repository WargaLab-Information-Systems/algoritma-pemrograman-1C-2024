#perintah if-elif-else
# nilai = 60
# if nilai < 40:
#     print("remidi")
# elif nilai < 70:
#     print("rata-rata")
# elif nilai < 100 :
#     print("lulus")
# else :
#     print("tidak lulus")

#perintah if-else
# angka = 7
# if angka < 7 :
#     print("")

#if ternary
# number =20
# result = "genap" if number % 2 == 0 else"ganjil"
# print(result)

#program perintah if
# nama = "python"
# if nama == "python":
#     print ("hallo" + nama)

# kunci = "python"
# password = input ("masukkan password :")
# if password == kunci :
#     print("passwenar")
# else:
#    print("password salah")
   
# program perintah if- elif-else
# angka=int(input("masukkan sebuah bilangan"))
# if angka > 0 :
#     print ("angka merupakan bilangan positif")
# elif angka < 0 :
#     print ("angka merupakan bilangan negatif")
# else :
#     print ("angka merupakan 0")

# program if bersarang
# x = int (input("masukkan nilai x="))
# y = int (input("masukkan nilai y="))
# if x == y :
#     print("nilai", x ,"dan", y ,"mempunyai nilai yang sama")
# else :
#     if x > y :
#         print(x,"lebih besar dari",y)
#     if x < y :
#         print(x,"lebih kecil dari",y)

# a = 10
# b = 20
# # contoh mengembalikan nilai pada ternary
# opet = "opet harus belajar" if a < b else "opet tak perlu belajar"
# print (opet)

# a = 10
# b = 20
# print("doni anak baik"if a == b else "doni bukan anak yang baik")

# nomor_acak = 7
# print ('tebak nomor acak dari 1 - 10')
# tebakan = int(input('tebakan anda(bil bulat):'))
# if tebakan == nomor_acak:
#     print('selamat! tebakan anda benar')
#     print('tapi tidak ada hadiah untuk anda:(')
# elif tebakan < nomor_acak:
#     print('tebakan anda terlalu kecil')
# else :
#     print('tebakan anda terlalu besar')
#     print ('selesai')

# a=int(input("masukkan umur:"))
# if a <= 15 :
#     print("muda")
# elif a<=20 :
#     print("remaja")
# else :
#     print("tua")

#ganjil genap
# nilai= int(input("masukkan angka:"))
# if nilai %2 :
#     print("bilangan ganjil")
# else:
#     print("bilangan genap")
#angka ke kata
a=int(input("masukkan angka (0~9):"))
if a==0:
    print("angka anda nol")
elif a==1:
    print("angka anda satu")
elif a==2:
    print("angka anda dua")
elif a==3:
    print("angka anda tiga")
elif a==4:
    print("angka anda empat")
elif a==5:
    print("angka anda lima")
elif a==6:
    print("angka anda enam")
elif a==7:
    print("angka anda tujuh")
elif a==8:
    print("angka anda delapan")
elif a==9:
    print ("angka anda sembilan")
else :