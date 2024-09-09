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

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("yanlış yazdınız")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")

#=======================================================================================================================

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >=45 and age<=55:
        print("Free")
        bill = 0
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

#=======================================================================================================================





