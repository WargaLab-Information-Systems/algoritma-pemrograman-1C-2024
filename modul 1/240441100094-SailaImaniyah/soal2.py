#  ingin mengetahui jumlah nilai (n) dari suku ke 8
# diketahui 
# u5 = 11
# u8 & u12 = 52
# suku u5 = a + 4b =11
# suku u8&u12 = 2a + 18b =52
# kedua suku tsb disubstitusikan mendapatkan hasil 
a = -1
b = 3
n = 8
# menghitung jumlah suku
sn = n / 2 * (2*a + (n-1) *b)
print ("jumlah suku ke 8 adalah"+str(sn))