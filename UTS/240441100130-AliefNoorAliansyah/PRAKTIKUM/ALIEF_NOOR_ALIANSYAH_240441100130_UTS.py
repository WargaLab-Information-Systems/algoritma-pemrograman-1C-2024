belum_makan = 15
belum_mandi = 10
jalan_kaki = 30
motor = 15

input(str("belum makan? :"))
input(str("belum mandi? :"))
input(str("pilih transportasi :"))

if belum_makan != "ya" :
    print("15 menit")
elif belum_mandi != "ya" :
    print("10 menit")
elif motor == "motor" :
    print("15 menit")
else :
    print("30 menit")

