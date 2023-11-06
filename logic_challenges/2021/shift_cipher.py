encrypt_key = int(input('Enter the encryption key: '))
num_digits = int(input('Enter number of digits to encrypt: '))
digits = []
for i in range(num_digits):
    digits.append(int(input(f'Enter digit {i}: ')))

encrypted = [(i + encrypt_key) % 10 for i in digits]
print(''.join([str(i) for i in encrypted]))

decrypt_key = int(input('Enter decryption key: '))

decrypted = [(int(i) - decrypt_key) % 10 for i in encrypted]
print(''.join([str(i) for i in decrypted]))