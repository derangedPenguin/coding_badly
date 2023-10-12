def odd_echo(N, *args):
    for i in range(input()):
        if i % 2 != 0:
            print(input())
        else:
            input()

odd_echo(10, 'only', 'if', 'these', 'oddindexed', 'words', 'appear', 'are', 'you', 'correct', 'output')