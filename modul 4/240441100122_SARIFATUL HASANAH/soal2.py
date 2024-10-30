desimal = int(input("Masukkan bilangan desimal: "))

if desimal < 0:
    print("Masukkan bilangan desimal positif.")
else:
    biner = ""
    while desimal > 0:
        sisa = desimal % 2
        biner = str(sisa) + biner
        desimal = desimal // 2

    print(f"Bilangan biner: {biner}")

    jumlah_biner = len(biner)
    for i in range(1, jumlah_biner + 1):
        print(biner[:i])

