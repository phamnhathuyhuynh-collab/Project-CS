text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ""
    
    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else :
            key_char = key[key_index % len(key)]
            key_index += 1
            
            offset = alphabet.find(key_char)
            index = alphabet.find(char)

            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

def encryption(message, key):
    return vigenere(message, key)
print(f'Encryption: {encryption(text, custom_key)}\n')

def decryption(message, key):
    return vigenere(message, key, -1)
print(custom_key);
print(f'\nDecryption: {decryption(text, custom_key)}')
