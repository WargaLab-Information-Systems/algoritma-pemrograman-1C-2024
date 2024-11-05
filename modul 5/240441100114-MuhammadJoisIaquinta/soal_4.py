def palindrom(kata):
    return kata == kata[::-1]
kata = input("masukkan kata : ")
if palindrom(kata):
    print(f"{kata} adalah palindrom.")
else:
    print(f"{kata} bukan palindrom.")