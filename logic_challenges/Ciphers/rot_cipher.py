
class Thingy:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self) -> None:
        rotation_num = int(input('\nEnter number of rotations\n > '))
        action = input('\nEncrypt "E", or Decrypt "D"?\n > ')
        message = input('\nMessage\n > ')
    
    def nums_to_chars():
        if message[0].isnumeric():
            message = str(ALPHABET[char] for char in message.split(' '))


    code_dict = {}

    for i in range(26):
        code_dict[ALPHABET[i]] = ALPHABET[((i+rotation_num) if action == 'E' else (i-rotation_num)) % 26]

    def convert_code(char: str):
        if char.lower() in ALPHABET:
            new_char: str = code_dict[char.lower()]
            if char.isupper():
                new_char = new_char.upper()
            return new_char
        else:
            return char


    print(''.join([convert_code(char) for char in list(message)]))