num_of_cases = int(input())

for case in range(num_of_cases):
    roof_size, num_of_hatches = [int(i) for i in input().split()]
    hatches = [
        tuple(int(i) for i in input().split()) for i in range(num_of_hatches)
    ]