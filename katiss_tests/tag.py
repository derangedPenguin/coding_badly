##Inputs
line1 = input()
num_of_students, num_of_tags = [int(i) for i in line1.split()]

line2 = input()
students = line2.split()

##Setup
currently_it = {students[0], }
cheaters = set()
cheat_incidents = []

##Run
for i in range(num_of_tags):
    linei = input()
    tagger, null, tagged = linei.split()

    if tagger not in currently_it:
        cheaters.add(tagger)
        currently_it.add(tagged)
    else:
        currently_it.add(tagged)
        currently_it.remove(tagger)

##Output
print(len(cheaters))
print(' '.join(sorted(cheaters)))
