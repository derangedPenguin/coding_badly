import json


with open('HypixelAPITesting/itemNamesAlphabetical.json','r') as file:
    original_dict = json.loads(file.read())
    keys = sorted(list(original_dict.keys()))
    new_dict = {}

    for i in keys:
        new_dict[i] = original_dict[i]

with open('HypixelAPITesting/itemNamesAlphabetical.json','w') as file:
    file.write(json.dumps(new_dict,indent=4))