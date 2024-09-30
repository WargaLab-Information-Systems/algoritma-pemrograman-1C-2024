import math
# menggunakan rumus kombinasi C(n, r) = n!/ (r! * (n - r) !)

n = 7 # total orang
r = 4 # jumlah orang dalam tim


jumlah_cara = math.comb (n , r)

print(F"jumlah cara membentuk tim:{jumlah_cara}")