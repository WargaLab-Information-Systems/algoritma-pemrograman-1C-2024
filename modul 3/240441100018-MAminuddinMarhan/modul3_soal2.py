bilangan = input("Masukkan bilangan bulat: ")
bilangan_terbalik = " "
for a in range(len(bilangan)-1, -1, -1):
    bilangan_terbalik += bilangan[a]
print(f"Bilangan setelah dibalik: {bilangan_terbalik}")