# progam coba while
# contoh 1

x = "wulan"
while x :
    print (x)
x = x[1:]

# # contoh 2

a = 0
b = 10
while a < b :
    print (a)
a = a + b



# while a < b :
#     print  (a)
#     a = a = 1

# # program for
for a in range (1,5):
    print(a)

# a = 1
# while True :
#     if a >= 5:
#         break
#     print(a)
#     a =+ 1

T = [(1,2), (3,4), (5,6)]
for (a,b) in T :
    print (a,b)


nama = ["budi", "andi", "rudi", "sandi"]
usia = [20, 18, 22, 19]
for i in range (len(nama)) :
    print (nama[i], "berusia", usia[i], "tahun" )