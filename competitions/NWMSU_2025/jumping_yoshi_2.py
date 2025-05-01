'''yoshi 2'''
## Input
num_pebbles = int(input())
pebbles = tuple(int(i) for i in input().split())
max_dist = 0
jumps = {}

## Logic
def can_jump(p1,p2):
    return pebbles[p1]+pebbles[p2] == p2 - p1

def update_max(new_max):
    global max_dist
    if new_max > max_dist:
        max_dist = new_max

def get_jumps(starting_pos):
    global jumps
    travel_dist = pebbles[starting_pos]
    exclude_locations = []
    while starting_pos + travel_dist <= num_pebbles:
        if can_jump(starting_pos, starting_pos+travel_dist) and not starting_pos+travel_dist in exclude_locations:
            jumps[starting_pos: starting_pos+travel_dist]
            exclude_locations.append(starting_pos+travel_dist)
            travel_dist = pebbles[starting_pos]
        else:
            


## Output
# main()
