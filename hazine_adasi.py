print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Hazine Adasına Hoş Geldiniz.")
print("Görevin seçimler yaparak hazine sandığının olduğu odayı bulmak.")

ilk_kisim=input("Karşında bir yol ayrımı var hangi yönü seçeceksin ? (sağ veya sol) :")

if ilk_kisim == "sağ":
    print("İleriye gittin ve bayırdan aşağı düştün. OYUN BİTTİ.")
elif ilk_kisim == "sol":
    print("Şimdi önüne bir ev çıktı ve hava kararmaya başladı.")
    ikinci_kisim=(input(" Eve doğru mu gideceksin yoksa geceyi dışarıda mı geçireceksin ? (ev veya dışarı) "))
    if ikinci_kisim == "ev":
        print("Evin kapısı kilitli.")
        ev_kisim=(input("Kapıyı mı kıracaksın yoksa pencereden mi girmeye çalışacaksın ? (kapı veya pencere) "))
        if ev_kisim == "kapı":
            print("Kapıyı kırmak için geri koştun ve tam kapıya çarpacakken ev sahibi kapıyı açtı ve içerideki duvara yapıştın ve burnunu kırdın. OYUN BİTTİ.")
        elif ev_kisim == "pencere":
            print("Camdan girerken ev sahibi seni hırsız sandı ve sana silahıyla ateş etti. OYUN BİTTİ.")
        else:
            print("YANLIŞ YAZDIN")
    elif ikinci_kisim == "dışarı":
        print("Dışarıda çok huzursuz bir gece geçirdin ama yoluna artık devam edebilirsin.")
        ücüncü_kisim=(input("Şimdi karşında gene bir yol ayrımı var. Hangi yönü seçeceksin ? (sağ veya sol)"))
        if ücüncü_kisim == "sağ":
            print("Yürümeye devam ettin ve karşında bir kule belirdi.")
            dördüncü_kisim=(input("Bu kulenin üç tane kapısı var. Hangi kapıyı tercih edeceksin ? (ilk , orta , son "))
            if dördüncü_kisim == "ilk":
                print("Hazine odasını buldun tebrikler. OYUNU KAZANDIN.")
            elif dördüncü_kisim == "orta":
                print("Kapıdan geçtikten sonra aşağıdaki tuzak kapısı açıldı ve düştün. OYUN BİTTİ.")
            elif dördüncü_kisim == "son":
                print("Kapıdan geçtin ve kasayı açtığın anda o bir kasa değil mimic canavarıymış seni yedi. OYUN BİTTİ.")
            else:
                print("YANLIŞ YAZDIN")
    else:
        print("YANLIŞ YAZDIN")
else:
    print("YANLIŞ YAZDIN")



