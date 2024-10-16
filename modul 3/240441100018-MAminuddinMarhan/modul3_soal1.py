ukuran = int(input("Masukkan size: "))
for a in range(ukuran):
    if a == 0 or a == ukuran - 1:
        print("x" * ukuran)
    else:
        print("x" + " " * (ukuran - 2) + "x")
print()
for a in range(ukuran):
    print(" " * (ukuran // 2) + "x")
print()
for a in range(ukuran):
    if a == 0 or a == ukuran - 1 or a == ukuran // 2:
        print("x" * ukuran)
    else:
        print("x" + " " * (ukuran - 2) + "x")