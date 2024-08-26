import json

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

class SubCipher:
    '''
    Container class for methods involving substitution ciphers
    '''
    @staticmethod
    def ceaser_brute(msg):
        #
        possibilities = []
        for i in range(1,27):
            possibilities.append(SubCipher.figure(msg, 'shift', decode=True, count=i))
        return '\n'.join(possibilities)

    @staticmethod
    def apply_keymap(msg, keymap: dict, decode=False):
        if decode:
            keymap = {b:a for a, b in keymap.items()}

        new_msg = []
        for char in msg:
            is_upper = char.isupper()
            try:
                #convert char via keymap, persist upper/lower-case
                new_msg.append(keymap[char.lower()].upper() if is_upper else keymap[char.lower()])
            except KeyError:
                new_msg.append(char)
        return ''.join(new_msg)
    
    @staticmethod
    def gen_keymap(type, kwargs):
        keymap = {}

        match type:
            case 'keyword':
                '''REQUIRED KWARGS: keyword'''
                #construct list of keymap values
                values = list(kwargs['keyword'])
                for letter in ALPHABET:
                    if letter not in values:
                        values.append(letter)
                
                #construct full keymap dict
                for i, letter in enumerate(ALPHABET):
                    keymap[letter] = values[i]

            case 'shift':
                '''REQUIRED KWARGS: count'''
                for i, letter in enumerate(ALPHABET):
                    keymap[letter] = ALPHABET[(i+kwargs['count'])%len(ALPHABET)]

        return keymap
    
    def figure(msg, type, decode=False, **kwargs):
        keymap = SubCipher.gen_keymap(type, kwargs=kwargs)
        return SubCipher.apply_keymap(msg, keymap, decode)
                
    @staticmethod
    def get_pretty_keymap(keymap: dict):
        output = ''
        for a, b in keymap.items():
            output += f'{a}:{b}\n'
        return output

input_string = input('decode: ')

result = SubCipher.ceaser_brute(input_string)

print()
# 'wklv lv d vhfuhw phvvdjh'