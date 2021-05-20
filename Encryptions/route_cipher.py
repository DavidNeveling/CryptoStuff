import math
def create_table(message, columns):
    index = 0
    table = [['' for j in range(int(columns))] for i in range(math.ceil(len(message) / float(columns)))]
    for r in range(len(table)):
        for c in range(int(columns)):
            if index >= len(message):
                table[r][c] = 'X'
            else:
                table[r][c] = message[index]
                index += 1
    return table

def encrypt_clockwise(table):
    r = 0
    c = len(table[0]) - 1
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    return encrypt_scheme(table, (r, c), directions)

def encrypt_counter_clockwise(table):
    r = 0
    c = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return encrypt_scheme(table, (r, c), directions)

def encrypt_scheme(table, start, directions_list):
    r, c = start
    visited_table = init_visited_table(table)
    directions = directions_list
    d = 0
    encryption = ''
    done = False
    while not done:
        encryption += table[r][c]
        visited_table[r+1][c+1] = True
        row_move = directions[d][0]
        col_move = directions[d][1]
        if visited_table[r+1+row_move][c+1+col_move]:
            d = (d + 1) % len(directions)
            if visited_table[r+1+directions[d][0]][c+1+directions[d][1]]:
                done = True
        r += directions[d][0]
        c += directions[d][1]
    return encryption


def encrypt(message, key):
    columns = (key / 2 + 2) % 8 # min cols = 2 max cols = 8
    table = create_table(message, columns)
    f = None
    if key % 2 == 0:
        f = encrypt_counter_clockwise
    else:
        f = encrypt_clockwise
    return f(table)

def decrypt_counter_clockwise(encryption, columns):
    r = 0
    c = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return decrypt_scheme(encryption, columns, (r, c), directions)

def decrypt_clockwise(encryption, columns):
    r = 0
    c = columns - 1
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    return decrypt_scheme(encryption, columns, (r, c), directions)

def decrypt_scheme(encryption, columns, start, directions_list):
    table = [['' for j in range(int(columns))] for i in range(math.ceil(len(encryption) / float(columns)))]
    r, c = start
    visited_table = init_visited_table(table)
    directions = directions_list
    d = 0
    index = 0
    done = False
    while not done:
        table[r][c] = encryption[index]
        index += 1
        visited_table[r+1][c+1] = True
        row_move = directions[d][0]
        col_move = directions[d][1]
        if visited_table[r+1+row_move][c+1+col_move]:
            d = (d + 1) % len(directions)
            if visited_table[r+1+directions[d][0]][c+1+directions[d][1]]:
                done = True
        r += directions[d][0]
        c += directions[d][1]
    return ''.join([''.join(s) for s in table])

def init_visited_table(table):
    visited_table = [[False for j in range(len(table[0]) + 2)] for i in range(len(table) + 2)]
    for i in range(len(visited_table[0])):
        visited_table[0][i] = True
        visited_table[len(visited_table) - 1][i] = True
    for i in range(1, len(visited_table) - 1):
        visited_table[i][0] = True
        visited_table[i][len(visited_table[0]) - 1] = True
    return visited_table

def decrypt(encryption, key):
    columns = (key / 2 + 2) % 8 # min cols = 2 max cols = 8
    f = None
    if key % 2 == 0:
        f = decrypt_counter_clockwise
    else:
        f = decrypt_clockwise
    return f(encryption, columns)

def test():
    message = 'this is a message to encrypt. also, how are you?'
    print('message = ' + message)
    encryption = encrypt(message, 2)
    print('encryption = ' + encryption)
    decryption = decrypt(encryption, 2)
    print('decryption = ' + decryption)

def main():
    test()

if __name__ == '__main__':
    main()