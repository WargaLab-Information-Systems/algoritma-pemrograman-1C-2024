size= int(input("masukkan size: "))
if size<3:
    print("size minimal 3 untuk pola yang benar")
else:
    #Mencetak angka 0
    print("x"*size)
    for i in range(size-2):
       print("x"+" "*(size-2)+"x")
    print("x"*size)
    print(" ")

    #Mencetak angka 1
    print("x"*(size-2))
    for kolom in range(size-2):
        print(" "+" "+"xx")
    print("x"*size)
    print("")
    
    #Mencetak angka 0
    print("x"*size)
    for i in range(size-2):
       print("x"+" "*(size-2)+"x")
    print("x"*size)
    print(" ")