'''yoshi'''
## Input
num_pebbles = int(input())
pebbles = tuple(int(i) for i in input().split())

## Logic
def can_jump(p1,p2):
    return pebbles[p1]+pebbles[p2] == p2 - p1

def find_path(starting_index, path):
    for i in range(num_pebbles-1, -1, -1):
        if can_jump(starting_index, i):
            path.append(i)
            return find_path(i, path)
    return starting_index

def main():
    dists = []
    for i in range(num_pebbles):
        dists.append( find_path(i, []) - i )
        print(dists)
    
    print(max(dists))

## Output
main()
