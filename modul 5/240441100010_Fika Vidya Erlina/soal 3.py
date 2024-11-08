def hitung_faktorial(n):
    if n == 0:
        return 1, "1"
    
    hasil = 1
    langkah = ""
    
    # Mengalikan setiap angka dari n sampai 1
    for i in range(n, 0, -1):
        hasil *= i
        langkah += str(i) + " x " if i > 1 else str(i)
    
    return hasil, langkah

# Program utama
n = int(input("Masukkan bilangan: "))
faktorial, urutan_perkalian = hitung_faktorial(n)
print(f"{n}! = {urutan_perkalian} = {faktorial}")