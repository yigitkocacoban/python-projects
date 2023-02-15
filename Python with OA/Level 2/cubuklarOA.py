cubuklar = [1,2,3,4,5,4,2,3,1,4,3,1,1,7,5,3,5,4]

"""

enUzun = 0

for i in cubuklar:
    if i > enUzun:
        enUzun = i
print(enUzun)

sayac = 0

for cubuk in cubuklar:
    if cubuk == enUzun:
        sayac += 1

print(sayac)

"""

enUzun = 0
sayac = 1

for cubuk in cubuklar:
    if cubuk > enUzun:
        enUzun = cubuk
        sayac = 1
    elif cubuk == enUzun:
        sayac += 1

print("En Uzun:", enUzun)
print("En Uzun Adedi:", sayac)