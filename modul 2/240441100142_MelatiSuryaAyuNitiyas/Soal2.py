# Data Jaka
jaka_skor = 1100
jaka_ipk = 3.5

# Data Ida
ida_skor = 1000
ida_ipk = 3.5

#input
jaka_skor = int(input("memasukkan jaka_skor: "))
jaka_ipk = float(input("memasukkan jaka_ipk: "))
ida_skor = int(input("memasukkan ida_skor: "))
ida_ipk = float(input("memasukkan ida_ipk: "))

# Kriteria Beasiswa
skor_minimal = 1100
ipk_minimal = 3.0

# Jaka
if jaka_skor >= skor_minimal and jaka_ipk >= ipk_minimal:
    print("Jaka memenuhi syarat beasiswa")
else:
    print("Jaka tidak memenuhi syarat beasiswa")

# Ida
if ida_skor >= skor_minimal and ida_ipk >= ipk_minimal:
    print("Ida memenuhi syarat beasiswa")
else:
    print("Ida tidak memenuhi syarat beasiswa")