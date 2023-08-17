import random, os, time

nameList = ['Steve','Bob','Perseus','Alex','Jayden','Owen','Charlie','Sarah','Lila','Gwen','Jameson','Yloxi','Giussepi','Rouge','Barb','Pal','Barnaby','Vier','']
speciesList = ['Human','Elf','Half-Elf','Half-Orc','Dwarf','Goblin','Herengon','Bugbear','Tiefling','Gnome','Halfling','Dragonborn','Changeling','Warforged','Aarakocra','Aasimar','Kenku','Firbolg','Genasi (Water)','Genasi (Fire)','Genasi (Earth)','Genasi (Air)','Goliath','Hobgoblin','Kalashtar','Kobold','Leonin','Lizardfolk','Tortle','Minotaur','Owlin','Tabaxi','Triton','Grung']
classList = ['Wizard','Sorcerer','Barbarian','Bard','Monk','Druid','Warlock','Fighter','Rogue','Ranger','Cleric','Paladin','Artificer']

# order here corresponds to character sheet
stre = 0
dex = 0
con = 0
inte = 0
wis = 0
cha = 0


statList = [stre, dex, con, inte, wis, cha] # holds actual stat values
unassignedStatVals = [] # holds vals to be assigned to stats

# funcs to imitate dice rolls
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
def stat(): # makes a stat using 4d6 drop the lowest
  tempStatFindList = [statRoll(),statRoll(),statRoll(),statRoll()]
  tempStatFindList.remove(min(tempStatFindList))
  return tempStatFindList[0] + tempStatFindList[1] + tempStatFindList[2]
def genStatList(): # makes a list of the stat values which can be assigned later
  for i in range(7):
    unassignedStatVals.append(stat())

# Major, Secondary, and Dump assign highest (always), second highest (if there is an importatn secondary stat for the class), and lowest (for some classes)
def assignMajorStat():
  global stre, dex, con, inte, wis, cha
  if Class == 'Barbarian' or Class == 'Fighter':
    stre = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignSecondaryStat():
  if Class == 'Monk' or Class == 'Rogue' or Class == 'Ranger':
    dex = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignSecondaryStat():
  if Class == '':
    con = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignSecondaryStat():
  if Class == 'Wizard' or Class == 'Artificer':
    inte = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignSecondaryStat():
  if Class == 'Druid' or Class == 'Cleric':
    wis = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignSecondaryStat():
  if Class == 'Sorcerer' or Class == 'Paladin' or Class == 'Bard' or Class == 'Warlock':
    cha = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignSecondaryStat():
  global stre, dex, con, inte, wis, cha
  if Class == '':
    stre = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignSecondaryStat():
  if Class == 'Monk' or Class == 'Fighter' or Class == '':
    dex = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignSecondaryStat():
  if Class == 'Barbarian' or Class == 'Cleric':
    con = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignSecondaryStat():
  if Class == 'Rogue':
    inte = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignSecondaryStat():
  if Class == '':
    wis = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignSecondaryStat():
  if Class == '':
    cha = max(unassignedStatVals)
    unassignedStatVals.remove(max(unassignedStatVals))
def assignDumpStat():
  global stre, dex, con, inte, wis, cha
  if Class == 'Wizard':
    stre = min(unassignedStatVals)
    unassignedStatVals.remove(min(unassignedStatVals))
  if Class == '':
    dex = min(unassignedStatVals)
    unassignedStatVals.remove(min(unassignedStatVals))
  if Class == 'Sorcerer':
    con = min(unassignedStatVals)
    unassignedStatVals.remove(min(unassignedStatVals))
  if Class == 'Barbarian':
    inte = min(unassignedStatVals)
    unassignedStatVals.remove(min(unassignedStatVals))
  if Class == '':
    wis = min(unassignedStatVals)
    unassignedStatVals.remove(min(unassignedStatVals))
  if Class == '':
    cha = min(unassignedStatVals)
    unassignedStatVals.remove(min(unassignedStatVals))
