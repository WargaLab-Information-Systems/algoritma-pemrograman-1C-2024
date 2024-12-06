def faktorial(n):
    if n == 0:
        return 
    else:
        hasil = n
        proses = f"{n}"
        for i in range(n - 1, 0, -1):
            hasil *= i
            proses += f" x {i}" #
        print(f"{n}! = {proses} = {hasil}") #menampilkan
        return hasil

angka = int(input("Masukkan angka: "))  
hasil_faktorial = faktorial(angka)
print("Faktorialnya adalah :", hasil_faktorial)