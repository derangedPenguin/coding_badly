from pygame import time

import json

clock = time.Clock()

base_data = json.loads(open('data.json', 'r').read())

counter = base_data['counter']

while True:
    with open('data.json') as file:
        if json.loads(file.read())['last_accessor'] == 'py':
            continue
    
    counter += 1
    base_data['counter'] = counter
    base_data['last_accessor'] = 'py'
    with open('data.json', 'w') as file:
        file.write(json.dumps(base_data))
    
    clock.tick(10)
