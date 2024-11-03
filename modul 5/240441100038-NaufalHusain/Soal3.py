# program menentukan faktorial
def faktorial(n): 
    if n == 0 or n == 1:
        return 1
    else:   
        return n * faktorial(n - 1)

while True:
    bilangan = int(input("Masukkan bilangan: "))
    if bilangan < 0:
        print(f"Faktorial dari {bilangan} tidak dapat dihitung. Silakan coba lagi.")
    else:
        print(f"Faktorial dari {bilangan} adalah ", end="")
        
        # Mencetak urutan dari 1 hingga bilangan
        for i in range(1, bilangan + 1):
            if i == bilangan:
                print(i, end=" ")
            else:
                print(i, end=" x ")

        # Menghitung hasil faktorial
        hasil_faktorial = faktorial(bilangan)
        
        print(f"= {hasil_faktorial}")
        break