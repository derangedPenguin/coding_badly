import random, os

nameList = ['Steve','Bob','Perseus','Alex','Jayden','Owen','Charlie','Sarah','Lila','Gwen','Jameson','Yloxi','Giussepi','Rouge','Barb','Pal','Barnaby','Ebenezer','Vier','George','Jon','Jo','Harold','Lukas','Stephan','Stef','Clara','Rory','Luke','Luna','Saphire','Emerald','Graham','Magnus','Sir','Lawson','Jeffrey']
speciesList = ['Human','Elf (High)','Elf (Wood)','Elf (Drow)','Elf (Eladrin)','Elf (Shadar-Kai)','Elf (Sea)','Half-Elf','Half-Orc','Orc','Dwarf (Hill)','Dwarf (Mountain)','Dwarf (Duergar)','Goblin','Harengon','Bugbear','Tiefling','Tiefling (Feral)','Gnome (Forest)','Gnome (Rock)','Gnome (Deep)','Gnome (Deep, Svirnefblin)','Halfling (Lightfoot)','Halfling (Stout)','Halfling (Ghostwise)','Dragonborn','Changeling','Warforged','Aarakocra','Aasimar (Protector)','Aasimar (Scourge)','Aasimar (Fallen)','Kenku','Firbolg','Genasi (Water)','Genasi (Fire)','Genasi (Earth)','Genasi (Air)','Goliath','Hobgoblin','Kalashtar','Kobold','Leonin','Lizardfolk','Tortle','Minotaur','Owlin','Tabaxi','Triton','Grung','Yuan-Ti','Githyanki','Githzerai','Verdan']
classList = ['Wizard','Sorcerer','Barbarian','Bard','Monk','Druid','Warlock','Fighter','Rogue','Ranger','Cleric','Paladin','Artificer']
alignmentList = ['Lawful Good','Nuetral Good','Chaotic Good','Lawful Nuetral','True Nuetral','Chaotic Nuetral','Lawful Evil','Nuetral Evil','Chaotic Evil','Chaotic Stupid']
backgroundList = ['Acolyte','Charlatan','Criminal / Spy','Entertainer','Folk Hero','Gladiator','Guild Artisan / Guild Merchant','Hermit','Knight','Noble','Outlander','Pirate','Sage','Sailor','Soldier','Urchin']

'''
*species and race used interchangeable, exclusively species in code so far (02/11/23 - 2:01pm)
Needs to be assigned:
- extra traits from species
- (a lot) more names
- proficiencies (skill and saving throws)
- figure age and height (based on species)
- assign origin book for race at minimum

'''

stre = 0
dex = 0
con = 0
inte = 0
wis = 0
cha = 0

streMod = 0
dexMod = 0
conMod = 0
inteMod = 0
wisMod = 0
chaMod = 0

Class = ''
Name = ''
Species = ''
Level = 1

armorClass = 10
Health = 0
hitDi = ''
Alignment = ''
extraTraits = ''
Height = 0
Age = 0
Speed = 30
extraSpeed = 0
extraSpeedType = ''
Size = 'Medium'
Languages = ['Common']
originBook = ''
Background = ''

statList = [stre, dex, con, inte, wis, cha]
statHoldList = []

def newCharDetails():
  global Class, Name, Species, Alignment, Background
  Class = classList[random.randint(0,len(classList)-1)]
  Name = nameList[random.randint(0,len(nameList)-1)]
  Species = speciesList[random.randint(0,len(speciesList)-1)]
  Alignment = alignmentList[random.randint(0,len(alignmentList)-1)]
  Background = backgroundList[random.randint(0,len(backgroundList)-1)]

def d4(mod):
  return random.randint(1,4) + mod
def d6(mod):
  return random.randint(1,6) + mod
def d8(mod):
  return random.randint(1,8) + mod
def d10(mod):
  return random.randint(1,10) + mod
def d12(mod):
  return random.randint(1,12) + mod
def d20(mod):
  return random.randint(1,20) + mod
def d100(mod):
  return random.randint(1,100) + mod

def statRoll(): # same as d6, but doesn't include ones, as those are re-rolled for stats
  return random.randint(2,6)
