n = int(input("Masukkan bilangan bulat : "))

def faktorial(n) :
    if n == 0 or n == 1 :
        return 1
    else:
        return n * faktorial(n - 1)
    
if n > 0 :
    print(f"{n}! = {faktorial(n)}")
for i in range(1, n + 1) :
    print(i, end=" ")