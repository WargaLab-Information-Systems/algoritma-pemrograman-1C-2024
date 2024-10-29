makan=("sudah makan?")
waktu_makan= ("15 menit")
mandi=("sudah mandi?")
waktu_mandi=("10 menit")
transportasi=("jalan kaki/menggunakan motor")
jalan_kaki=("30 menit")
menggunakan_motor=("30 menit")

if makan == input("sudah makan? ya/tidak: "):
    print("kamu membutuhkan waktu {waktu_makan}")
else:
    print(mandi)
    
if mandi==input("sudah mandi?ya/tidak: "):
    print("kamu membutuhkan waktu {waktu_mandi}")
else:
    print(transportasi)
    
if transportasi== input("jalan kaki/menggunakan motor: "):
    print("kamu membutuhkan waktu {jalan_kaki}")
    print("kamu membutuhkan waktu {waktu_mandi}")



print ("selesai")