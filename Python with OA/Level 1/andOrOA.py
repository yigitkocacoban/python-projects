"""
and (ve) ve or (veya) ile islem yapilacak.
Islemlerde Boolean Algebra (Bool Cebiri) temel alinacak.
and her iki durum karsilasirildiginda eger her ikisi de True (Dogru) ise True sonucu verir. Diger durumlarda False.
or her iki durum karsilastirildiginda eger her ikisi de False (Yanlis) ise False sonucunu verir. Diger durumlarda True.
not: işlem sonucunu terse çevirir 1 -> 0 , 0-> 1
"""
a = 3
b = 2
c = 3

islem_or = a == b or a == c
islem_and = a == b and a == c
print(islem_or)
print("***************************")
print (islem_and)
print("***************************")
islem_coklu = (a == b or a == c) or (a == b and a == c)
print (islem_coklu)
print("***************************")
islem_coklu = not(a == b or a == c) or (a == b and a == c)
print (islem_coklu)
print("***************************")
