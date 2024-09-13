fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit+"pie")

#=======================================================================================================================

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#toplama yöntemi 1
toplam_skor=sum(student_scores)
print(toplam_skor)


#toplama yöntemi 2
toplam = 0
for skor in student_scores:
    toplam += skor

print(toplam)
#=======================================================================================================================


# max() fonksiyonunu kullanmak yerine for döngüsü ile en büyük sayıyı bulmak
en_buyuk_puan = 0
for puan in student_scores:
    if puan > en_buyuk_puan:
        en_buyuk_puan = puan
        print(puan)

#=======================================================================================================================

for sayi in range(1,10):
    print(sayi)

for sayi in range(1,10,3):
    print(sayi)



sayi=0
for toplam_sayi in range(1,101):
    sayi+=toplam_sayi
print(sayi)


sayi=0
for sayi in range(1,101):
    if sayi%3 == 0:
        print("fizz")
    elif sayi%5 == 0:
        print("buzz")
    elif sayi%15 == 0:
        print("fizzbuzz")
    else:
        print(sayi)