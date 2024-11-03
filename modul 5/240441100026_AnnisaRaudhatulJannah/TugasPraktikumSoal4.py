
def cek_palindrom(kata):
    kata = kata.replace(" ", "").lower() # Menghapus spasi dan mengubah ke huruf kecil untuk pemeriksaan
    return kata == kata[::-1]

kata1= "Katak"
kata2= "Madam"
kata3= "Hello"

if cek_palindrom(kata1):
   print(f"{kata1} adalah palindrom : True ")
else:
   print(f"{kata1} adalah bukan palindrom : False")

if cek_palindrom(kata2):
   print(f"{kata2} adalah palindrom : True")
else:
   print(f"{kata2} adalah bukan palindrom : False")  

if cek_palindrom(kata3):
   print(f"{kata3} adalah palindrom : True")
else:
   print(f"{kata3} adalah bukan palindrom : False")  