import time 
a = 0
while a < 5:
    a += 1 
    parol = input("parolni kiriting")
    if parol == "firdavs02":
        print("Parol tugri")
        break

    elif parol == 3:
         time.sleep(0.2)

    else:
        print("Parol xato")
        break
                
        
