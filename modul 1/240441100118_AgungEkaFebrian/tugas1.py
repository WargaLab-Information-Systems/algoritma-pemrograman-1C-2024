("Andi mempunyai celengan berbentuk balok dan tabung. Celengan yang berbentuk balok memiliki ukuran panjang 20cm dan lebar 13cm, dan tinggi 7cm, Sedangkan celengan yang berbentuk tabung memiliki diameter 14cm dan luas selimutnya 440cm2. Bantulah Andi dengan membuat program untuk menghitung volume dari kedua celengan miliknya tersebut ")
# balok
p_balok = 20
l_balok = 13
t_balok = 7

# tabung
d_tabung = 14
luas_selimut = 440
r_tabung =  d_tabung / 2
t_tabung = luas_selimut / (2 * 22/7 * r_tabung)

# volume balok
v_balok = p_balok * l_balok * t_balok

# volume tabung
v_tabung = 22/7 * r_tabung ** 2 * t_tabung

print ("panjang balok : ", p_balok)
print ("lebar balok : ", l_balok)
print ("tinggi balok : ", t_balok)
print ("\ndiameter tabung : ", d_tabung)
print ("luas selimut : ", luas_selimut)
print ("jari-jari : ", r_tabung)
print ("tinggi tabung : ", t_tabung)
print ("\nvolume balok : ", v_balok)
print ("volume tabung : ", v_tabung)
