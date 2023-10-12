signs = {
    'red':input('red sign: '),
    'yellow':input('yellow sign: '),
    'blue':input('blue sign: '),
    'green':input('green sign: ')
}

CHAR_TO_TENT = {
    'R':'red',
    'Y':'yellow',
    'B':'Blue',
    'G':'green'
}

def get_where(from_where, tent_char):
    if tent_char == 'H':
        return from_where
    else:
        return CHAR_TO_TENT[tent_char]
    
solutions = []

for i in range(4):
    fails = False
    true_tent = list(signs.keys())[i]
    bag_loc = None

    for j in range(4):
        if signs[true_tent][0] == 'T':
            if bag_loc == None:
                bag_loc = get_where(true_tent, signs[true_tent][1])
            else:
                fails = True
    
    if fails:
        solutions.append({'true_tent':true_tent, 'bag_loc':bag_loc})

print(solutions)
