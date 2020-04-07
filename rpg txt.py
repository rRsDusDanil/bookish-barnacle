from random import randint      # импорт нужных команд (рандом и сон)
from time import sleep

hpP = 100
attP = 10
hpB = 100        # бесполезные переменные
attB = 10

print('Mini-RPG')
q = input('Начать игру.')
print('Выберите тип игры:')
print('1 PvE')
print('2 Песочница')    # отсутсвует
q = int(input())
while q == 1:
   print('Рандомизировать здоровье врага?')    # рандом хп врага
   f = int(input('1(Да)/2(Нет)'))
   if f == 1:
      hpB = randint(50,200)
   print('ГОТОВ?')
   print('1 Да')
   print('1 Нет')
   w = int(input(''))
   if w <= 1:
      break
   elif w >= 2:
      sleep(1)

print('Выберите класс вашего героя:')

while w <= 1:
   print('1. Рыцарь \n 2. Лучник \n 3. Маг')
   r = int(input())
   if r == 1:
      print('Описание: \n Имеет большое количество хп(200) и брони(10). \n Весь получаемый урон понижен на 30%.')
      print('Выбрать?')
      g = int(input(1/2))
      if g == 1:
         clas = r
         break
      if g == 2:
         print('...')
      if r == 2:
       print('Описание: \n Имеет найменьшее количество хп(75) и отсутсвие брони. \n Способен уворачиватся от ударов(50%).')
       print('Выбрать?')
       g = int(input(1/2))
       if g == 1:
         clas = r
         break
       if g == 2:
          print('...')
      if r == 3:
       print('Описание: \n Имеет обычное количество хп(100) и отсутсвие брони. \n Увеличивает урон на 20%.')
       print('Выбрать?')
       g = int(input(1/2))
       if g == 1:
          clas = r
          break
       if g == 2:
          print('...')
 # 0.1.0