def stat(): # makes a stat using 4d6 drop the lowest (and reroll ones) method
  tempStatFindList = [statRoll(),statRoll(),statRoll(),statRoll()]
  tempStatFindList.remove(min(tempStatFindList))
  return tempStatFindList[0] + tempStatFindList[1] + tempStatFindList[2]
def genStatList(): # makes a list of the stat values which can be assigned later
  for i in range(6):
    statHoldList.append(stat())

def assignSpeciesFeatures():
  global stre, dex, con, inte, wis, cha, Species, Speed, Height, Age, Size, originBook, Languages, extraTraits, extraSpeed, extraSpeedType
  if Species == 'Dwarf (Hill)':
    Speed = 25
    Languages.append('Aarakocra')
    Languages.append('Auran')
    Languages.append('Dwarvish')
  if Species == 'Dwarf (Mountain)':
    Speed = 25
    Languages.append('Dwarvish')
  if Species == 'Elf (High)':
    Languages.append('Elvish')
  if Species == 'Elf (Wood)':
    Languages.append('Elvish')
  if Species == 'Elf (Drow)':
    Languages.append('Elvish')
  if Species == 'Halfling (Lightfoot)':
    Size = 'Small'
    Speed = 25
    Languages.append('Halfling')
  if Species == 'Halfling (Stout)':
    Size = 'Small'
    Speed = 25
    Languages.append('Halfling')
  if Species == 'Human':
    stre += 1
    dex += 1
    con += 1
    inte += 1
    wis += 1
    cha += 1
  if Species == 'Dragonborn':
    Languages.append('Draconic')
  if Species == 'Gnome (Forest)':
    Size = 'Small'
    Speed = 25
    Languages.append('Gnomish')
  if Species == 'Gnome (Rock)':
    Size = 'Small'
    Speed = 25
    Languages.append('Gnomish')
  if Species == 'Half-Orc':
    Languages.append('Orcish')
  if Species == 'Tiefling':
    Languages.append('Infernal')
  if Species == 'Elf (Eladrin)':
    Languages.append('Elvish')
  if Species == 'Aarakocra':
    Speed = 25
    extraSpeed = 50
    extraSpeedType = 'Fly'
  if Species == 'Gnome (Deep)':
    Size = 'Small'
    Speed = 25
    Languages.append('Gnomish')
    Languages.append('Undercommon')
  if Species == 'Genasi (Air)':
    Languages.append('Primordial')
  if Species == 'Genasi (Earth)':
    Languages.append('Primordial')
  if Species == 'Genasi (Fire)':
    Languages.append('Primordial')
  if Species == 'Genasi (Water)':
    Languages.append('Primordial')
    extraSpeed = 30
    extraSpeedType = 'Swim'
  if Species == 'Goliath':
    Languages.append('Giant')
  if Species == 'Halfling (Ghostwise)':
    Size = 'Small'
    Speed = 25
    Languages.append('Halfling')
  if Species == 'Gnome (Deep, Svirnefblin)':
    Size = 'Small'
    Speed = 25
    Languages.append('Gnomish')
  if Species == 'Tiefling (Feral)':
    Languages.append('Infernal')
  if Species == 'Aasimar (Protector)':
    Languages.append('Celestial')
  if Species == 'Aasimar (Scourge)':
    Languages.append('Celestial')
  if Species == 'Aasimar (Fallen)':
    Languages.append('Celestial')
  if Species == 'Firbolg':
    Languages.append('Elvish')
    Languages.append('Giant')
  if Species == 'Kenku':
    Languages.append('Auran')
    Languages.append('Exclusively in Mimicry')
  if Species == 'Lizardfolk':
    extraSpeed = 30
    extraSpeedType = 'Swim'
    Languages.append('Draconic')
  if Species == 'Tabaxi':
    extraTraits = ''
  if Species == 'Triton':
    stre += 1
    con += 1
    cha += 1
    extraSpeed = 30
    extraSpeedType = 'Swim'
    Languages.append('Primordial')
  if Species == 'Bugbear':
    Languages.append('Goblin')
  if Species == 'Goblin':
    Size = 'Small'
    Speed = 25
    Languages.append('Goblin')
  if Species == 'Hobgoblin':
    Languages.append('Goblin')
  if Species == 'Kobold':
    dex += 2
    Size = 'Small'
    Languages.append('Draconic')
  if Species == 'Orc':
    Languages.append('Orcish')
  if Species == 'Yuan-Ti':
    Languages.append('Abyssal')
    Languages.append('Draconic')
  if Species == 'Elf (Sea)':
    extraSpeed = 30
    extraSpeedType = 'Swim'
    Languages.append('Elvish')
  if Species == 'Elf (Shadar-Kai)':
    Languages.append('Elvish')
  if Species == 'Dwarf (Duergar)':
    Speed = 25
    Languages.append('Dwarvish')
    Languages.append('Undercommon')
  if Species == 'Githyanki':
    extraTraits = ''
  if Species == 'Githzerai':
    extraTraits = ''
  if Species == 'Tortle':
    Speed = 25
    extraSpeed = 35
    extraSpeedType = 'Swim'
    Languages.append('Aquan')
  if Species == 'Verdan':
    extraTraits = ''
  if Species == 'Kalashtar':
    extraTraits = ''
  if Species == 'Centaur':
    extraTraits = ''
  if Species == 'Minotaur':
    extraTraits = ''
  if Species == 'Leonin':
    extraTraits = ''
  if Species == 'Satyr':
    extraTraits = ''
  if Species == 'Half-Elf':
    Languages.append('Elvish')
  if Species == 'Changeling':
    extraTraits = ''
  if Species == 'Warforged':
    extraTraits = ''
  if Species == 'Harengon':
    extraTraits = ''
  if Species == 'Owlin':
    extraTraits = ''
  if Species == 'Grung':
    extraTraits = ''
    Languages.append('Grung')
    Size = 'Small'
    Speed = 25
    extraSpeed = 25
    extraSpeedType = 'Crawl'
