nama = input("Masukkan nama: ")

ipk = float(input("Masukkan nilai IPK: "))
skor = int(input("Masukkan skor: "))

if ipk >= 3.0 and skor > 1100:
    keterangan = f"{nama}, anda memenuhi syarat untuk menerima KIP."
elif ipk >= 2.5 and skor >= 1000:
    keterangan = f"{nama}, Mohon maaf anda tidak memenuhi syarat untuk menerima KIP."
else:
    keterangan = f"{nama}, Anda tidak memenuhi syarat untuk menerima KIP."

print(keterangan)
                                           