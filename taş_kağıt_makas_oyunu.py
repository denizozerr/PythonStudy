import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

""
liste=[rock,paper,scissors]

print("Taş, Kağıt, Makas Oyununa Hoşgeldiniz.")
sec=input("Taş için '1', Kağıt için '2', Makas için '3' yazın :")
if sec=='1':
    print(rock)
elif sec=='2':
    print(paper)
elif sec=='3':
    print(scissors)
else:
    print("YANLIŞ YAZDINIZ")

print("Bilgisayarın Seçtiği")
bot=random.choice([rock,paper,scissors])
print(bot)

if sec=="1" and bot==rock or sec=="2" and bot==paper or sec=="3" and bot==scissors:
    print("berabere")
elif sec=="1" and bot==scissors or sec=="2" and bot==rock or sec=="3" and bot==paper:
    print("Sen Kazandın")
elif sec=="1" and bot==paper or sec=="2" and bot==scissors or sec=="3" and bot==rock:
    print("Bilgisayar Kazandı")
else:
    print("SİSTEM HATASI OYUNU YENİDEN BAŞLAT")