jaka_nama = "Jaka"
jaka_skor = 1100
jaka_ipk = 3.5

ida_nama = "Ida"
ida_skor = 1000
ida_ipk = 3.5

p_skor = 1100 
p_ipk = 3.0

print("Hasil Kelulusan Beasiswa:")

# JAKA
if jaka_skor > p_skor and jaka_ipk >= p_ipk:
    print(f"{jaka_nama} Lulus Persyaratan Beasiswa")

else:
    print(f"{jaka_nama} Tidak Lulus Persyaratan Beasiswa")

# IDA
if ida_skor > p_skor and ida_ipk >= p_ipk:
    print(f"{ida_nama} Lulus Persyaratan Beasiswa")
    
else:
    print(f"{ida_nama} Tidak Lulus Persyaratan Beasiswa")