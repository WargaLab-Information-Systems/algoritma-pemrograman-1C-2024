nilai_input = int(input("masukan nilai (0-100): "))
if 100 >= nilai_input >= 81:
    grade = "A"
elif 80 >= nilai_input >= 71:
    grade = "B"
elif 70 >= nilai_input >= 61:
    grade = "C"
elif 60 >= nilai_input >= 41:
    grade = "D"
elif 40 >= nilai_input >= 0:
    grade = "E"
else:
    grade = "nilai tidak valid"
print(f"grade: {grade}")