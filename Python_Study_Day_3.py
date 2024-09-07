print("Rollercoaster'a Hoşgeldiniz!")
height = int(input("Boyunuz Kaç cm ?"))

if height >= 120:
    print("Trene binebilirsiniz")
else:
    print("Üzgünüm boyunuz 120cm olana kadar trene binemezsiniz")

#=======================================================================================================================

sayı_kontrol=int(input("Tamsayı girin: "))

if sayı_kontrol %2==0:
    print("Çift Sayıdır")
else:
    print("Tek Sayıdır")

#=======================================================================================================================

print("Welcome to the Ferris wheel!")
weight = int(input("What is your weight in kg? "))

if weight >= 17 :
    print("You can ride the Ferris wheel")
    age = int(input("What is your age? "))
    if age <= 12:
        if age < 5:
            print("Free")
        else:
            print("You should pay 7$")
    elif age <= 18:
        print("You should pay 10$")
    elif age > 80:
        print("You are too old for this")
    else:
        print("You should pay 12$")
else:
    print("Sorry you have to gain weight.")

#=======================================================================================================================
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride."),

weight = 85
height2 = 1.85

bmi = weight / (height2 ** 2)

print(bmi)

#=======================================================================================================================





