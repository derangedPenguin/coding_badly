from sys import exit
## Inputs
minimum_assignments, hours_available = [int(i) for i in input('m,h: ').split(',')]

assignments = input('assignments\n > ').strip('()').split('), (')
for i, val in enumerate(assignments):
    assignments[i] = [int(i) for i in val.split(',')]
# print(assignments)

##Inits
accumulated_score = 0
assignments_done = 0

## Program
def use_time(val):
    global hours_available, assignments, assignments_done
    if val > hours_available:
        print(assignments)
        print(f'Willie got a score of {accumulated_score} by completing {assignments_done} assignments')
        exit()
    else:
        hours_available -= val
        assignments_done += 1
def use_time_score_based(val):
    global hours_available, assignments, assignments_done
    if val > hours_available:
        print(assignments)
        return False
    else:
        hours_available -= val
        assignments_done += 1
    return True

#handle m
assignments.sort(key=lambda a:a[0])
print(assignments)
for i in range(minimum_assignments):
    print(tuple(assignments[i]))
    use_time(assignments[i][0])
    accumulated_score += assignments[i][1]
for i in range(minimum_assignments):
    del assignments[0]

# higher scores
assignments.sort(key=lambda a:a[1], reverse=True)
for i, assignment in enumerate(assignments):
   
    # if assignment[0] > hours_available:
    #     continue
    if use_time_score_based(assignments[i][0]):
        accumulated_score += assignments[i][1]
    # print(tuple(assignment))
    

print(f'Willie got a score of {accumulated_score} by completing {assignments_done} assignments')