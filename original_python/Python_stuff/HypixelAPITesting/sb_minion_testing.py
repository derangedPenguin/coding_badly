from sb_minion_lib import minions
import requests as req, time, json, os, PySimpleGUI as sg

sg.theme('DarkGreen4')
layout = [
    [sg.T('Skyblock Minion Utils',size=(30,1),font='Helvetica 30 bold')],
    [sg.B('get all crafted minions',size=(15,1),key='-GET_GENS-')],
    [sg.T('',key='-OUTPUT-')]
]
window = sg.Window('window',layout)

key='6fee679e-f96d-4352-8782-4aa221007058'
uuid='22899dea-3bb5-4035-9a38-26526d4450fa' #gAMER12008 player id
stripped_uuid = '22899dea3bb540359a3826526d4450fa'
responseDict = {}

responseDict = req.get("https://api.hypixel.net/skyblock/profile?key={}&uuid={}&profile={}".format(key,uuid,stripped_uuid)).json()
responseTxt = json.dumps(responseDict,indent=4)

craftedGens = sorted(responseDict['profile']['members'][stripped_uuid]['crafted_generators'])

# convert crafted gens list to dict of crafted gens with their highest level
holdStr = ''
highestGens = {}
for i in craftedGens:
    highestGens[i[:-2]] = i[-2:]
    if highestGens[i[:-2]][0] == '_':
        highestGens[i[:-2]] = int(highestGens[i[:-2]][1])
    else:
        highestGens[i[:-2]] = int(highestGens[i[:-2]])
genTypes = list(highestGens.keys())
for i in range(len(genTypes)-1):
    if genTypes[i] + '_' == genTypes[i+1]:
        highestGens[genTypes[i]] = highestGens[genTypes[i+1]]
        del highestGens[genTypes[i+1]]

def get_cute_name(name):
    name = name.lower()
    if '_' in name:
        name = name.replace(name[name.index('_')+1], name[name.index('_')+1].upper(),1)
        name = name.replace(name[name.index('_')],' ')
    name = name.replace(name[0],name[0].upper(),1)
    return name


options = ['get list of crafted minions and highest levels (Enter \'1\')','get required materials and cost of minion upgrades Enter (\'2\')']

while True: #control loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == '-GET_GENS-':
        window['-OUTPUT-'].update(json.dumps(highestGens,indent=4))

window.close()