import os
from CharGenDefs import *

os.system('clear')
while True:
  newChar = input('\nNew character? \'yes\'/\'no\'\n > ')
  if newChar == 'yes':
    doAllTheThings()
    print(getRandomTextColor())
    print('Race:',Species,'    Class:',Class,'    Background:',Background,'    Name:',Name,'    Level:',str(Level))
    print()
    for i in range(6):
      print(statItems[i],str(statList[i])+'    ',end='')
    print()
    if extraSpeed != 0: print('\nSpeed:',str(Speed)+'ft walking and a',str(extraSpeed)+'ft',extraSpeedType,'speed')
    else: print('\nSpeed:',str(Speed)+'ft') 
    print('\nHit Di:',str(Level)+hitDi,'    Max Health:',str(Health)+'    Armor Class (unarmored): '+str(armorClass))
    print('\033[0;37;49m')
  elif newChar.isnumeric():
    for i in range(int(newChar)):
      doAllTheThings()
      print(getRandomTextColor())
      print('Race:',Species,'    Class:',Class,'    Background:',Background,'    Name:',Name,'    Level:',str(Level))
      print()
      for i in range(6):
        print(statItems[i],str(statList[i])+'    ',end='')
      print()
      if extraSpeed != 0: print('\nSpeed:',str(Speed)+'ft walking and a',str(extraSpeed)+'ft',extraSpeedType,'speed')
      else: print('\nSpeed:',str(Speed)+'ft') 
      print('\nHit Di:',str(Level)+hitDi,'    Max Health:',str(Health)+'    Armor Class (unarmored): '+str(armorClass))
      print('\033[0;37;49m')

'''Attempt at Char info formatting

Race: _____ Class: ______ Background: _____ Name: ______
Str: _ Dex: _ Con: _ Int: _ Wis: _ Cha: _
Speed: _ extra speed, other attribute idk
Hit Di: _ Max HP: _
* Basic Race description
* Basic Class description
* Basic Background description

needs spell mods and stuff for casting classes

Ask to export PDF containing full Char info (lots of dev and figuring out how for that part)
'''