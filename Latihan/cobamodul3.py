#ini ubtuk coba while

# x = "wulan"
# while x :
#     print (x)
#     x = x[1 :]

# #contoh 2
# a = 0
# b = 10

# while a < b :
#     print (a)
#     a = a + 1

#coba for 
# for a in range (1,5):
#     print(a)
#     pass

# a = 1
# while True :
#     if a >= 5:
#         break
#     print(a)
#     a += 1

#coba for tanpa
# a = 1
# while a < 5 :
#     print (a)
#     a += 1


#contoh break
x = 4
while x < 5 :
    if x == 3 :
        break 
    print(x)
    x = x + 1

else :
    print("Loop sudah selesai dikerjakan")

#coba continue
n = 10
while n :
    n = n - 1
    if n % 2 != 0:
     continue
print(n)

# for i in [5, 4, 3, 2, 1]:
#     print(i)

# T = [(1, 2), (3, 4), (5, 6)]
# for (a, b) in T:
#     print(a, b)

# nama = ['budi', 'andi', 'rudi', 'sandi']
# usia = [20, 18, 22, 19]

# for i in range(len(nama)):
#     print(nama[i], 'berusia', usia[i], 'tahun')

#Program tidak akan melakukan
# #proses looping
# # while True : pass
# while True : pass 


# a = 1
# while a < 5:
#     print(a)
#     a = a + 1

# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 1:
#         print(a, "adalah bilangan ganjil")
#     else:
#         continue


# a = 1
# while a < 10:
#     print(a)
#     a = a + 1
#     if a > 6:
#         break

# while 1:
#     print("Perulangan tiada batas, tekan 'Ctrl+C' untuk berhenti")

bulan = {'1': 'januari', '2': 'februari', '3': 'maret', '4': 'april', '5': 'mei'}
for a in bulan.values():
    print(a)