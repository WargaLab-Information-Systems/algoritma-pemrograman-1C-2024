#soal no 2
print("Darmaji ingin mengetahui jumlah nilai dari 8 suku pertama dari sebuah deret aritmatika dengan keadaan suku ke-5 dari deret tersebut bernilai 11 dan jumlah nilai suku ke-8 dan suku ke-12 nya adalah 52. Buatlah program untuk membantu Darmaji untuk menyelesaikan masalah tersebut !")   
suku_ke5 = 11
suku_ke8_dan_ke12 = 52
    #maka 
    #1. a + 4d = 11 
    #2. 2a + 18d = 52

    #dari suku ke-5
    #u5 = a + 4d = 11(1)
    #substitusi persamaan kedua
    #u8 = a + 7d
    #u12 = a + 11d
    #u8 + u12 = 2(11 - 4d)+ 18d = 52
    #penyelesaian
    #22 - 8d + 18d = 52
    #10d = 30
    #d = 3

print(f"2. Darmaji ingin mengetahui jumlah nilai dari 8 suku pertama dari sebuah deret aritmatika dengan keadaan suku ke-5 dari deret tersebut bernilai 11 dan jumlah nilai suku ke 8 dan suku ke-12 nya adalah 52. Buatlah program untuk membantu Darmaji untuk menyelesaikan masalah tersebut ! ")
print(f"jawaban : ")
print(f"diketahui suku ke 5 adalah 11 dan jumlah suku ke 8 dan suku ke 12 adalah 52,maka : ")
d = 3
a = 11 - 4 * d
jumlah_8_suku_1 = 8 / 2 * (2 * a + (8 - 1) * d)
print(f"jumlah 8 suku 1 = 8 / 2 * (2 * a + (8 - 1) * d )")
print(f"jadi jumlah 8 suku pertama yaitu : {jumlah_8_suku_1}")

