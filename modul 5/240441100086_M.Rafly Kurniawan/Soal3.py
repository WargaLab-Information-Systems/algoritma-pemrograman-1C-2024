def hitung_faktorial(n, b):
    faktorial = 1 
    
    for i in range(n, 0, -1):
        faktorial = faktorial * i
        
    # Cetak hasil faktorial
    print(f"{n}! = {faktorial}")

# Meminta input dari pengguna
angka = int(input("Masukkan angka yang ingin difaktorialkan: "))
hitung_faktorial(angka)