#(weird) Half-elf, Changeling, warforged, Harengon, Owlin, Grung, - should probably change it to custom stat bonuses for all

def assignStats():
  global stre, dex, con, inte, wis, cha, Class, Species, statHoldList
  if Species != 'Human' and Species != 'Kobold' and Species != 'Triton' and max(statHoldList) != 18 and max(statHoldList) != 17:
    if Class == 'Wizard' or Class == 'Artificer':
      inte += max(statHoldList)+2
    elif Class == 'Sorcerer' or Class == 'Bard' or Class == 'Warlock':
      cha += max(statHoldList)+2
    elif Class == 'Barbarian' or Class == 'Paladin' or Class == 'Fighter':
      stre += max(statHoldList)+2
    elif (Class == 'Monk' or Class == 'Rogue' or Class == 'Ranger'):
      dex += max(statHoldList)+2
    elif Class == 'Druid' or Class == 'Cleric':
      wis += max(statHoldList)+2
    statHoldList.remove(max(statHoldList))
    if Class == 'Barbarian':
      con += max(statHoldList)+1
      statHoldList.remove(max(statHoldList))
    elif Class == 'Paladin':
      cha += max(statHoldList)+1
      statHoldList.remove(max(statHoldList))
    elif Class == 'Fighter':
      dex += max(statHoldList)+1
      statHoldList.remove(max(statHoldList))
    if Species != 'Human' and Species != 'Triton' and Species != 'Kobold' and Class != 'Barbarian' and Class != 'Fighter' and Class != 'Paladin':
      statHoldList[random.randint(0,len(statHoldList)-1)] += 1
  else:
    if (Species == 'Human' or Species == 'Triton') and max(statHoldList) == 18:
      if Class == 'Wizard' or Class == 'Artificer':
        inte += max(statHoldList)+1
      elif Class == 'Sorcerer' or Class == 'Bard' or Class == 'Warlock':
        cha += max(statHoldList)+1
      elif Class == 'Barbarian' or Class == 'Paladin' or Class == 'Fighter':
        stre += max(statHoldList)+1
      elif (Class == 'Monk' or Class == 'Rogue' or Class == 'Ranger'):
        dex += max(statHoldList)+1
      elif Class == 'Druid' or Class == 'Cleric':
        wis += max(statHoldList)+1
    elif Species == 'Kobold' and max(statHoldList) == 17 and (Class == 'Rogue' or Class == 'Ranger' or Class == 'Monk'):
      dex += max(statHoldList) + 1
    elif Species == 'Kobold' and max(statHoldList) == 18 and (Class == 'Rogue' or Class == 'Ranger' or Class == 'Monk'):
      dex += max(statHoldList)
      


  # primary and secondary stats have been assigned based on class, rest will be random
  for i in range(len(statHoldList)):
    if stre < 6:
      stre += statHoldList[0]
      del statHoldList[0]
    elif dex < 6:
      dex += statHoldList[0]
      del statHoldList[0]
    elif con < 6:
      con += statHoldList[0]
      del statHoldList[0]
    elif inte < 6:
      inte += statHoldList[0]
      del statHoldList[0]
    elif wis < 6:
      wis += statHoldList[0]
      del statHoldList[0]
    elif cha < 6:
      cha += statHoldList[0]
      del statHoldList[0]

