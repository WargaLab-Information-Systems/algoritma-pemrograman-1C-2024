size = int(input("masukkan size: "))
rumus = int(size/2)


# membuat pola angka dengan menggunakan x pola angka 1
for i in range (size):
    print(" " * (size -4) + "x")
print() # pindah baris
    
# angka 2
print("x" * size)
for i in range(1,rumus):
    print(""+" " * (size - 1) + "x")
print("x" * size)
for i in range(1,rumus):
    print("x"+" " * (size - 2) + "")
print("x" * size)

print()

# angka 6
print("x" * size)
for i in range(1,rumus):
    print(""+" " * (size - 6) + "x")
print("x" * size)
for i in range(1,rumus):
    print("x"+" " * (size - 2) + "x")
print("x" * size)