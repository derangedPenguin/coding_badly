'''Passwords'''
## Input
minlen, maxlen = [int(i) for i in input().split()]
num_blacklisted = int(input())
blacklist = [input() for i in range(num_blacklisted)]

## Logic
# setup
char_nums = {0:'o', 1:'i',3:'e',5:'s',7:'t'}
num_chars_per_digit = 26*2 + 10



## Output