def setHitDi():
  global Class, hitDi
  if Class == 'Barbarian':
    def hitDi(): return d12()
    hitDi = 'd12'
  if Class == 'Fighter' or Class == 'Paladin' or Class == 'Ranger':
    def hitDi(): return d10()
    hitDi = 'd10'
  if Class == 'Artificer' or Class == 'Bard' or Class == 'Cleric' or Class == 'Druid' or Class == 'Monk' or Class == 'Rogue' or Class == 'Warlock':
    def hitDi(): return d8()
    hitDi = 'd8'
  if Class == 'Sorcerer' or Class == 'Wizard':
    def hitDi(): return d6()
    hitDi = 'd6'
def setHealth():
  global Health, hitDi
  Health = int(hitDi[1:])+int(getMod(con))

def setArmorClass():
  global armorClass, dex
  armorClass += getMod(dex)

def getRandomTextColor():
  tempVal = random.randint(0,255)
  tempVal1 = random.randint(0,255)
  tempVal2 = random.randint(0,255)
  return '\033[38;2;'+str(tempVal)+';'+str(tempVal1)+';'+str(tempVal2)+'m'

def getMod(stat): #figures the modifier given a stat between 6 and 20 (could be done better with a var and a for loop up from 6 by 2)
  if 6 <= stat <= 7:
    return int(-2)
  elif 8 <= stat <= 9:
    return int(-1)
  elif 10 <= stat <= 11:
    return int(0)
  elif 12 <= stat <= 13:
    return int(1)
  elif 14 <= stat <= 15:
    return int(2)
  elif 16 <= stat <= 17:
    return int(3)
  elif 18 <= stat <= 19:
    return int(4)
  elif stat == 20:
    return int(5)
  else:
    print('Stat Err',statHoldList,statList,Class,Species)
    return 300
def assignMods():
  global streMod, dexMod, conMod, inteMod, wisMod, chaMod
  streMod = getMod(stre)
  dexMod = getMod(dex)
  conMod = getMod(con)
  inteMod = getMod(inte)
  wisMod = getMod(wis)
  chaMod = getMod(cha)
def getModSign(stat):
  if stat >= 10:
    return '+'
  else:
    return ''

def doAllTheThings():
    global stre, dex, con, inte, wis, cha, Class, Name, Species, Alignment, statList, statHoldList, extraTraits, Speed, extraSpeed, extraSpeedType, Languages, Height, Age, Size, originBook, Background, armorClass, Health, hitDi, streMod, dexMod, conMod, inteMod, wisMod, chaMod
    stre = 0
    dex = 0
    con = 0
    inte = 0
    wis = 0
    cha = 0

    streMod = 0
    dexMod = 0
    conMod = 0
    inteMod = 0
    wisMod = 0
    chaMod = 0

    Class = ''
    Name = ''
    Species = ''
    Level = 1

    armorClass = 10
    Health = 0
    hitDi = ''
    Alignment = ''
    extraTraits = ''
    Height = 0
    Age = 0
    Speed = 30
    extraSpeed = 0
    extraSpeedType = ''
    Size = 'Medium'
    Languages = ['Common']
    originBook = ''
    Background = ''

    statList = [stre, dex, con, inte, wis, cha]
    statHoldList = []

    newCharDetails()
    assignSpeciesFeatures()
    setHitDi()
    genStatList()
    assignStats()
    assignMods()
    setHealth()
    setArmorClass()

