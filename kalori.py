# Kullanıcıdan günde kaç saat nelere vakit ayırabileceğini çekeceğiz.
# Bazal Metabolizmasını hesaplayıp günde kaç kaloriye ihtiyac duyduğunu gireceğiz.
# Günlük ortalama ne kadar kalori tüketmesi gerektiğini söyleyeceğiz.
# Bu şekilde ne kadar sürede kaç kilo zayıflayacağını kullanıcıya iletmiş olacağız.
# Fit bir görünüm üzerinden ideal boy / kilo oranından hesaplayacağız.

print("------------------------------------------------------------------------------------------------------")

# Yetişkin bir erkeğin bazal metabolizma hızı=  88.362 + (13.397 x ağırlık kg) + (4.799 x cm olarak boy) – (5.677 x yıl olarak yaş)
# Yetişkin bir kadının bazal metabolizma hızı= 447.593 + (9.247 x kg olarak ağırlık) + (3.098 x cm olarak boy) – (4.330 x yıl olarak yaş)

cinsiyet = str(input("Cinsiyetiniz nedir? (E/K) : "))

yas = float(input("Yaşınız nedir? : "))

boy = float(input("Boyunucu 'cm' cinsinden giriniz : "))

ideal = boy - 100

kilo = float(input("Kilonuzu 'kg' cinsinden giriniz : "))

if cinsiyet == "E":
    bazal = 88.362 + (13.397 * kilo) + (4.799 * boy) - (5.677 * yas)
elif cinsiyet == "K":
    bazal = 447.593 + (9.247 * kilo) + (3.098 * boy) - (4.330 * yas)

print("------------------------------------------------------------------------------------------------------")

# Girilen verilerle (günlük yakılan kalori ie) ne kadar sürede zayıflanacağını bul. (İaeal kiloya ne kadar sürede ulaşılacak)

print("İdeal kilonuz: " , ideal)

deger = str

deger2 = str

deger3 = str

deger4 = str

miktar = kilo - ideal

if ideal > kilo:
    miktar = miktar * (-1)
    deger = "alman"
    deger2 = "Almanız"
    deger3 = "alacaksın"
    deger4 = "alarak"
    deger5 = "alırsan"
else:
    deger = "vermen"
    deger2 = "Yakmanız"
    deger3 = "yakacaksın"
    deger4 = "yakarak"
    deger5 = "almazsan"

print("Günlük BMR kalorin :" , bazal)

print(miktar , "kg", deger , "gerekiyor.")

kg = 7400

kaloriler = miktar * kg

print(deger2, "gereken toplam kalori :" , kaloriler)

print("------------------------------------------------------------------------------------------------------")

if kilo > ideal:
    print("Etkinlikler ve Kalorileri")
    print("------------------------------------------------------------------------------------------------------")
    print("Koşu (1074) : 9km/h ile koşmak size saatte 755 kalori yaktırır.")
    print("Yük Yüryüşü (635) : Ağırlık yüklü çantanızla 1 saat yürümek size 635 kalori yaktırır.")
    print("Bisiklet (366) : 1 saat ortalama hızda bisiklet sürmek saatte 366 kalori yaktırır.")
    print("Yürüyüş (390) : Ortalama hızda 1 saat yürümek size 390 kalori yaktırır.")
    print("Futbol (728) : 1 saat futbol oynamak 728 kalori yaktırır.")
    print("Doğa Yüryüşü (546) : 1 saatlik doğa yürüyüşü 546 kalori yaktırır.")
    print("Ağırlık (455) : 1 saatllik ağırlık antremanı size 455 kalori yaktırır.")
    print("İp Atlamak (1074) : 1 saat boyunca ip attırmak size 1074 kalori yaktırır.")
    print("------------------------------------------------------------------------------------------------------")

print("Günde kaç kalori" , deger3 , "? : ")

kalori = float(input())

print("------------------------------------------------------------------------------------------------------") 

gun = kaloriler / kalori

gunbazal = kaloriler / (kalori + bazal)

print("İdeal kilona günde" , kalori , "kalori" , deger4 , gun , "gün sonra ulaşacaksın.")

print("(" , gun / 30 , "ay sonra. )")

print("------------------------------------------------------------------------------------------------------")

print("Günlük min. tüketmen gereken kalori:" , bazal)

print("Eğer tüketmen gereken kaloriyi" , deger5 , ", ideal kilona günde" , kalori + bazal , "kalori" , deger4 , gunbazal , "gün sonra ulaşacaksın.")

print("------------------------------------------------------------------------------------------------------")