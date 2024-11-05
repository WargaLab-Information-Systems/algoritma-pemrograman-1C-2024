total_belanja = int(input("Masukkan Harga belanja : "))
keanggotaan = input("Masukkan member 'Gold' 'Silver' 'Bronze' : ")

def calculate_discount(total_belanja, keanggotaan):
    diskon = 0

    if total_belanja > 1000000:
        diskon += 0.05
        discount = 5
        if keanggotaan == "Gold":
            diskon += 0.15
            discount += 15
        elif keanggotaan == "Silver":
            diskon += 0.10
            discount += 10
        elif keanggotaan == "Bronze":
            diskon += 0.05
            discount += 5
        else:
            diskon += 0.0
            print("Anda tidak dapat diskon tambahan")

    print(f"Diskon yang didapat: {discount} %")

    total_diskon = total_belanja * diskon
    return total_diskon


diskon = calculate_discount(total_belanja, keanggotaan)
print(f"Total diskon yang didapat: {int(diskon)}")
print(f"Total harga belanja: {total_belanja - diskon}")