from math import pi

opp_speed = 30
opp_time = 125 * pi / opp_speed

my_speed = float(input('my speed: '))

# i = 0

prize_money = lambda n: 1000-(n*100)

my_time = lambda n: pi * (125 * (18-n)/18) / my_speed

for i in range(10):
# while True:
    if my_time(i) <= opp_time:# and prize_money(i) > 0:
        print(f'Start at {i*10} degree angle mark for {prize_money(i)}$')
        break
    # if prize_money(i) == 0:
    #     print('No possible starting position with reward')
    #     break
    # i += 1
else:
    print('No possible starting position with reward')

