#soal 5
nama = input("masukkan nama:")
umur = int(input("masukkan umur:"))
total_belanja = float(input("masukkan total belanja anda:"))
member = input("apakah anda memiliki kartu member?")  == "ya"
if umur < 18 :
    print("maaf anda masih belum cukup umur untuk melakukan transaksi") 
    diskon = 0
else :
    diskon = 0
    if member:
        diskon = 15
    elif total_belanja > 500.000:
        diskon = 10
        

total_diskon = total_belanja * (diskon / 100)
total_bayar = total_belanja * total_diskon

