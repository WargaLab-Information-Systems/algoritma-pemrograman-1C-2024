def hitung_faktorial(n):
    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif"
    elif n == 0 or n == 1:
        return "1"
    else:
        faktorial = 1
        langkah = ""
        for i in range(n, 0, -1):
            faktorial *= i
            langkah += str(i)
            if i > 1:
                langkah += " x "
        return langkah + f" = {faktorial}"

print(f"5! = {hitung_faktorial(5)}")
print(f"3! = {hitung_faktorial(3)}")
print(f"2! = {hitung_faktorial(2)}")
print(f"0! = {hitung_faktorial(0)}")
