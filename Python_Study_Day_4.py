import random

#rastgele_tamsayi=random.randint(1,100)

#print(rastgele_tamsayi)

#random_sayı_0_1_arasi=random.random() * 10
#print(random_sayı_0_1_arasi)

#random_float=random.uniform(1,10)
#print(random_float)

yazi_tura=random.randint(0,1)
if yazi_tura==0:
    print("yazı")
else:
    print("tura")

#=======================================================================================================================

fruits = ["Cherry", "Apple", "Pear"]
print(fruits[1])

fruits.append("Melon")
print(fruits)

fruits.extend(["watermelon","peach"])
print(fruits)

#=======================================================================================================================

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#1. yöntem
rastgele=random.choice(friends)

print(rastgele)
#2. yöntem
rastgele2=random.randint(0,4)
print(friends[rastgele2])

#=======================================================================================================================

