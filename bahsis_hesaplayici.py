print("Bahşiş Hesaplayıcıya Hoşgeldiniz!")
bill = float(input("Hesap Ne Kadar Tuttu? $"))
tip = int(input("Yüzde kaç bahşiş vereceksiniz?"))
people = int(input("Hesabı Kaç Kişi Ödeyecek? "))

bahsis=(bill*tip/100+bill)

odeyecek_kisi_sayisi=(bahsis/people)

print("Kişi başı hesap tutarı :"+ str(round(odeyecek_kisi_sayisi, 2)))