def assignRemainingStats(): # the name is pretty clear, too long tho
  global stre, dex, con, inte, wis, cha
  while len(unassignedStatVals) != 0:
    if stre == 0:
      stre = unassignedStatVals[0]
      del unassignedStatVals[0]
    if dex == 0:
      dex = unassignedStatVals[0]
      del unassignedStatVals[0]
    if con == 0:
      con = unassignedStatVals[0]
      del unassignedStatVals[0]
    if inte == 0:
      inte = unassignedStatVals[0]
      del unassignedStatVals[0]
    if wis == 0:
      wis = unassignedStatVals[0]
      del unassignedStatVals[0]
    if cha == 0:
      cha = unassignedStatVals[0]
      del unassignedStatVals[0]
def assignStats():
  genStatList()
  assignMajorStat()
  assignSecondaryStat()
  assignDumpStat()
  assignRemainingStats()



def getMod(stat): #figures the modifier given a stat between 6 and 20 (could be done better with a var and a for loop up from 6 by 2)
  if 6 <= stat <= 7:
    return '(-2)'
  if 8 <= stat <= 9:
    return '(-1)'
  if 10 <= stat <= 11:
    return '(+0)'
  if 12 <= stat <= 13:
    return '(+1)'
  if 14 <= stat <= 15:
    return '(+2)'
  if 16 <= stat <= 17:
    return '(+3)'
  if 18 <= stat <= 19:
    return '(+4)'
  if stat == 20:
    return '(+5)'

Class = classList[random.randint(0,len(classList)-1)]
Species = speciesList[random.randint(0,len(speciesList)-1)]
Name = nameList[random.randint(0,len(nameList)-1)]

# assigning stats


def genChar():
    print(Name,'is a',Species,Class,', with strength:',str(stre)+getMod(stre),', wisdom:',str(wis)+getMod(wis),', intelligence:',str(inte)+getMod(inte),', constitution:',str(con)+getMod(con),', dexterity:',str(dex)+getMod(dex),', and charisma:',str(cha)+getMod(cha))

os.system('clear')
print('Random Character Generator!\n')
print("Warning: somewhat based off of stereoptypes and memes\n")

assignStats()
print(stre,dex,con,inte,wis,cha)
genChar()
while True:
    if input('\nanother character? > ') == 'yes':
        print()
        Class = classList[random.randint(1,len(classList)-1)]
        Species = speciesList[random.randint(1,len(speciesList)-1)]
        Name = nameList[random.randint(1,len(nameList)-1)]
        assignStats()
        genChar()

