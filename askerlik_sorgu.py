askerlik_sorgu=int(input("Yaşını Yaz: "))

if askerlik_sorgu >= 18:
    okul_durumu = input("Okul durumunu gir (evet veya hayır): ")
    if okul_durumu == ("evet"):
        print("askere gelmene gerek yok")
    elif okul_durumu == ("hayır"):
        print("askere gidiyosun geçmiş olsun")
    else:
        print("yanlış yazdın")
else:
    print("askere daha gelmiyorsun")