os.system('clear')
while True:
  newChar =input('\nNew character? \'yes\'/\'no\'\n > ')
  if newChar == 'yes':
    doAllTheThings()
    print(getRandomTextColor())
    print('Race:',Species,'    Class:',Class,'    Background:',Background,'    Name:',Name,'    Level:',str(Level))
    print('\nStrength: '+str(stre)+'('+getModSign(stre)+str(streMod)+')'+'    Dexterity: '+str(dex)+'('+getModSign(dex)+str(dexMod)+')'+'    Constitution: '+str(con)+'('+getModSign(con)+str(conMod)+')'+'    Intelligence: '+str(inte)+'('+getModSign(inte)+str(inteMod)+')'+'    Wisdom: '+str(wis)+'('+getModSign(wis)+str(wisMod)+')'+'    Charisma: '+str(cha)+'('+getModSign(cha)+str(chaMod)+')')
    if extraSpeed != 0: print('\nSpeed:',str(Speed)+'ft walking and a',str(extraSpeed)+'ft',extraSpeedType,'speed')
    else: print('\nSpeed:',str(Speed)+'ft') 
    print('\nHit Di:',str(Level)+hitDi,'    Max Health:',str(Health)+'    Armor Class (unarmored): '+str(armorClass))
    print('\033[0;37;49m')
  elif newChar == '100':
    for i in range(100):
      doAllTheThings()
      print(getRandomTextColor())
      print('Race:',Species,'    Class:',Class,'    Background:',Background,'    Name:',Name,'    Level:',str(Level))
      print('\nStrength: '+str(stre)+'('+getModSign(stre)+str(streMod)+')'+'    Dexterity: '+str(dex)+'('+getModSign(dex)+str(dexMod)+')'+'    Constitution: '+str(con)+'('+getModSign(con)+str(conMod)+')'+'    Intelligence: '+str(inte)+'('+getModSign(inte)+str(inteMod)+')'+'    Wisdom: '+str(wis)+'('+getModSign(wis)+str(wisMod)+')'+'    Charisma: '+str(cha)+'('+getModSign(cha)+str(chaMod)+')')
      if extraSpeed != 0: print('\nSpeed:',str(Speed)+'ft walking and a',str(extraSpeed)+'ft',extraSpeedType,'speed')
      else: print('\nSpeed:',str(Speed)+'ft') 
      print('\nHit Di:',str(Level)+hitDi,'    Max Health:',str(Health)+'    Armor Class (unarmored): '+str(armorClass))
      print('\033[0;37;49m')
  elif newChar == 'all':
    for i in range(2500):
      doAllTheThings()
      print(getRandomTextColor())
      print('Race:',Species,'    Class:',Class,'    Background:',Background,'    Name:',Name,'    Level:',str(Level))
      print('\nStrength: '+str(stre)+'('+getModSign(stre)+str(streMod)+')'+'    Dexterity: '+str(dex)+'('+getModSign(dex)+str(dexMod)+')'+'    Constitution: '+str(con)+'('+getModSign(con)+str(conMod)+')'+'    Intelligence: '+str(inte)+'('+getModSign(inte)+str(inteMod)+')'+'    Wisdom: '+str(wis)+'('+getModSign(wis)+str(wisMod)+')'+'    Charisma: '+str(cha)+'('+getModSign(cha)+str(chaMod)+')')
      if extraSpeed != 0: print('\nSpeed:',str(Speed)+'ft walking and a',str(extraSpeed)+'ft',extraSpeedType,'speed')
      else: print('\nSpeed:',str(Speed)+'ft') 
      print('\nHit Di:',str(Level)+hitDi,'    Max Health:',str(Health)+'    Armor Class (unarmored): '+str(armorClass))
      print('\033[0;37;49m')

'''
Attempt at Char info formatting

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