''' *contains archived racial stat bonus assignment for second version

def assignSpeciesFeatures():
  global stre, dex, con, inte, wis, cha, Species, Speed, Height, Age, Size, originBook, Languages, extraTraits, extraSpeed, extraSpeedType
  if Species == 'Dwarf (Hill)':
    con += 2
    wis += 1
    Speed = 25
    Languages.append('Aarakocra')
    Languages.append('Auran')
    Languages.append('Dwarvish')
  if Species == 'Dwarf (Mountain)':
    con += 2
    stre += 2
    Speed = 25
    Languages.append('Dwarvish')
  if Species == 'Elf (High)':
    dex += 2
    inte += 1
    Languages.append('Elvish')
  if Species == 'Elf (Wood)':
    dex += 2
    wis += 1
    Languages.append('Elvish')
  if Species == 'Elf (Drow)':
    dex += 2
    cha += 1
    Languages.append('Elvish')
  if Species == 'Halfling (Lightfoot)':
    dex += 2
    cha += 1
    Size = 'Small'
    Speed = 25
    Languages.append('Halfling')
  if Species == 'Halfling (Stout)':
    con += 2
    wis += 1
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
    stre += 2
    cha += 1
    Languages.append('Draconic')
  if Species == 'Gnome (Forest)':
    inte += 2
    dex += 1
    Size = 'Small'
    Speed = 25
    Languages.append('Gnomish')
  if Species == 'Gnome (Rock)':
    inte  += 2
    con += 1
    Size = 'Small'
    Speed = 25
    Languages.append('Gnomish')
  if Species == 'Half-Orc':
    stre += 2
    con += 1
    Languages.append('Orcish')
  if Species == 'Tiefling':
    cha += 2
    inte += 1
    Languages.append('Infernal')
  if Species == 'Elf (Eladrin)':
    dex += 2
    inte += 1
    Languages.append('Elvish')
  if Species == 'Aarakocra':
    dex += 2
    wis += 1
    Speed = 25
    extraSpeed = 50
    extraSpeedType = 'Fly'
  if Species == 'Gnome (Deep)':
    inte += 2
    dex += 1
    Size = 'Small'
    Speed = 25
    Languages.append('Gnomish')
    Languages.append('Undercommon')
  if Species == 'Genasi (Air)':
    con += 2
    dex += 1
    Languages.append('Primordial')
  if Species == 'Genasi (Earth)':
    con += 2
    stre += 1
    Languages.append('Primordial')
  if Species == 'Genasi (Fire)':
    con += 2
    inte += 1
    Languages.append('Primordial')
  if Species == 'Genasi (Water)':
    con += 2
    wis += 1
    Languages.append('Primordial')
    extraSpeed = 30
    extraSpeedType = 'Swim'
  if Species == 'Goliath':
    stre += 2
    con += 1
    Languages.append('Giant')
  if Species == 'Halfling (Ghostwise)':
    inte += 2
    con += 1
    Size = 'Small'
    Speed = 25
    Languages.append('Halfling')
  if Species == 'Gnome (Deep, Svirnefblin)':
    inte += 2
    con += 1
    Size = 'Small'
    Speed = 25
    Languages.append('Gnomish')
  if Species == 'Tiefling (Feral)':
    con += 2
    inte += 1
    Languages.append('Infernal')
  if Species == 'Aasimar (Protector)':
    cha += 2
    wis += 1
    Languages.append('Celestial')
  if Species == 'Aasimar (Scourge)':
    cha += 2
    con += 1
    Languages.append('Celestial')
  if Species == 'Aasimar (Fallen)':
    cha += 2
    stre += 1
    Languages.append('Celestial')
  if Species == 'Firbolg':
    wis += 2
    stre += 1
    Languages.append('Elvish')
    Languages.append('Giant')
  if Species == 'Kenku':
    dex += 2
    wis += 1
    Languages.append('Auran')
    Languages.append('Exclusively in Mimicry')
  if Species == 'Lizardfolk':
    con += 2
    wis += 1
    extraSpeed = 30
    extraSpeedType = 'Swim'
    Languages.append('Draconic')
  if Species == 'Tabaxi':
    dex += 2
    cha += 1
  if Species == 'Triton':
    stre += 1
    con += 1
    cha += 1
    extraSpeed = 30
    extraSpeedType = 'Swim'
    Languages.append('Primordial')
  if Species == 'Bugbear':
    stre += 2
    dex += 1
    Languages.append('Goblin')
  if Species == 'Goblin':
    dex += 2
    con += 1
    Size = 'Small'
    Speed = 25
    Languages.append('Goblin')
  if Species == 'Hobgoblin':
    dex += 2
    inte += 1
    Languages.append('Goblin')
  if Species == 'Kobold':
    dex += 2
    Size = 'Small'
    Languages.append('Draconic')
  if Species == 'Orc':
    stre += 2
    dex += 1
    Languages.append('Orcish')
  if Species == 'Yuan-Ti':
    cha += 2
    inte += 1
    Languages.append('Abyssal')
    Languages.append('Draconic')
  if Species == 'Elf (Sea)':
    con += 2
    dex += 1
    extraSpeed = 30
    extraSpeedType = 'Swim'
    Languages.append('Elvish')
  if Species == 'Elf (Shadar-Kai)':
    con += 2
    dex += 1
    Languages.append('Elvish')
  if Species == 'Dwarf (Duergar)':
    dex += 2
    stre += 1
    Speed = 25
    Languages.append('Dwarvish')
    Languages.append('Undercommon')
  if Species == 'Githyanki':
    stre += 2
    inte += 1
  if Species == 'Githzerai':
    wis += 2
    inte += 1
  if Species == 'Tortle':
    stre += 2
    wis += 1
    Speed = 25
    extraSpeed = 35
    extraSpeedType = 'Swim'
    Languages.append('Aquan')
  if Species == 'Verdan':
    cha += 2
    con += 1
  if Species == 'Kalashtar':
    wis += 2
    cha += 1
  if Species == 'Centaur':
    stre += 2
    wis += 1
  if Species == 'Minotaur':
    stre += 2
    dex += 1
  if Species == 'Leonin':
    dex += 2
    con += 1
  if Species == 'Satyr':
    cha += 2
    dex += 1
  if Species == 'Half-Elf':
    Languages.append('Elvish')
  if Species == 'Changeling':
    return 'Err'
  if Species == 'Warforged':
    return 'Err'
  if Species == 'Harengon':
    return "Err"
  if Species == 'Owlin':
    return 'Err'
  if Species == 'Grung':
    Languages.append('Grung')
    Size = 'Small'
    Speed = 25
    extraSpeed = 25
    extraSpeedType = 'Crawl'
'''
''' *contains potential for assigning stats to specific ruled stat bonus races in v3 (defs and run)

if Class == 'Wizard' or Class == 'Artificer':
        inte += max(statHoldList)
      elif Class == 'Sorcerer' or Class == 'Bard' or Class == 'Warlock':
        cha += max(statHoldList)
      elif Class == 'Barbarian' or Class == 'Paladin' or Class == 'Fighter':
        stre += max(statHoldList)
      elif (Class == 'Monk' or Class == 'Rogue' or Class == 'Ranger'):
        dex += max(statHoldList)
      elif Class == 'Druid' or Class == 'Cleric':
        wis += max(statHoldList)
        statHoldList.remove(max(statHoldList)) #primary stats
      if Class == 'Barbarian':
        con += max(statHoldList)
        statHoldList.remove(max(statHoldList))
      elif Class == 'Paladin':
        cha += max(statHoldList)
        statHoldList.remove(max(statHoldList))
      elif Class == 'Fighter':
        dex += max(statHoldList)
        statHoldList.remove(max(statHoldList))
    elif Species == 'Kobold':
      if Class == 'Wizard' or Class == 'Artificer':
        inte += max(statHoldList)
      elif Class == 'Sorcerer' or Class == 'Bard' or Class == 'Warlock':
        cha += max(statHoldList)
      elif Class == 'Barbarian' or Class == 'Paladin' or Class == 'Fighter':
        stre += max(statHoldList)
      elif (Class == 'Monk' or Class == 'Rogue' or Class == 'Ranger'):
        dex += max(statHoldList)
      elif Class == 'Druid' or Class == 'Cleric':
        wis += max(statHoldList)
        statHoldList.remove(max(statHoldList)) #primary stats
      if Class == 'Barbarian':
        con += max(statHoldList)
        statHoldList.remove(max(statHoldList))
      elif Class == 'Paladin':
        cha += max(statHoldList)
        statHoldList.remove(max(statHoldList))
      elif Class == 'Fighter':
        dex += max(statHoldList)
        statHoldList.remove(max(statHoldList))
    elif Species == 'Triton':
      if Class == 'Wizard' or Class == 'Artificer':
        inte += max(statHoldList)
      elif Class == 'Sorcerer' or Class == 'Bard' or Class == 'Warlock':
        cha += max(statHoldList)
      elif Class == 'Barbarian' or Class == 'Paladin' or Class == 'Fighter':
        stre += max(statHoldList)
      elif (Class == 'Monk' or Class == 'Rogue' or Class == 'Ranger'):
        dex += max(statHoldList)
      elif Class == 'Druid' or Class == 'Cleric':
        wis += max(statHoldList)
        statHoldList.remove(max(statHoldList)) #primary stats
      if Class == 'Barbarian':
        con += max(statHoldList)
        statHoldList.remove(max(statHoldList))
      elif Class == 'Paladin':
        cha += max(statHoldList)
        statHoldList.remove(max(statHoldList))
      elif Class == 'Fighter':
        dex += max(statHoldList)
        statHoldList.remove(max(statHoldList))'''