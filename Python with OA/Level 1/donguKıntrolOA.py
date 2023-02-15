# break , continue

a = 0 
while True:
    a += 1
    print(a)
    if a == 1000:
        break
    print("1.00'e eşit değil")
print("Eşitlendi!")

a = 0
while True:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
print("bitti.")