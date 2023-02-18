import math
import random

gamer1 = int(input("Oyuncu 1, sayı giriniz (1-100)"))
gamer2 = int(input("Oyuncu 2, sayı giriniz (1-100)"))
gamer3 = int(input("Oyuncu 3, sayı giriniz (1-100)"))
gamer4 = int(input("Oyuncu 4, sayı giriniz (1-100)"))
gamer5 = int(input("Oyuncu 5, sayı giriniz (1-100)"))

oyuncuTahminleri = [gamer1, gamer2, gamer3, gamer4, gamer5]

randomTahmin = random.choice(oyuncuTahminleri)

if randomTahmin == gamer1:
    print("1. oyuncu kazandı.")
elif randomTahmin == gamer2:
    print("2. oyuncu kazandı.")
elif randomTahmin == gamer3:
    print("3. oyuncu kazandı.")
elif randomTahmin == gamer4:
    print("4. oyuncu kazandı.")
elif randomTahmin == gamer5:
    print("5. oyuncu kazandı.")
else:
    exit

print(randomTahmin)

