jaka_Skor = 1100
jaka_IPK = 3.5

ida_Skor = 1000
ida_IPK = 3.5

Batas_Skor = 1100
Batas_IPK = 3.0

jaka_lulus = (jaka_Skor > Batas_Skor) * (jaka_IPK >= Batas_IPK)
ida_lulus = (ida_Skor > Batas_Skor) * (ida_IPK >= Batas_IPK)

if jaka_lulus:
    print("jaka lulus persyaratan beasiswa")

else:
    print("jaka tidak lulus persyaratan beasiswa")

if ida_lulus:
    print("ida lulus persyaratan beasiswa")
else:
    print("ida tidak lulus persyaratan beasiswa")