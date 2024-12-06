# DATA SKOR
jaka_skor = 1200
ida_skor = 1000

# DATA IPK
ipk_jaka = 3.5
ipk_ida = 3.5

# DATA KRITERIA BEASISWA
minimal_skor = 1100
minimal_ipk = 3.0

# SYARAT KELULUSAN ADALAH MELEBIHI KRITERIA NILAI BEASISWA

# JAKA 
if jaka_skor > minimal_skor or ipk_jaka >= minimal_ipk :
    print("skor dan ipk yang dimiliki jaka memenuhi standar kelulusan penerima beasiswa")
else : 
    print("skor dan ipk yang dimiliki jaka tidak memenuhi standar kelulusan penerima beasiswa")

# IDA 
if ida_skor > minimal_skor or ipk_ida >= minimal_ipk :
    print("skor dan ipk yang dimiliki ida memenuhi standar kelulusa penerima beasiswa")
else : 
    print("skor dan ipk yang dimiliki ida tidak memenuhi standar kelulusan penerima beasiswa")