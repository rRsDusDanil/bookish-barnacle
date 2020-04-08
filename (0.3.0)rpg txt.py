from random import randint      # импорт нужных команд (рандом и сон)
from time import sleep

print('Mini-RPG')
q = input('Начать игру.')
print('Выберите тип игры:')
print('1 PvE')
print('2 Битва с боссом')    # отсутсвует
q = int(input())
while q == 1:
   print('ГОТОВ?')
   print('1 Да')
   print('2 Нет')
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
      print('Описание: \n Имеет большое количество хп(145) и брони(5). \n Весь получаемый урон понижен на 20%.')
      print('Выбрать?')
      g = int(input('1/2'))
      if g == 1:
         classPlayer = r
         break
      if g == 2:
         print('...')
   if r == 2:
       print('Описание: \n Имеет найменьшее количество хп(85) и отсутсвие брони. \n Буст к урону +30%.')
       print('Выбрать?')
       g = int(input('1/2'))
       if g == 1:
         classPlayer = r
         break
       if g == 2:
          print('...')
   if r == 3:
       print('Описание: \n Имеет обычное количество хп(110) и отсутсвие брони. \n Увеличивает урон на 20%.')
       print('Выбрать?')
       g = int(input('1/2'))
       if g == 1:
          classPlayer = r
          break
       if g == 2:
          print('...')

if classPlayer == 1:
   hpPlayer = 145
   attPlayer = randint(10,20)
   deffPlayer = 5
if classPlayer == 2:
   hpPlayer = 85
   attPlayer = randint(10,25)
   deffPlayer = -3
if classPlayer == 3:
   hpPlayer = 110
   attPlayer = randint(15,30)
   deffPlayer = -1

classBot = randint(1,3)

if classBot == 1:
   hpBot = 145
   attBot = randint(10,20)
   deffBot = 5
if classBot == 2:
   hpBot = 85
   attBot = randint(10,25)
   deffBot = -3
if classBot == 3:
   hpBot = 110
   attBot = randint(15,30)
   deffBot = -1

z = int(input('1(yes)/2(no)'))
print('[P]                   [B]')
print('-------------------------')
while z == 1:
   if classPlayer == 1:
      print('Выберите атаку: \n 1. Удар \n2. Хил')
      atPlayer = int(input('Выбор:'))
      if atPlayer == 1 and classBot == 1: 
         hpBot -= attPlayer * 0.8 - deffBot
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 2: 
         hpBot -= (attPlayer - deffBot)
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 3: 
         hpBot -= (attPlayer - deffBot)
         print('ХП врага = %s' % hpBot)
   if classPlayer == 2:
      print('Выберите атаку: \n 1. Выстрел \n2. Хил')
      atPlayer = int(input('Выбор:'))
      if atPlayer == 1 and classBot == 1: 
         hpBot -= attPlayer * 1.1 - deffBot
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 2: 
         hpBot -= attPlayer * 1.3 - deffBot
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 3: 
         hpBot -= (attPlayer * 1.3 - deffBot)
         print('ХП врага = %s' % hpBot)
   if classPlayer == 3:
      print('Выберите атаку: \n 1. Магия \n2. Хил')
      atPlayer = int(input('Выбор:'))
      if atPlayer == 1 and classBot == 1: 
         hpBot -= attPlayer - deffBot
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 2: 
         hpBot -= attPlayer * 1.2 - deffBot
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 3: 
         hpBot -= (attPlayer * 1.2 - deffBot)
         print('ХП врага = %s' % hpBot)
   if atPlayer == 2:
      heal = randint(15,35)
      hpPlayer += heal 
      print('Вы восстановили себя на %s ХП.' % heal)
      print('Ваше ХП теперь %s.' % hpPlayer)
   print('Бот атакует!')
   if classBot == 1:
    if classPlayer == 1: 
       hpPlayer -= attBot * 0.8 - deffPlayer
    if classPlayer == 2: 
       hpPlayer -= attBot - deffPlayer
    if classPlayer == 3: 
       hpPlayer -= attBot - deffPlayer
   if classBot == 2:
    if classPlayer == 1: 
       hpPlayer -= attBot * 1.1 - deffPlayer
    if classPlayer == 2: 
       hpPlayer -= attBot * 1.3 - deffPlayer
    if classPlayer == 3: 
       hpPlayer -= attBot * 1.3 - deffPlayer
   if classBot == 3:
    if classPlayer == 1: 
       hpPlayer -= attBot - deffPlayer
    if classPlayer == 2:
       hpPlayer -= attBot * 1.2 - deffPlayer
    if classPlayer == 3: 
       hpPlayer -= attBot * 1.2 - deffPlayer
   print('Ваше ХП теперь %s' % hpPlayer)
   if hpPlayer <= 0:
      print('Вы проиграли!')
      break
   if hpBot <= 0:
      print('Вы выиграли!')
      break
r = int(input('    '))