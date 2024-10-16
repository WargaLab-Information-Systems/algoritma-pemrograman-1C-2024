makan = input("sudah makan? (ya/tidak)")
if makan=="ya":
    waktu_makan=0
else: 
    waktu_makan=15

mandi= input("sudah mandi? (ya/tidak)")
if mandi=="ya":
    waktu_mandi=0
else:
    waktu_mandi= 10

transportasi= input("pilih trasportasi (motor/jalankaki)")
if transportasi=="motor":
    waktu=30
elif transportasi=="jalankaki":
    waktu=30

total_waktu= waktu_makan + waktu_mandi +waktu

print("total waktu persiapan dan perjalanan:", total_waktu)
if total_waktu<60:
    print("tapat waktu")
else: 
    print("terlambat")