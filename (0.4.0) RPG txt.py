from random import randint      # импорт нужных команд (рандом и сон)
from time import sleep

stHealPlayer = 0
stHealBot = 0
abilityKnight = 0

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
      print('Описание: \n Имеет большое количество хп(145) и брони(5). \n Весь получаемый урон понижен на 20%.\nСпособность Железная выдержка: увеличивает броню на 2 каждые 8 ходов.')
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
       print('Описание: \n Имеет обычное количество хп(110) и отсутсвие брони. \n Увеличивает урон на 20%.\n Способность Магический Щит: увеличивает броню на 2 за счет очков восстановления(5).')
       print('Выбрать?')
       g = int(input('1/2'))
       if g == 1:
          classPlayer = r
          break
       if g == 2:
          print('...')

if classPlayer == 1:
   hpPlayer = 185
   attPlayer = randint(15,20)
   deffPlayer = 2
if classPlayer == 2:
   hpPlayer = 100
   attPlayer = randint(10,25)
   deffPlayer = 1
if classPlayer == 3:
   hpPlayer = 130
   attPlayer = randint(15,30)
   deffPlayer = 160

classBot = randint(1,3)

if classBot == 1:
   hpBot = 185
   attBot = randint(15,20)
   deffBot = 2
if classBot == 2:
   hpBot = 100
   attBot = randint(10,25)
   deffBot = 1
if classBot == 3:
   hpBot = 130
   attBot = randint(15,30)
   deffBot = 1

z = int(input('1(yes)/2(no)'))
if classBot == 1:
   print('Вы против Рыцаря!')
if classBot == 2:
   print('Вы против Лучника!')
if classBot == 3:
   print('Вы против Мага!')
print('-----------------------------------------')
while z == 1:
   abilityKnight += 1
   stHealBot += 1
   stHealPlayer += 1
   if classPlayer == 1:
      print('Выберите атаку: \n 1. Удар \n2. Хил')
      atPlayer = int(input('Выбор:'))
      if atPlayer == 1 and classBot == 1: 
         hpBot -= randint(15,20) * 0.8 - deffBot
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 2: 
         hpBot -= randint(15,20) - deffBot
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 3: 
         hpBot -= randint(15,20) - deffBot
         print('ХП врага = %s' % hpBot)
   if classPlayer == 2:
      print('Выберите атаку: \n 1. Выстрел \n2. Хил')
      atPlayer = int(input('Выбор:'))
      if atPlayer == 1 and classBot == 1: 
         hpBot -= randint(10,25) * 1.1 - deffBot
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 2: 
         hpBot -= randint(10,25) * 1.3 - deffBot
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 3: 
         hpBot -= randint(10,25) * 1.3 - deffBot
         print('ХП врага = %s' % hpBot)
   if classPlayer == 3:
      print('Выберите атаку: \n 1. Магия \n2. Хил \n 3. Способность')
      atPlayer = int(input('Выбор:'))
      if atPlayer == 1 and classBot == 1: 
         hpBot -= randint(20,25) - deffBot
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 2: 
         hpBot -= randint(20,25) * 1.2 - deffBot
         print('ХП врага = %s' % hpBot)
      if atPlayer == 1 and classBot == 3: 
         hpBot -= randint(20,25) * 1.2 - deffBot
         print('ХП врага = %s' % hpBot)
   if atPlayer == 3 and classPlayer == 3 and stHealPlayer >= 5:
      print('Вы использовали навык Магический Щит.')
      deffPlayer += 2
      stHealPlayer -= 5
   elif atPlayer == 3 and classPlayer == 3 and stHealPlayer < 5:
      print('Вам не хватает очков восстановления! Требуется 5, сейчас %s' % stHealPlayer)
   if abilityKnight == 8 and classPlayer == 1:
      deffPlayer += 2
      print('У вас сработал навык Железная выдержка, увеличивший вашу броню до %s' % deffPlayer)
      abilityKnight = 0
   if atPlayer == 2 and stHealPlayer >= 2:
      stHealPlayer -= 2
      heal = randint(15,35)
      hpPlayer += heal 
      print('Вы восстановили себя на %s ХП.' % heal)
      print('Ваше ХП теперь %s.' % hpPlayer)
   elif atPlayer == 2:
      print('У вас не хватает очков восстановления!\n Требуется 2, сейчас %s.' % stHealPlayer)
   if hpBot > 60:
      print('Бот атакует!')
      if classBot == 1:
         if classPlayer == 1: 
            hpPlayer -= randint(15,20) * 0.8 - deffPlayer
         if classPlayer == 2: 
            hpPlayer -= randint(15,20) - deffPlayer
         if classPlayer == 3: 
            hpPlayer -= randint(15,20) - deffPlayer
      if classBot == 2:
         if classPlayer == 1: 
            hpPlayer -= randint(10,25) * 1.1 - deffPlayer
         if classPlayer == 2: 
            hpPlayer -= randint(10,25) * 1.3 - deffPlayer
         if classPlayer == 3: 
            hpPlayer -= randint(10,25) * 1.3 - deffPlayer
      if classBot == 3:
         if classPlayer == 1: 
            hpPlayer -= randint(20,25) - deffPlayer
         if classPlayer == 2:
            hpPlayer -= randint(20,25) * 1.2 - deffPlayer
         if classPlayer == 3: 
            hpPlayer -= randint(20,25) * 1.2 - deffPlayer
   if hpBot <= 60 and stHealBot >= 2:
      stHealBot -= 2
      heal = randint(15,35)
      hpBot += heal 
      print('Бот восстановил себя на %s ХП.' % heal)
      print('ХП бота теперь %s.' % hpBot)
   else:
      if classBot == 1:
         if classPlayer == 1: 
            hpPlayer -= randint(10,20) * 0.8 - deffPlayer
         if classPlayer == 2: 
            hpPlayer -= randint(10,20) - deffPlayer
         if classPlayer == 3: 
            hpPlayer -= randint(10,20) - deffPlayer
      if classBot == 2:
         if classPlayer == 1: 
            hpPlayer -= randint(10,25) * 1.1 - deffPlayer
         if classPlayer == 2: 
            hpPlayer -= randint(10,25) * 1.3 - deffPlayer
         if classPlayer == 3: 
            hpPlayer -= randint(10,25) * 1.3 - deffPlayer
      if classBot == 3:
         if classPlayer == 1: 
            hpPlayer -= randint(15,30) - deffPlayer
         if classPlayer == 2:
            hpPlayer -= randint(15,30) * 1.2 - deffPlayer
         if classPlayer == 3: 
            hpPlayer -= randint(15,30) * 1.2 - deffPlayer
   print('Ваше ХП теперь %s' % hpPlayer)
   if hpPlayer <= 0:
      print('Вы проиграли!')
      break
   if hpBot <= 0:
      print('Вы выиграли!')
      break
r = int(input('    '))