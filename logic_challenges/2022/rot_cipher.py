ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def build_key(rot_num):
    global code_dict

    for i in range(26):
        code_dict[ALPHABET[i]] = ALPHABET[((i+rot_num) if action == 'E' else (i-rot_num)) % 26]

def convert_char(char: str):
    if char.lower() in ALPHABET:
        new_char: str = code_dict[char.lower()]
        if char.isupper():
            new_char = new_char.upper()
        return new_char
    else:
        return char
    
def brute():
    potentials = []
    for i in range(1,27):
        build_key(i)
        potentials.append(''.join([convert_char(char) for char in list(message)]))
    print(''.join([str(i+1) + ' ' + potentials[i] + '\n' for i in range(len(potentials))]))

rotation_num = input('\nEnter number of rotations\n > ')
action = input('\nEncrypt "E", or Decrypt "D"?\n > ')
message = input('\nMessage\n > ')

code_dict = {}

if rotation_num == 'b':
    brute()
else:
    rotation_num = int(rotation_num)

if message[0].isnumeric():
    message = str(ALPHABET[char] for char in message.split(' '))




print(''.join([convert_char(char) for char in list(message)]))