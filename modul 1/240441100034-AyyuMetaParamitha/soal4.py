# import math

# total_orang = 7
# tim = 4
 
# kombinasi = math.comb(total_orang, tim)
# print(f"Banyaknya cara untuk memilih 4 dari 7 orang adalah: {kombinasi} cara")
 

# jumlah total orang
n = 7

# jumlah tim
r = 4 

# faktorial 7
faktorial_7 = 7*6*5*4*3*2*1

# faktorial 4
faktorial_4 = 4*3*2*1

# faktorial dari (n-r) = 3
faktorial_3 = 3*2*1

# rumus (n,r) = n!(r!*(n-r)!)
(total_cara) = (faktorial_7)/(faktorial_4*faktorial_3)
print(total_cara)