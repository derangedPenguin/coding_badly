'''firetrucks'''
## Input
n = int(input())
peoples_nums = [{int(i) for i in input().split()[1:]} for _ in range(n)]
# [{nums}]

# class Node:
#     def __init__(self):
#         self.connections = []

## Logic
def main():
    pairs = []
    for i in range(n): # person 1
        start_len = len(pairs)
        for j in range(n): # person 2
            if i == j: continue

            for num in peoples_nums[i]:
                if num in peoples_nums[j]:
                    pairs.append((i,j,num))
        if start_len == pairs:
            print('impossible')
            return
    
    nodes = {i:[] for i in range(n)}
    for pair in pairs:
        nodes[pair[0]].append(pair[1])
        nodes[pair[1]].append(pair[0])

    web = [nodes[0]]
    checked_nodes = []

    for node in web:
        for connection in node:
            if connection not in checked_nodes:
                web.append(nodes[connection])
                checked_nodes.append(connection)
    
    
    if len(web) == len(nodes):
        print('impossible')
    else:
        for pair in pairs:
            print(f'{pair[0]} {pair[1]} {pair[2]} ')
    
    
    
    


## Output
main()
