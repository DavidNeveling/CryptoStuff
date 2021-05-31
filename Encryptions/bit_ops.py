import random, math

def int_to_bits(num):
    if num == 0:
        return ''
    return int_to_bits(num // 2) + str(num % 2)

def fill_to_byte(bit_string):
    if len(bit_string) == 8:
        return bit_string
    return fill_to_byte('0' + bit_string)

def char_to_bits(char):
    return fill_to_byte(int_to_bits(ord(char)))

def string_to_bits(string):
    if string == '':
        return ''
    return string_to_bits(string[:-1]) + char_to_bits(string[-1])

def key_gen(length, key):
    random.seed(key)
    return ''.join([str(round(random.random())) for x in range(length)])

# i don't like how i'm doing this, I just wanna get something down
def add_bit_strings(str1, str2):
    carry_bit = 0
    added_string = ''
    for i in range(len(str1) - 1, 0, -1):
        if str1[i] == '0' and str2[i] == '0':
            added_string = str(0 + carry_bit) + added_string
            carry_bit = 0
        if (str1[i] == '1' and str2[i] == '0') or (str1[i] == '0' and str2[i] == '1'):
            if carry_bit == 0:
                added_string = '1' + added_string
            if carry_bit == 1:
                added_string = '0' + added_string
        if str1[i] == '1' and str2[i] == '1':
            added_string = str(0 + carry_bit) + added_string
            carry_bit = 1
    if str1[0] == '0' and str2[0] == '0':
            added_string = str(0 + carry_bit) + added_string
            carry_bit = 0
    if (str1[0] == '1' and str2[0] == '0') or (str1[0] == '0' and str2[0] == '1'):
        if carry_bit == 0:
            added_string = '1' + added_string
        if carry_bit == 1:
            added_string = '0' + added_string
    if str1[0] == '1' and str2[0] == '1':
        added_string = str(0 + carry_bit) + added_string
        carry_bit = 1
    index = -1
    added_string = list(added_string)
    while carry_bit == 1:
        if added_string[index] == '1':
            added_string[index] = '0'
        else:
            added_string[index] = '1'
            carry_bit = 0
        index -= 1
    return ''.join(added_string)

def encrypt(message, key):
    bit_message = string_to_bits(message)
    bit_key = key_gen(len(bit_message), key)
    print('bit key = ' + bit_key)
    return add_bit_strings(bit_message, bit_key)

def decrypt(encryption, key):
    bit_key = key_gen(len(encryption), key)
    print('bit key = ' + bit_key)
    return add_bit_strings(encryption, bit_key)

def test():
    message = 'apple'
    print('message = ' + string_to_bits(message))
    encryption = encrypt(message, 1)
    print('encryption = ' + encryption)
    decryption = decrypt(encryption, 1)
    print('decryption = ' + decryption)

def main():
    test()

if __name__ == '__main__':
    main()