signs = {
    'red':input('red sign: '),
    'yellow':input('yellow sign: '),
    'blue':input('blue sign: '),
    'green':input('green sign: ')
} # keys method serves as list of tents

CHAR_TO_TENT = {
    'R':'red',
    'Y':'yellow',
    'B':'Blue',
    'G':'green'
}

def get_where(from_where, tent_char): #gets input 
    if tent_char == 'H':
        return from_where
    else:
        return CHAR_TO_TENT[tent_char]
    
solutions = []

'''
for each tent, treat current tent as true (invert all other statements), evaluate all statements for conflicts, if found, current tent is lying
'''

for tent in range(4):
    current_is_false = False
    true_tent = list(signs.keys())[tent]
    bag_loc = None

    for sign in signs.values():
        if sign[0] == 'T': # in this case, T is negative, N is positive
            if bag_loc == None or bag_loc == get_where(true_tent, sign[1]):
                bag_loc == get_where(true_tent, sign[1])
            else:
                current_is_false = True

    if bag_loc != None:
        solutions.append({"true_tent":true_tent, 'bag_loc':bag_loc})


print(solutions)