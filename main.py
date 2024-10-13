karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

import random

while True:
    hesap = input("Hangi hesabin icin sifre istersin?\n")
    if hesap == "cikis":
        break
    sayi = int(input('Kac karakterli sifre istersiniz?\n'))
    sifre = ""
    for i in range(sayi):
        sifre += random.choice(karakterler)
        with open("sifreler.txt", "a") as file:
            file.write(f"{hesap} : {sifre}")

    print(f"{hesap} : {sifre}")