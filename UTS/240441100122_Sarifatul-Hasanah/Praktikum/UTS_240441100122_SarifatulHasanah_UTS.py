makan = str(input("Apakah anda sudah makan : "))
mandi = str(input("Apakah anda sudah mandi : "))
transportasi = str(input("Pilih Transportasi : "))
waktu_makan = 15
waktu_mandi = 10
transportasi_jalan = 30
transportasi_motor = 15
transportasi_sepeda = 15

if makan == "tidak" :
    print("Anda harus makan selama 15 menit")
    makan = waktu_makan 
else :
    print("Silahkan lanjutkan aktivitas anda")

if mandi == "tidak" :
    print("Anda harus mandi selama 10 menit")
    mandi = waktu_mandi
else :
    print("Silahkan lanjutkan aktivitas anda")

if transportasi == "jalan kaki" :
    print("Anda membutuhkan waktu 30 menit untuk sampai kampus")
elif transportasi == "motor" :
    print("Anda membutuhkan waktu 15 menit untuk sampai kampus")
elif transportasi == "sepeda" :
    print("Anda membutuhkan waktu 50 menit untuk sampai kampus")

total_waktu_persiapan = waktu_makan + waktu_mandi + transportasi_jalan + transportasi_motor + transportasi_sepeda

#menghitung total waktu yang dibutuhkan
if total_waktu_persiapan > 60 :
    print("Kamu Terlambat")
else :
    print("Kamu Berangkat Tepat Waktu")
 
