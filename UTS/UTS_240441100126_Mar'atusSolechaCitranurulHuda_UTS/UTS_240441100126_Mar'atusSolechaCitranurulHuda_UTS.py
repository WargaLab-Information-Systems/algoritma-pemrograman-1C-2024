makan = input("apakah kamu sudah makan? : ")
tidak = 15

if makan == "tidak" :
    print("sebaiknya anda segera makan")
    if makan == "ya" and "waktu makan" > 15 :
        print("sebaiknya anda segera makan dalam waktu", tidak)
else :
    print("jika anda sudah makan, sebaiknya anda segera mandi")


mandi = (input("apakah kamu sudah mandi? "))
mandi = 10
if mandi == "ya" :
    print("sebaiknya anda segera bersiap-siap")
else :
    print("sebaiknya anda segera mandi dengan waktu", mandi)


berangkat = (input("dengan transportasi apa kamu akan berangkat? "))
jalan_kaki = 30 #menit
motor = 15 #menit
if berangkat == jalan_kaki :
    print("kamu akan membutuhkan waktu 30 menit untuk sampai")
elif berangkat == motor :
    print("kamu membutuhkan waktu 15 menit untuk sampai")


