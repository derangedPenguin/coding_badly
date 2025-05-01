## Inputs
track_length = float(input('Z: '))
my_speed = float(input('S1: '))
my_laps_completed = int(input('W: '))
times_lapped = int(input('X: ')) + 1
Sue_hours_done_faster_than_me = float(input('M: ')) / 60

## Setup
my_time = track_length / my_speed * my_laps_completed
sue_laps_completed = my_laps_completed + times_lapped
sue_time = my_time - Sue_hours_done_faster_than_me

## Run
sue_rate = track_length * sue_laps_completed / sue_time
print(round(sue_rate, 2))