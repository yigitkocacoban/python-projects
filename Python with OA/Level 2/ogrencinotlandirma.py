

notlar = [19,49, 55, 63, 78, 81]

for n in notlar:
    if n < 40:
        print("Kaldınız. Notunuz:" , n)
    else:
        if n % 5 == 0:
            print("Geçtiniz. Notunuz:" , n)
        elif n % 5 >= 3:
            print("Geçtiniz. Yukarı yuvarlanmış notunuz:" , n + (5 - n % 5 ))
        else:
            print("Geçtiniz. Aşağı yuvarlanan notunuz:" , n - (n % 5))