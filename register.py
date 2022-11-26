
ism = input("ismingizni kiriting")
familiya = input("Familiyangizni kiriting")
tugilgan = int(input("tug'ilgan yilinggizni kiriting"))
while True:
    parol1 = input("parolni kiriting")
    parol2 = input("parolni kiriting")


    if parol1 == parol2:
        yil = 2022 - tugilgan
        print("muvaffiqiyatli kiritildingiz" + ism ,yil,familiya)
        break

    elif parol1 != parol2:
        print("xato kod kritdingiz")



