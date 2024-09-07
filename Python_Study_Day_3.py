#ödev
#askerlik sorgula : kullanıcıdan yaş al, okul durumunu sor.
from bahsis_hesaplayici import odeyecek_kisi_sayisi

#18 den büyükse ve okuyorsa askere GİDEMEZ
#18den küçükse askere GİDEMEZ
#18den büyükse ve okumuyorsa askere GİDER
#%%
askerlik_sorgu=int(input("Yaşını Yaz: "))

if askerlik_sorgu >= 18:
    okul_durumu = input("Okul durumunu gir (evet veya hayır: ")
    if okul_durumu == ("evet"):
        print("askere gelmene gerek yok")
    elif okul_durumu == ("hayır"):
        print("askere gidiyosun geçmiş olsun")
    else:
        print("yanlış yazdın")
else:
    print("askere daha gelmiyorsun")



