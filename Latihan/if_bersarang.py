# program if bersarang
x = int(input("Masukkan nilai x= "))
y = int(input("Masukkan nilai y= "))
if x == y:
    print("nilai", x ,"dan" ,y ,"mempunyai nilai yang sama")
else:
    if x > y :
        print(x, "Lebih besar dari", y)
    if x < y :
        print(x, "Lebih kecil dari", y)

a = 10
b = 20
#contoh mengembalikan nilai pada ternary
opet = “opet harus belajar” if a < b else “opet tak perlu belajar”
