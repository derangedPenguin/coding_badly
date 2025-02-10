import os

def get_options(prompt:str, **options:dict[str,set[str]]) -> str:
    while True:
        inp = input(f'\n{prompt} [{'/'.join(list(options.keys()))}]\n > ').lower().strip()
        for option, versions in options.items():
            if inp in versions:
                return option
        print('please enter a valid input')
def get_yes_no(prompt:str) -> bool:
    return get_options(prompt, yes={'y','yes'}, no={'n','no'}) == 'yes'

def output(output_txt:str) -> None:
    output_mode = 'file'#get_options('Output mode?', file={'f','file'}, shell={'c','console','s','shell'})
    if output_mode == 'file':
        should_del = get_yes_no('clear output file?')
        with open('output.txt', ('w' if should_del else 'a')) as file:
            file.write('\n------------------New Entry--------------------\n' + output_txt)
    elif output_mode == 'console':
        print(output_txt)

        should_clear = get_yes_no('Clear shell?')
        if should_clear:
            os.system('clear')