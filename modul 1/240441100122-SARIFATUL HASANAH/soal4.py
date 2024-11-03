n = 7
k = 4

faktorial_n = 7 * 6 * 5 * 4 * 3 * 2 * 1 #5040

faktorial_k = 4 * 3 * 2 * 1 #24

#menghitung faktorial n-k = 3
faktorial_nk = 3 * 2 * 1 #6

kombinasi = faktorial_n / (faktorial_k * faktorial_nk) #5040 / 144

print("Total cara membentuk tim Darsono : ", int(kombinasi))
