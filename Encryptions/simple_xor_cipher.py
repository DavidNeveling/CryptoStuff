def encrypt(message, key):
    key_index = 0
    encryption = ''
    for character in message:
        encryption += chr(ord(character) ^ ord(key[key_index]))
        if key_index > len(key):
            key_index = 0
    return encryption

def decrypt(encryption, key):
    return encrypt(encryption, key)

def test():
    message = 'this is a message to encrypt'
    key = 'face/off'
    print('message = ' + message)
    encryption = encrypt(message, key)
    print('encryption = ' + encryption)
    decryption = decrypt(encryption, key)
    print('decryption = ' + decryption)

def main():
    test()

if __name__ == '__main__':
    main()