import random as rand

'''
finding best strategy to guess in a series of multiple choice questions, need to test completely random, random from set, and random from set with extra
'''
BASEANSWERS = [1,2,3,4]
crnt_list = []
test_range = 9
prev_answer = 0
strats = {'random':0,'zigzag':0,'A100':0,'A50-B50':0}
strat_totals = {'random':0,'zigzag':0,'A100':0,'A50-B50':0}


def gen_rand_list(length, method):
    builtList = []
    if method == 'default':
        for i in range(length):
            builtList.append(rand.choice(BASEANSWERS))
        return builtList
    elif method == 'cyclic':
        holdList = []
        for i in BASEANSWERS:
            holdList.append(i)
        for i in range(100):
            if holdList != []:
                item = rand.choice(holdList)
                builtList.append(item)
                holdList.remove(item)
            else:
                for i in BASEANSWERS:
                    holdList.append(i)
        return builtList
    elif method == 'cyclic1':
        holdList = []
        for i in BASEANSWERS:
            holdList.append(i)
        holdList.append(rand.choice(BASEANSWERS))
        for i in range(100):
            if holdList != []:
                item = rand.choice(holdList)
                builtList.append(item)
                holdList.remove(item)
            else:
                for i in BASEANSWERS:
                    holdList.append(i)
                holdList.append(rand.choice(BASEANSWERS))
        return builtList

def guess(strat):
    global prev_answer
    if strat == 'A100':
        return 1
    elif strat == 'random':
        return rand.choice(BASEANSWERS)
    elif strat == 'zigzag':
        if prev_answer < len(BASEANSWERS):
            prev_answer += 1
        else:
            prev_answer = 1
        return prev_answer
    elif strat == 'A50-B50':
        if prev_answer == 1:
            prev_answer = 2
            return prev_answer
        else:
            prev_answer = 1
            return prev_answer

while True:
    runs = int(input('runs: '))
    method = 'cyclic'
    for i in range(runs):
        strats = {'random':0,'zigzag':0,'A100':0,'A50-B50':0}
        rand_list = gen_rand_list(100,method)

        for strat in list(strats.keys()):
            for answer in rand_list:
                if guess(strat) == answer:
                    strats[strat] += 1
                    strat_totals[strat] += 1
    for i in strat_totals:
        strat_totals[i] /= runs

    print(strat_totals,end='\n\n')

    '''if input('break?: ') == 'yes':
        break'''