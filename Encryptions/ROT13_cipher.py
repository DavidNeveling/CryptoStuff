import string, caeser_cipher

def encrypt(message):
    encryption_space = ''
    if message[0] in string.ascii_uppercase:
        encryption_space = string.ascii_uppercase
    else:
        encryption_space = string.ascii_lowercase
    return caeser_cipher.encrypt(message, encryption_space, 13)

def decrypt(encryption):
    encryption_space = ''
    if encryption[0] in string.ascii_uppercase:
        encryption_space = string.ascii_uppercase
    else:
        encryption_space = string.ascii_lowercase
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