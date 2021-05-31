import string

def encrypt(message, message_space = string.printable, shift = 1):
    encryption = ''
    for character in message:
        encryption += message_space[(message_space.find(character) + shift) % len(message_space)]
    return encryption

def decrypt(encryption, message_space = string.printable, shift = 1):
    decryption = ''
    for character in encryption:
        decryption += message_space[(message_space.find(character) - shift) % len(message_space)]
    return decryption

def test():
    message = 'abc'
    print('message = ' + message)
    encryption = encrypt(message)
    print('encryption = ' + encryption)
    decryption = decrypt(encryption)
    print('decryption = ' + decryption)

def main():
    test()

if __name__ == '__main__':
    main()