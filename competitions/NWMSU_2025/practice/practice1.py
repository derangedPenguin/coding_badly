'''
Oh no! Now towards the end of the term there are all kinds of exams and final projects closing in! By your side you of course have your trusty stash of caffeinated drinks. Tea, coffee, energy drinks and more can help you cover all the material and finish all the projects in the time you have. Such drinks are however far from free, so now the question is how deep you have to dip into your stash to get everything done in time.

Each drink halves the number of hours a task will take, rounded down to the nearest whole number of hours. Two drinks will thus half the hours in this manner twice. For example a 
 hour project goes down to a single hour after two drinks.

Each exam or project has a deadline and has to be finished by that date. Everything is given in hours and we of course assume there will be no sleep or other distractions from working on studies.

Input
The first line of input contains a single positive integer 
, the number of tasks. Next there are 
 lines, each containing two integers 
. 
 denotes the number of hours it will take to complete the task without caffeine, 
 denotes how many hours from now the task has to be finished.

Output
Print the minimum number of caffeinated drinks it will take to finish everything in time. You may assume that all tasks can be finished in time given enough caffeine. Note that this is not true to real life.
'''

## Input
num_of_tasks = int(input())
tasks = {}
for i in range(num_of_tasks):
    taske_length, due_time = [int(i) for i in input().split()]
    tasks[taske_length] = due_time

## Logic
total_drinks = 0

for task_length, due_time in tasks.items():
    while task_length > due_time:
        task_length //= 2
        total_drinks += 1

print(total_drinks)