def kalkulator_diskon(total_belanja, keanggotaan):
    diskon = 0
    if keanggotaan == "gold":
        discount= 0.15
        diskon+=15
    elif keanggotaan == "silver":
        discount = 0.10
        diskon +=10
    elif keanggotaan == "bronze":
        discount = 0.05
        diskon+=5
    else:
        discount = 0.0 
    
    total_diskon = total_belanja * discount  
    hasil_setelah_diskon = total_belanja - total_diskon 

    if total_belanja > 1000000:
        tambahan_diskon = total_belanja * 0.05
        diskon+=5
        total_diskon += tambahan_diskon
        hasil_setelah_diskon -= tambahan_diskon

    return hasil_setelah_diskon,total_diskon,diskon

total_belanja = int(input("masukkan total belanja: "))
keanggotaan = input("masukkan jenis keanggotaan: ")
hasil_setelah_diskon,total_diskon,diskon= kalkulator_diskon(total_belanja, keanggotaan)
print(f"diskon kamu {diskon} %")
print(f"total diskon yang di dapat: {total_diskon}")
print(f"total yang harus di bayar: {hasil_setelah_diskon}")