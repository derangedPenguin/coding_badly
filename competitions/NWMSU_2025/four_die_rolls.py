'''Four Die Rolls'''
## Input
rolls = int(input())
nums = [int(i) for i in input().split()]

## Logic
if rolls == 1:
    print("60 156")
elif rolls == 2:
    if nums[0] == nums[1]:
        print("0 36")
    else:
        print("12 24")
else:
    if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
        print("0 6")
    else:
        print("3 3")


## Output

