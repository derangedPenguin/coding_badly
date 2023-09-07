def avg(*args):
    return (sum(args) / len(args))

def rect_area(side1, side2):
    return side1 * side2

while True:
    run_func = input('average or area of rect?: ')
    match run_func:
        case 'average':
            print('enter a non-numeric character to stop')
            nums = []
            while True:
                new_num = input('number: ')
                try:
                    nums.append(int(new_num))
                except:
                    break
            print('Average: '+str(avg(*nums[:-1])))
        case 'area':
            print('Area: '+str(rect_area(int(input('side 1: ')), int(input('side 2: ')))))


            