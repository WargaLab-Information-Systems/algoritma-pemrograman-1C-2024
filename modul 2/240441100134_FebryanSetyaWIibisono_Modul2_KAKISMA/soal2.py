skor_Jaka = 1100
skor_Ida = 1000
IPK_Jaka = 3,5
IPK_Ida = 3,5
min_IPK =3,0
min_skor=1100
syarat_lulus_beasiswa=min_IPK and min_skor
if syarat_lulus_beasiswa == skor_Jaka and IPK_Jaka :
    print("Jaka lulus beasiswa")
else :
    print("Jaka tidak lulus beasiswa")
if syarat_lulus_beasiswa == skor_Ida and IPK_Ida :
    print("Ida lulus beasiswa")
else :
    print("Ida tidak lulus beasiswa")
