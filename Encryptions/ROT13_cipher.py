import message_space, caeser_cipher

def encrypt(message):
    encryption_space = ''
    if message[0] in message_space.UPPERCASE_CHARACTERS:
        encryption_space = message_space.UPPERCASE_CHARACTERS
    else:
        encryption_space = message_space.LOWERCASE_CHARACTERS
    return caeser_cipher.encrypt(message, encryption_space, 13)

def decrypt(encryption):
    encryption_space = ''
    if encryption[0] in message_space.UPPERCASE_CHARACTERS:
        encryption_space = message_space.UPPERCASE_CHARACTERS
    else:
        encryption_space = message_space.LOWERCASE_CHARACTERS
    return caeser_cipher.decrypt(encryption, encryption_space, 13)

def test():
    message = 'abcmnoxyz'
    print('message = ' + message)
    encryption = encrypt(message)
    print('encryption = ' + encryption)
    decryption = decrypt(encryption)
    print('decryption = ' + decryption)

def main():
    test()

if __name__ == '__main__':
    main()