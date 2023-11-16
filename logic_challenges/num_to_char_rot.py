ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

rotation_num = 6
message = input('\nMessage\n > ')

#message = str([ALPHABET[int(char)] for char in message.split(' ')])
new_msg = []
for char in message.split(' '):
    try:
        new_msg.append(ALPHABET[int(char)])
    except:
        pass

message = str(new_msg)

code_dict = {}

for i in range(26):
    code_dict[ALPHABET[i]] = ALPHABET[(i-rotation_num) % 26]

def convert_code(char: str):
    if char.lower() in ALPHABET:
        new_char: str = code_dict[char.lower()]
        if char.isupper():
            new_char = new_char.upper()
        return new_char
    else:
        return char


print(''.join([convert_code(char) for char in list(message)]))