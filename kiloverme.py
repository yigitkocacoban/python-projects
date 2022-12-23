kilo = float(input("Kaç kilosunuz: "))
hedef = float(input("Hedef kilonuz nedir: "))
kg = 7400
toplam = (kilo-hedef)*(7400-2000)
print("Yakılması gereken toplam kalori:" , toplam)
gun = float(input("Kaç günde hedef kiloya ulaşmak istiyorsunuz: "))
x = toplam/gun 
print("Günde" , x , "kadar kalori yakarak" , gun , "günde hedefe ulaşabilirsiniz.")